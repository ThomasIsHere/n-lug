from kivy.graphics.vertex_instructions import Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.screenmanager import Screen
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
            screen.spaceship_canvas_color = Color(1, 1, 1) # white
            body = Ellipse(
                        pos=(start_x, start_y),
                        size=(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                  )
            spaceship = Spaceship(body, [], speed, fuel, lives, timer_immortal)
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
                  [],
                  randint(1, ENEMY_MAX_SPEED),
                  randint(1, ENEMY_MAX_SPEED),
                  choice([True, False]),
                  choice([True, False])
                  )
            return enemy


def __return_enemy_random_init_pos(screen: Screen) -> tuple[int, int]:
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

      obj1_left = False
      obj1_down = False

      if x1 < x2:
            obj1_left = True

      if y1 < y2:
            obj1_down = True

      diameter_sub = 0.0

      if obj1_left and obj1_down:
            diameter_sub = w1
      elif not obj1_left and obj1_down:
            diameter_sub = w1
      elif not obj1_left and not obj1_down:
            diameter_sub = w2
      elif obj1_left and not obj1_down:
            diameter_sub = w2

      d = __distance_2_points(x1, y1, x2, y2) - diameter_sub
      if d < 0:
            return True
      else:
            return False
      

def __overlap(obj1: GameObjet, obj2: GameObjet) -> bool:
      x1, y1 = obj1.body.pos
      w1, h1 = obj1.body.size
      x2, y2 = obj2.body.pos
      w2, h2 = obj2.body.size

      x_overlap = False
      y_overlap = False
      overlap = False

      if (
            __point_in_range(x1, x2, x2 + w2) 
            or __point_in_range(x1 + w1, x2, x2 + w2)
            or __point_in_range(x2, x1, x1 + w1)
            or __point_in_range(x2 + w2, x1, x1 + w1)
            ):
            x_overlap = True

      if (
            __point_in_range(y1, y2, y2 + h2) 
            or __point_in_range(y1 + h1, y2, y2 + h2)
            or __point_in_range(y2, y1, y1 + h1) 
            or __point_in_range(y2 + h2, y1, y1 + h1)
            ):
            y_overlap = True

      if x_overlap and y_overlap:
            overlap = True
      
      return overlap


def __point_in_range(p1, p2, p3):
      if p1 >= p2 and p1 <= p3:
            return True
      else:
            return False


def __distance_2_points(x1, y1, x2, y2) -> float:
      return sqrt(pow(x1-x2,2) + pow(y1-y2,2))


def __collision_handler_spaceship_enemy(screen: Screen, spaceship: Spaceship, enemy: Enemy):
      if not __overlap(spaceship, enemy) and enemy in spaceship.listOverlap:
                  spaceship.listOverlap.remove(enemy)
      if __is_collision(spaceship, enemy):
            __spaceship_stops(screen)
            if enemy not in spaceship.listOverlap:
                  enemy_change_direction(enemy)
            if __overlap(spaceship, enemy) and enemy not in spaceship.listOverlap:
                  spaceship.listOverlap.append(enemy)
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
                        if not __overlap(e1, e2) and e2 in e1.listOverlap:
                              e1.listOverlap.remove(e2)
                        if __is_collision(e1, e2):
                              if e2 not in e1.listOverlap:
                                    enemy_change_direction(e1)
                              if __overlap(e1, e2) and e2 not in e1.listOverlap:
                                    e1.listOverlap.append(e2)


def do_not_touch_spaceship(screen: Screen, go_x: int, go_y: int) -> bool:
    x, y = screen.spaceship.body.pos
    center_x = x + SPACESHIP_WIDTH /2
    center_y = y + SPACESHIP_HEIGHT /2
    if (
        (center_x - SPACESHIP_WIDTH < go_x and go_x < center_x + SPACESHIP_WIDTH)
        and (center_y - SPACESHIP_HEIGHT < go_y and go_y < center_y + SPACESHIP_HEIGHT)
    ):
        return False
    else:
        return True


def __spaceship_stops(screen: Screen):
      x, y = screen.spaceship.body.pos
      screen.dict_destination = {
                                "go_to_x": x, 
                                "go_to_y": y, 
                                "speed_corrector_x": 0.0, 
                                "speed_corrector_y": 0.0,
                                "is_moving": False
                             }
      

def immortal_color_handler(screen: Screen, spaceship: Spaceship):
      if spaceship.timer_immortal <= 0:
            screen.spaceship_canvas_color.rgba = (1, 1, 1, 1) # white
      else:
            screen.spaceship_canvas_color.rgba = (1, 1, 1, .4) # white 60% transparent