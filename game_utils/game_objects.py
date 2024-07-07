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
    def __init__(self, body: Ellipse, speed: int):
        self.body = body
        self.speed = speed
