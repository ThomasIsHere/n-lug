from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line
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


class Asteroid(GameObjet):
    def __init__(self, body: Ellipse, listOverlap: List['GameObjet'], gravitational_field: Ellipse):
        GameObjet.__init__(self, body, listOverlap)
        self.gravitational_field = gravitational_field

    def init_asteroid_canvas(self, widget):
        with widget.canvas:
            Color(.88, .57, .39) # Brown
            self.body = Ellipse(pos=(10, 10),size=(30, 30))    
            Color(1, 1, 1)
            x, y = self.__get_center_asteroid()
            self.gravitational_field = Line(circle=(x, y, 100), width=.3)

    def __get_center_asteroid(self) -> tuple[int, int]:
        x, y = self.body.pos
        print(self.body.pos)
        w, h = self.body.size
        x_center = x + w /2
        y_center = y + h /2
        return (x_center, y_center)