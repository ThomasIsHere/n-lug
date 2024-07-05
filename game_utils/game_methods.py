from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp


from .game_objects import Spaceship, Enemy


def init_spaceship(self, speed: int, start_x: int, start_y: int, fuel: int, lives: int) -> Spaceship:
        with self.canvas:
            Color(1, 1, 1)
            body = Rectangle(pos=(start_x, start_y), size=(dp(40), dp(40)))
            spaceship = Spaceship(body, speed, fuel, lives)
        return spaceship


def is_collision() -> bool:
      return False


def distance_spaceship_with_enemy(s: Spaceship, e: Enemy) -> int:
      return None