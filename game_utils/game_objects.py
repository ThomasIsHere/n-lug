from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class GameObjet:
    pass


class Spaceship(GameObjet):
    def __init__(self, body: Ellipse, speed: int, fuel: float, lives: int):
        self.body = body
        self.speed = speed
        self.fuel = fuel
        self.lives = lives


class Enemy(GameObjet):
    def __init__(self, body: Ellipse, speed_x: int, speed_y: int, right: bool, up: bool):
        self.body = body
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.right = right
        self.up = up
