from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from math import sqrt, pow


from .game_objects import GameObjet, Spaceship, Enemy


def init_spaceship(self, speed: int, start_x: int, start_y: int, fuel: int, lives: int) -> Spaceship:
        with self.canvas:
            Color(1, 1, 1)
            body = Ellipse(pos=(start_x, start_y), size=(dp(40), dp(40)))
            spaceship = Spaceship(body, speed, fuel, lives)
            return spaceship


def init_enemy(self) -> Enemy:
      with self.canvas:
            Color(1, 0, 0)
            body = Ellipse(pos=(500, 500), size=(40, 40))
            enemy = Enemy(body, 0)
            return enemy
      

def enemy_random_move(self) -> tuple[int, int]:
      return (0,0)


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