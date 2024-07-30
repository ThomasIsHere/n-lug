from kivy.graphics.vertex_instructions import Ellipse, Line
from kivy.graphics.context_instructions import Color

#from random import randint
from typing import List

'''from game_utils.game_constants import (
      SCREEN_HEIGHT,
      SCREEN_WIDTH,
      ASTEROID_WIDTH,
      ASTEROID_HEIGHT
      )'''

from .go import GameObjet

class Asteroid(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], gravitational_field: Ellipse, speed: int, projectile: bool):
        GameObjet.__init__(self, body, listOverlap)
        self.gravitational_field = gravitational_field
        self.speed = speed
        self.projectile = projectile

    '''def init_asteroid_canvas(self, widget):
        start_x = randint(0, SCREEN_WIDTH - int(ASTEROID_WIDTH))
        start_y = randint(0, SCREEN_HEIGHT - int(ASTEROID_HEIGHT))
        with widget.canvas:
            Color(.88, .57, .39) # Brown
            self.body = Ellipse(pos=(start_x, start_y),size=(ASTEROID_WIDTH, ASTEROID_HEIGHT))    
            Color(1, 1, 1)
            x, y = self.get_body_center()
            self.gravitational_field = Line(circle=(x, y, 100), width=.3)'''