from kivy.graphics.vertex_instructions import Ellipse

from random import randint
from typing import List
from math import sqrt, pow

from game_utils.game_constants import (
      SCREEN_HEIGHT,
      SCREEN_WIDTH
      )


class GameObjet:
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet']):
        self.body = body
        self.listOverlap = listOverlap

    def generate_random_pos(self)  -> tuple[int, int]:
        w, h = self.body.size
        x = randint(0, SCREEN_WIDTH - int(w))
        y = randint(0, SCREEN_HEIGHT - int(h))
        return (x, y)
    
    def move(self, speed_x, speed_y):
        x, y = self.body.pos
        x += speed_x
        y += speed_y
        self.body.pos = (x, y)
    
    def collied_with(self, other_go) -> bool:
      x1, y1 = self.body.pos
      w1, h1 = self.body.size
      x2, y2 = other_go.body.pos
      w2, h2 = other_go.body.size

      self_left = False
      self_down = False

      if x1 < x2:
            self_left = True

      if y1 < y2:
            self_down = True

      diameter_sub = 0.0

      if self_left and self_down:
            diameter_sub = w1
      elif not self_left and self_down:
            diameter_sub = w1
      elif not self_left and not self_down:
            diameter_sub = w2
      elif self_left and not self_down:
            diameter_sub = w2

      d = self.__distance_2_points(x1, y1, x2, y2) - diameter_sub
      if d < 0:
            return True
      else:
            return False


    def __distance_2_points(self, x1, y1, x2, y2) -> float:
        return sqrt(pow(x1-x2,2) + pow(y1-y2,2))