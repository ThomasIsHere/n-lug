from kivy.graphics.vertex_instructions import Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.screenmanager import Screen
from random import randint, choice

from typing import List

from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy
from .game_objects.go_asteroid import Asteroid, AsteroidState
from .game_constants import (
      SPACESHIP_HEIGHT,
      SPACESHIP_WIDTH,
      SCREEN_HEIGHT,
      SCREEN_WIDTH,
      ENEMY_WIDTH,
      ENEMY_HEIGHT,
      ENEMY_MAX_SPEED,
      ASTEROID_WIDTH,
      ASTEROID_HEIGHT,
      ASTEROID_SPEED
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
                  pos=__enmy_random_init_pos_away_spaceship(screen),
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


def __enmy_random_init_pos_away_spaceship(screen: Screen) -> tuple[int, int]:
      x = randint(0, SCREEN_WIDTH - int(ENEMY_WIDTH))
      y = randint(0, SCREEN_HEIGHT - int(ENEMY_HEIGHT))
      spaceship_x, spaceship_y = screen.spaceship.body.pos
      d = distance_2_points(x, x, spaceship_x, spaceship_y)
      # enemy pops at least 4 times the distance of spaceship width
      if d > 4 * SPACESHIP_WIDTH:
            return (x, y)
      return __enmy_random_init_pos_away_spaceship(screen)
      

def init_enemies(screen: Screen, num: int) -> List[Enemy]:
      list_enemies = []
      while(num > 0):
            list_enemies.append(__init_enemy(screen))
            num-=1
      return list_enemies


def init_asteroids(screen: Screen, num: int) -> List[Asteroid]:
      list_asteroids = []
      dict_asteroids_colors = {}
      while(num > 0):
            asteroid, asteroid_canvas_color = __init_asteroid(screen)
            list_asteroids.append(asteroid)
            dict_asteroids_colors[asteroid] = asteroid_canvas_color
            num-=1
      return list_asteroids, dict_asteroids_colors


def __init_asteroid(screen: Screen) -> tuple[Asteroid, object]:
      start_x, start_y = __random_asteroid_position(screen)
      with screen.canvas:
            screen.asteroid_canvas_color = Color(1, .6, .1) 
            body = Ellipse(pos=(start_x, start_y),size=(ASTEROID_WIDTH, ASTEROID_HEIGHT))
            asteroid = Asteroid(
                  body,
                  [],
                  AsteroidState.RANDOM,
                  randint(0, ASTEROID_SPEED),
                  randint(0, ASTEROID_SPEED),
                  choice([True, False]),
                  choice([True, False])
            )
            return asteroid, screen.asteroid_canvas_color


def __random_asteroid_position(screen: Screen) -> tuple[int, int]:
      x = randint(0, SCREEN_WIDTH - int(ASTEROID_WIDTH))
      y = randint(0, SCREEN_HEIGHT - int(ASTEROID_HEIGHT))
      spaceship_x, spaceship_y = screen.spaceship.body.pos
      d = distance_2_points(x, x, spaceship_x, spaceship_y)
      # enemy pops at least 4 times the distance of spaceship width
      if d > 20 * SPACESHIP_WIDTH:
            return (x, y)
      return __random_asteroid_position(screen)