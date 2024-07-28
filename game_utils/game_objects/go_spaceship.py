from kivy.graphics.vertex_instructions import Ellipse
from kivy.graphics.context_instructions import Color

from typing import List

from .go import GameObjet

from game_utils.game_constants import (
      SCREEN_HEIGHT,
      SCREEN_WIDTH,
      SPACESHIP_WIDTH,
      SPACESHIP_HEIGHT,
      SPACESHIP_SPEED,
      SPACESHIP_MAX_FUEL_100,
      SPACESHIP_START_LIVES
      )


class Spaceship(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], speed: int, fuel: float, lives: int, timer_immortal: int):
        GameObjet.__init__(self, body, listOverlap)
        self.speed = speed
        self.fuel = fuel
        self.lives = lives
        self.timer_immortal = timer_immortal
    
    def init_spaceship_canvas(self, widget):
        with widget.canvas:
            widget.spaceship_canvas_color = Color(1, 1, 1) # white
            self.body = Ellipse(
                        pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                        size=(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                  )
            self.listOverlap = []
            self.speed = SPACESHIP_SPEED
            self.fuel = SPACESHIP_MAX_FUEL_100
            self.lives = SPACESHIP_START_LIVES
            self.timer_immortal = 0