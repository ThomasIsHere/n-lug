from kivy.graphics.vertex_instructions import Ellipse
from kivy.uix.screenmanager import Screen

from typing import List
from enum import Enum
from random import randint

from .go import GameObjet

from game_utils.utils_methods import speed_corrector

from game_utils.game_constants import (
    ASTEROID_SPEED,
    FPS
    )



class AsteroidState(Enum):
    RANDOM = "RANDOM"
    FOLLOW = "FOLLOW"
    PROJECTILE = "PROJECTILE"



class Asteroid(GameObjet):
    def __init__(
            self, 
            body: Ellipse, 
            listOverlap: List['GameObjet'], 
            state: AsteroidState,
            speed_x: int, 
            speed_y: int, 
            right: bool, 
            up: bool
            ):
        GameObjet.__init__(self, body, listOverlap)

        self.state = state
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.right = right
        self.up = up

    def random_move(self, s: Screen):
        x, y = self.body.pos
        w, h = self.body.size

        if x + w <= s.width and self.right:
                x+=self.speed_x
        elif x >= 0 and not self.right:
                x-=self.speed_x

        if x + w > s.width and self.right:
                self.right = False
                self.speed_x = randint(1, ASTEROID_SPEED)
        elif x < 0 and not self.right:
                self.right = True
                self.speed_x = randint(1, ASTEROID_SPEED)
        
        if y + h <= s.height and self.up:
                y+=self.speed_y
        elif y >= 0 and not self.up:
                y-=self.speed_y

        if y + h > s.height and self.up:
                self.up = False
                self.speed_y = randint(1, ASTEROID_SPEED)
        elif y < 0 and not self.up:
                self.up = True
                self.speed_y = randint(1, ASTEROID_SPEED)

        self.body.pos = (x, y)

    def moves_to_target(self, target_x: float, target_y: float, dt: int):
        go_x, go_y = self.body.pos

        speed_corrector_x, speed_corrector_y = speed_corrector(go_x, go_y, target_x, target_y)
            
        x_speed = self.speed_x * speed_corrector_x * dt * FPS
        y_speed = self.speed_y * speed_corrector_y * dt * FPS

        if go_x < target_x:
                go_x += x_speed
        elif go_x > target_x:
                go_x -= x_speed
        else:
                go_x = target_x
        
        if go_y < target_y:
                go_y += y_speed
        elif go_y > target_y:
                go_y -= y_speed
        else:
                go_y = target_y
        
        self.body.pos = go_x, go_y