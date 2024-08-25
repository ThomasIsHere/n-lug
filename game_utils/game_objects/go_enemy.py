from kivy.graphics import Ellipse
from kivy.uix.screenmanager import Screen

from typing import List
from random import randint

from .go import GameObjet

from ..game_constants import (
      ENEMY_MAX_SPEED
      )

class Enemy(GameObjet):
    def __init__(
                  self, 
                  body: Ellipse, 
                  listOverlap: List['GameObjet'], 
                  speed_x: int, 
                  speed_y: int, 
                  right: bool, 
                  up: bool
                  ):
        GameObjet.__init__(self, body, listOverlap)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.right = right
        self.up = up

    def enemy_change_direction(self):
        self.up = not self.up
        self.right = not self.right


    def enemy_random_move(self, s: Screen):
        x, y = self.body.pos
        w, h = self.body.size

        if x + w <= s.width and self.right:
                x+=self.speed_x
        elif x >= 0 and not self.right:
                x-=self.speed_x

        if x + w > s.width and self.right:
                self.right = False
                self.speed_x = randint(1, ENEMY_MAX_SPEED)
        elif x < 0 and not self.right:
                self.right = True
                self.speed_x = randint(1, ENEMY_MAX_SPEED)
        
        if y + h <= s.height and self.up:
                y+=self.speed_y
        elif y >= 0 and not self.up:
                y-=self.speed_y

        if y + h > s.height and self.up:
                self.up = False
                self.speed_y = randint(1, ENEMY_MAX_SPEED)
        elif y < 0 and not self.up:
                self.up = True
                self.speed_y = randint(1, ENEMY_MAX_SPEED)

        self.body.pos = (x, y)