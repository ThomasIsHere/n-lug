from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class Spaceship:
    def __init__(self, body: Rectangle, speed: int, fuel: float, lives: int):
        self.body = body
        self.speed = speed
        self.fuel = fuel
        self.lives = lives


class Enemy:
    def __init__(self, body: Ellipse, speed: int):
        self.body = body
        self.speed = speed
