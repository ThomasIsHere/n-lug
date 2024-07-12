from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from typing import List, Tuple


class GameObjet:
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet']):
        self.body = body
        self.listOverlap = listOverlap


class Spaceship(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], speed: int, fuel: float, lives: int, timer_immortal: int):
        GameObjet.__init__(self, body, listOverlap)
        self.speed = speed
        self.fuel = fuel
        self.lives = lives
        self.timer_immortal = timer_immortal


class Enemy(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], speed_x: int, speed_y: int, right: bool, up: bool):
        GameObjet.__init__(self, body, listOverlap)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.right = right
        self.up = up