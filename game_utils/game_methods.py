from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from math import sqrt, pow
from random import randint, choice

from typing import List

from .game_objects import GameObjet, Spaceship, Enemy
from .game_constants import (
      SPACESHIP_HEIGHT,
      SPACESHIP_WIDTH,
      SCREEN_HEIGHT,
      SCREEN_WIDTH,
      ENEMY_WIDTH,
      ENEMY_HEIGHT,
      FPS,
      ENEMY_MAX_SPEED
      )


def init_spaceship(
            screen: Screen,
            speed: int, 
            start_x: int, 
            start_y: int, 
            fuel: int,
            lives: int,
            timer_immortal: int
            ) -> Spaceship:
        with screen.canvas:
            Color(1, 1, 1) # white
            body = Ellipse(
                        pos=(start_x, start_y),
                        size=(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                  )
            spaceship = Spaceship(body, speed, fuel, lives, timer_immortal)
            return spaceship


def __init_enemy(screen: Screen) -> Enemy:
      with screen.canvas:
            Color(1, 0, 0) # red
            body = Ellipse(
                  pos=__return_enemy_random_init_pos(screen),
                  size=(ENEMY_WIDTH, ENEMY_HEIGHT),
                  )
            enemy = Enemy(
                  body,
                  randint(1, ENEMY_MAX_SPEED),
                  randint(1, ENEMY_MAX_SPEED),
                  choice([True, False]),
                  choice([True, False])
                  )
            return enemy


def __return_enemy_random_init_pos(screen: Screen) -> tuple[int, int]:
      print(screen.enemies)
      enemy_x = randint(0, SCREEN_WIDTH - int(ENEMY_WIDTH))
      enemy_y = randint(0, SCREEN_HEIGHT - int(ENEMY_HEIGHT))
      spaceship_x, spaceship_y = screen.spaceship.body.pos
      d = __distance_2_points(enemy_x, enemy_y, spaceship_x, spaceship_y)
      # enemy pops at least 4 times the distance of spaceship width
      if d > 4 * SPACESHIP_WIDTH:
            return (enemy_x, enemy_y)
      return __return_enemy_random_init_pos(screen)
      

def init_enemies(screen: Screen, num: int) -> List[Enemy]:
      list_enemies = []
      while(num > 0):
            list_enemies.append(__init_enemy(screen))
            num-=1
      return list_enemies


def enemy_random_move(s: Screen, e: Enemy):
      x, y = e.body.pos
      w, h = e.body.size

      if x + w <= s.width and e.right:
            x+=e.speed_x
      elif x >= 0 and not e.right:
            x-=e.speed_x

      if x + w > s.width and e.right:
            e.right = False
            e.speed_x = randint(1, ENEMY_MAX_SPEED)
      elif x < 0 and not e.right:
            e.right = True
            e.speed_x = randint(1, ENEMY_MAX_SPEED)
      
      if y + h <= s.height and e.up:
            y+=e.speed_y
      elif y >= 0 and not e.up:
            y-=e.speed_y

      if y + h > s.height and e.up:
            e.up = False
            e.speed_y = randint(1, ENEMY_MAX_SPEED)
      elif y < 0 and not e.up:
            e.up = True
            e.speed_y = randint(1, ENEMY_MAX_SPEED)

      e.body.pos = (x, y)


def enemy_change_direction(e: Enemy):
      e.up = not e.up
      e.right = not e.right


def __is_collision(obj1: GameObjet, obj2: GameObjet) -> bool:
      x1, y1 = obj1.body.pos
      w1, h1 = obj1.body.size
      x2, y2 = obj2.body.pos
      w2, h2 = obj2.body.size
      d = __distance_2_points(x1, y1, x2, y2) - w1 / 2 - w2 /2
      if d < 0:
            return True
      else:
            return False


def __distance_2_points(x1, y1, x2, y2) -> float:
      return sqrt(pow(x1-x2,2) + pow(y1-y2,2))


def __collision_handler_spaceship_enemy(screen: Screen, spaceship: Spaceship, enemy: Enemy):
        if __is_collision(spaceship, enemy):
            enemy_change_direction(enemy)
            if spaceship.timer_immortal <= 0:
                spaceship.lives -=1
                screen.lives_remaining = str(spaceship.lives)
                screen.spaceship.timer_immortal = 4 * FPS # 4 * FPS fps


def collision_handler_spaceship_enemies(screen: Screen, spaceship: Spaceship, lenemies: List[Enemy]):
      for e in lenemies:
            __collision_handler_spaceship_enemy(screen, spaceship, e)


def collision_handler_between_enemies(screen: Screen, lenemies: List[Enemy]):
      for e1 in lenemies:
            for e2 in lenemies:
                  if e1 is not e2:
                        if __is_collision(e1, e2):
                              enemy_change_direction(e1)