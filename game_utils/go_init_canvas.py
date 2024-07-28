from kivy.graphics.vertex_instructions import Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.screenmanager import Screen
from random import randint, choice

from typing import List

from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy
from .game_constants import (
      SPACESHIP_HEIGHT,
      SPACESHIP_WIDTH,
      SCREEN_HEIGHT,
      SCREEN_WIDTH,
      ENEMY_WIDTH,
      ENEMY_HEIGHT,
      ENEMY_MAX_SPEED
      )
from .utils_methods import distance_2_points


def init_spaceship(
            screen: Screen,
            speed: int, 
            start_x: int, 
            start_y: int, 
            fuel: int,
            lives: int,
            timer_immortal: int
            ) -> Spaceship:
        with screen.canvas:
            screen.spaceship_canvas_color = Color(1, 1, 1) # white
            body = Ellipse(
                        pos=(start_x, start_y),
                        size=(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                  )
            spaceship = Spaceship(body, [], speed, fuel, lives, timer_immortal)
            return spaceship


def __init_enemy(screen: Screen) -> Enemy:
      with screen.canvas:
            Color(1, 0, 0) # red
            body = Ellipse(
                  pos=__return_enemy_random_init_pos(screen),
                  size=(ENEMY_WIDTH, ENEMY_HEIGHT),
                  )
            enemy = Enemy(
                  body,
                  [],
                  randint(1, ENEMY_MAX_SPEED),
                  randint(1, ENEMY_MAX_SPEED),
                  choice([True, False]),
                  choice([True, False])
                  )
            return enemy


def __return_enemy_random_init_pos(screen: Screen) -> tuple[int, int]:
      enemy_x = randint(0, SCREEN_WIDTH - int(ENEMY_WIDTH))
      enemy_y = randint(0, SCREEN_HEIGHT - int(ENEMY_HEIGHT))
      spaceship_x, spaceship_y = screen.spaceship.body.pos
      d = distance_2_points(enemy_x, enemy_y, spaceship_x, spaceship_y)
      # enemy pops at least 4 times the distance of spaceship width
      if d > 4 * SPACESHIP_WIDTH:
            return (enemy_x, enemy_y)
      return __return_enemy_random_init_pos(screen)
      

def init_enemies(screen: Screen, num: int) -> List[Enemy]:
      list_enemies = []
      while(num > 0):
            list_enemies.append(__init_enemy(screen))
            num-=1
      return list_enemies