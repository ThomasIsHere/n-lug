from kivy.graphics import Ellipse

from typing import List

from .go import GameObjet


class Spaceship(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], speed: int, fuel: float, lives: int, timer_immortal: int):
        GameObjet.__init__(self, body, listOverlap)
        self.speed = speed
        self.fuel = fuel
        self.lives = lives
        self.timer_immortal = timer_immortal