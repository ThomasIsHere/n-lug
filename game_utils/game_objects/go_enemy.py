from kivy.graphics.vertex_instructions import Ellipse

from typing import List

from .go import GameObjet

class Enemy(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], speed_x: int, speed_y: int, right: bool, up: bool):
        GameObjet.__init__(self, body, listOverlap)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.right = right
        self.up = up