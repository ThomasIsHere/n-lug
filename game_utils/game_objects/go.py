from kivy.graphics import Ellipse
from kivy.uix.screenmanager import Screen

from random import randint
from typing import List

from game_utils.utils_methods import distance_2_points, point_in_range


class GameObjet:
      def __init__(self, body: Ellipse, listOverlap: List['GameObjet']):
            self.body = body
            self.listOverlap = listOverlap


      def generate_random_pos(self, screen: Screen)  -> tuple[int, int]:
            w, h = self.body.size
            ws, hs = screen.size
            x = randint(0, ws - int(w))
            y = randint(0, hs - int(h))
            return (x, y)


      def move(self, speed_x, speed_y):
            x, y = self.body.pos
            x += speed_x
            y += speed_y
            self.body.pos = (x, y)


      def collied_with(self, other_go: 'GameObjet') -> bool:
            x1, y1 = self.body.pos
            w1, h1 = self.body.size
            x2, y2 = other_go.body.pos
            w2, h2 = other_go.body.size

            self_left = False
            self_down = False

            if x1 < x2:
                  self_left = True

            if y1 < y2:
                  self_down = True

            diameter_sub = 0.0

            if self_left and self_down:
                  diameter_sub = w1
            elif not self_left and self_down:
                  diameter_sub = w1
            elif not self_left and not self_down:
                  diameter_sub = w2
            elif self_left and not self_down:
                  diameter_sub = w2

            d = distance_2_points(x1, y1, x2, y2) - diameter_sub
            if d < 0:
                  return True
            else:
                  return False


      def overlap(self, other_go: 'GameObjet') -> bool:
            x1, y1 = self.body.pos
            w1, h1 = self.body.size
            x2, y2 = other_go.body.pos
            w2, h2 = other_go.body.size

            x_overlap = False
            y_overlap = False
            overlap = False

            if (
                  point_in_range(x1, x2, x2 + w2) 
                  or point_in_range(x1 + w1, x2, x2 + w2)
                  or point_in_range(x2, x1, x1 + w1)
                  or point_in_range(x2 + w2, x1, x1 + w1)
                  ):
                  x_overlap = True

            if (
                  point_in_range(y1, y2, y2 + h2) 
                  or point_in_range(y1 + h1, y2, y2 + h2)
                  or point_in_range(y2, y1, y1 + h1) 
                  or point_in_range(y2 + h2, y1, y1 + h1)
                  ):
                  y_overlap = True

            if x_overlap and y_overlap:
                  overlap = True
            
            return overlap

        
      def get_body_center(self) -> tuple[int, int]:
            x, y = self.body.pos
            w, h = self.body.size
            x_center = x + w /2
            y_center = y + h /2
            return (x_center, y_center)