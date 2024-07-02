from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp


from .game_objects import Spaceship, Enemy


def init_spaceship(self, speed: int) -> Spaceship:
        with self.canvas:
            Color(1, 1, 1)
            body = Rectangle(pos=(400, 400), size=(dp(40), dp(40)))
            spaceship = Spaceship(body, speed)
        return spaceship


def is_collision() -> bool:
      return False


def distance_spaceship_with_enemy(s: Spaceship, e: Enemy) -> int:
      return None