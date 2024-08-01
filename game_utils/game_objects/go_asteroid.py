from kivy.graphics.vertex_instructions import Ellipse

#from random import randint
from typing import List

from .go import GameObjet
from .go_spaceship import Spaceship

from game_utils.utils_methods import speed_corrector, distance_2_points

from game_utils.game_constants import FPS, ASTEROID_NUMBER_WIDTH_PROJECTILE


class Asteroid(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], gravitational_field: Ellipse, speed: int, projectile: bool):
        GameObjet.__init__(self, body, listOverlap)
        self.gravitational_field = gravitational_field
        self.speed = speed
        self.projectile = projectile


    def transform_to_projectile(self, s: Spaceship):
        w, h = self.body.size
        x1, y1 = self.body.pos
        x2, y2 = s.body.pos
        if distance_2_points(x1, y1, x2, y2) <=  w * ASTEROID_NUMBER_WIDTH_PROJECTILE:
            self.projectile = True

    
    '''def moves_toward_spaceship(self, s: Spaceship, dt: int):
        ax, ay = self.body.pos
        a_speed = self.speed

        target_x, target_y = s.body.pos
        speed_corrector_x, speed_corrector_y = speed_corrector(ax, ay, target_x, target_y)
        
        x_speed = a_speed * speed_corrector_x * dt * FPS
        y_speed = a_speed * speed_corrector_y * dt * FPS

        if ax < target_x:
            ax += x_speed
        elif ax > target_x:
            ax -= x_speed
        else:
            ax = target_x
        
        if ay < target_y:
            ay += y_speed
        elif ay > target_y:
            ay -= y_speed
        else:
            ay = target_y
        
        self.body.pos = ax, ay'''


    def projectile_straight_move(self):
        pass