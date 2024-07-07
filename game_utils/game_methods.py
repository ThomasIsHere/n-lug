from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from math import sqrt, pow
from random import randint


from .game_objects import GameObjet, Spaceship, Enemy


def init_spaceship(self, speed: int, start_x: int, start_y: int, fuel: int, lives: int) -> Spaceship:
        with self.canvas:
            Color(1, 1, 1)
            body = Ellipse(pos=(start_x, start_y), size=(dp(40), dp(40)))
            spaceship = Spaceship(body, speed, fuel, lives, 0)
            return spaceship


def init_enemy(self) -> Enemy:
      with self.canvas:
            Color(1, 0, 0)
            body = Ellipse(pos=(500, 500), size=(40, 40))
            enemy = Enemy(body, 10, 10, True, True)
            return enemy


def enemy_random_move(self, e: Enemy):
      x, y = e.body.pos
      w, h = e.body.size

      if x + w <= self.width and e.right:
            x+=e.speed_x
      elif x >= 0 and not e.right:
            x-=e.speed_x

      if x + w > self.width and e.right:
            e.right = False
            e.speed_x = randint(1, 10)
      elif x < 0 and not e.right:
            e.right = True
            e.speed_x = randint(1, 10)
      
      if y + h <= self.height and e.up:
            y+=e.speed_y
      elif y >= 0 and not e.up:
            y-=e.speed_y

      if y + h > self.height and e.up:
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