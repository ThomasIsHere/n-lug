from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class Spaceship:
    def __init__(self, body: Rectangle, speed: int):
        self.body = body
        self.speed = speed


class Enemy:
    def __init__(self, body: Ellipse, speed: int):
        self.body = body
        self.speed = speed
