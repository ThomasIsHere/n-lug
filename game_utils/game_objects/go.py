from kivy.graphics.vertex_instructions import Ellipse

from random import randint
from typing import List

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