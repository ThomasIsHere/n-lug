#from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics import Rectangle, Rotate
from kivy.uix.screenmanager import Screen
from random import randint, choice

from typing import List

from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy
from .game_objects.go_asteroid import Asteroid, AsteroidState
from .game_constants import (
      SPACESHIP_HEIGHT,
      SPACESHIP_WIDTH,
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
            body = Rectangle(
                        source = 'assets/spaceship.png',
                        pos=(start_x, start_y),
                        size=(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                  )
            spaceship = Spaceship(body, [], speed, fuel, lives, timer_immortal)
            return spaceship


def __init_enemy(screen: Screen) -> Enemy:
      with screen.canvas:
            body = Rectangle(
                  source = 'assets/enemy.png',
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
      ws, hs = screen.size
      x = randint(0, ws - int(ENEMY_WIDTH))
      y = randint(0, hs - int(ENEMY_HEIGHT))
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
      while(num > 0):
            asteroid = __init_asteroid(screen)
            list_asteroids.append(asteroid)
            num-=1
      return list_asteroids


def __init_asteroid(screen: Screen) -> tuple[Asteroid]:
      start_x, start_y = __random_asteroid_position(screen)
      with screen.canvas:
            body = Rectangle(
                  source = 'assets/asteroid.png',
                  pos=(start_x, start_y)
                  ,size=(ASTEROID_WIDTH, ASTEROID_HEIGHT)
                  )
            asteroid = Asteroid(
                  body,
                  [],
                  AsteroidState.RANDOM,
                  randint(1, ASTEROID_SPEED),
                  randint(1, ASTEROID_SPEED),
                  choice([True, False]),
                  choice([True, False]),
                  None,
                  None
            )
            return asteroid


def __random_asteroid_position(screen: Screen) -> tuple[int, int]:
      ws, hs = screen.size
      x = randint(0, ws - int(ASTEROID_WIDTH))
      y = randint(0, hs - int(ASTEROID_HEIGHT))
      spaceship_x, spaceship_y = screen.spaceship.body.pos
      d = distance_2_points(x, x, spaceship_x, spaceship_y)
      if d > 7 * SPACESHIP_WIDTH:
            return (x, y)
      return __random_asteroid_position(screen)