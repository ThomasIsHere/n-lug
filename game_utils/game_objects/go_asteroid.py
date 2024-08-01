from kivy.graphics.vertex_instructions import Ellipse

#from random import randint
from typing import List

from .go import GameObjet
from .go_spaceship import Spaceship

from game_utils.utils_methods import a_b_function, distance_2_points

from game_utils.game_constants import ASTEROID_NUMBER_WIDTH_PROJECTILE, SCREEN_WIDTH


class Asteroid(GameObjet):
    def __init__(
            self, 
            body: Ellipse, 
            listOverlap: List['GameObjet'], 
            gravitational_field: Ellipse, 
            speed: int, 
            projectile: bool, 
            projectile_target: tuple[float, float]
            ):
        GameObjet.__init__(self, body, listOverlap)
        self.gravitational_field = gravitational_field
        self.speed = speed
        self.projectile = projectile
        self.projectile_target = projectile_target


    def transform_to_projectile(self, s: Spaceship):
        w, h = self.body.size
        x1, y1 = self.body.pos
        x2, y2 = s.body.pos
        if distance_2_points(x1, y1, x2, y2) <=  w * ASTEROID_NUMBER_WIDTH_PROJECTILE:
            self.projectile = True


    # to be call before transform_to_projectile
    def projectile_straight_target(self, s: Spaceship):
        if not self.projectile:
            x1, y1 = self.body.pos
            x2, y2 = s.body.pos
            a, b = a_b_function(x1, y1, x2, y2)
            if x1 < x2: # direction right
                target_x = SCREEN_WIDTH
            else: # direction left
                target_x = 0
            target_y = a * target_x + b
            self.projectile_target = target_x, target_y