from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from math import sqrt, pow
from random import randint

from typing import List

from .game_objects import GameObjet, Spaceship, Enemy


def init_spaceship(self, speed: int, start_x: int, start_y: int, fuel: int, lives: int) -> Spaceship:
        with self.canvas:
            Color(1, 1, 1)
            body = Ellipse(pos=(start_x, start_y), size=(dp(40), dp(40)))
            spaceship = Spaceship(body, speed, fuel, lives, 0)
            return spaceship


def __init_enemy(self) -> Enemy:
      with self.canvas:
            Color(1, 0, 0)
            body = Ellipse(pos=(500, 500), size=(40, 40))
            enemy = Enemy(body, 10, 10, True, True)
            return enemy


def init_enemies(self, num: int) -> List[Enemy]:
      list_enemies = []
      for i in range(0, num):
            list_enemies.append(__init_enemy(self))
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
            e.speed_x = randint(1, 10)
      elif x < 0 and not e.right:
            e.right = True
            e.speed_x = randint(1, 10)
      
      if y + h <= s.height and e.up:
            y+=e.speed_y
      elif y >= 0 and not e.up:
            y-=e.speed_y

      if y + h > s.height and e.up:
            e.up = False
            e.speed_y = randint(1, 10)
      elif y < 0 and not e.up:
            e.up = True
            e.speed_y = randint(1, 10)

      e.body.pos = (x, y)


def enemy_change_direction(e: Enemy):
      e.up = not e.up
      e.right = not e.right


def is_collision(obj1: GameObjet, obj2: GameObjet) -> bool:
      x1, y1 = obj1.body.pos
      w1, h1 = obj1.body.size
      x2, y2 = obj2.body.pos
      w2, h2 = obj2.body.size
      d = sqrt(pow(x1-x2,2) + pow(y1-y2,2)) - w1 / 2 - w2 /2
      if d < 0:
            return True
      else:
            return False


def distance_spaceship_with_enemy(s: Spaceship, e: Enemy) -> int:
      return None


def __collision_handler_spaceship_enemy(screen: Screen, spaceship: Spaceship, enemy: Enemy):
        if is_collision(spaceship, enemy):
            enemy_change_direction(enemy)
            if spaceship.timer_immortal <= 0:
                spaceship.lives -=1
                screen.lives_remaining = str(spaceship.lives)
                screen.spaceship.timer_immortal = 4 * 60 # 4 * 60 fps


def collision_handler_spaceship_enemies(screen: Screen, spaceship: Spaceship, lenemies: List[Enemy]):
      for e in lenemies:
            __collision_handler_spaceship_enemy(screen, spaceship, e)