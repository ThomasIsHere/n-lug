from kivy.uix.screenmanager import Screen

from typing import List

from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy
from .game_objects.go_asteroid import Asteroid

from .game_constants import FPS, SCREEN_WIDTH, SCREEN_HEIGHT

from .utils_methods import spaceship_stops


def __collision_handler_spaceship_enemy(screen: Screen, spaceship: Spaceship, enemy: Enemy):
    if not spaceship.overlap(enemy) and enemy in spaceship.listOverlap:
        spaceship.listOverlap.remove(enemy)
    if spaceship.collied_with(enemy):    
        spaceship_stops(screen)
        if enemy not in spaceship.listOverlap:
            enemy.enemy_change_direction()
        if spaceship.overlap(enemy) and enemy not in spaceship.listOverlap:
            spaceship.listOverlap.append(enemy)
        if spaceship.timer_immortal <= 0:
            __spaceship_lives_handler(screen)


def collision_handler_spaceship_enemies(screen: Screen, spaceship: Spaceship, lenemies: List[Enemy]):
      for e in lenemies:
            __collision_handler_spaceship_enemy(screen, spaceship, e)


def collision_handler_between_enemies(screen: Screen, lenemies: List[Enemy]):
      for e1 in lenemies:
            for e2 in lenemies:
                  if e1 is not e2:
                        if not e1.overlap(e2) and e2 in e1.listOverlap:
                              e1.listOverlap.remove(e2)
                        if e1.collied_with(e2):
                              if e2 not in e1.listOverlap:
                                    e1.enemy_change_direction()
                              if e1.overlap(e2) and e2 not in e1.listOverlap:
                                    e1.listOverlap.append(e2)


def collision_handler_asteroids(screen: Screen):
      for a in screen.asteroids:
            __collision_handler_asteroid_with_spaceship(a, screen)
            __collision_handler_asteroid_with_enemies(a, screen)
            __collision_handler_asteroid_with_screen_borders(a, screen)
     

def __collision_handler_asteroid_with_spaceship(a: Asteroid, screen: Screen):
      s = screen.spaceship
      if a.projectile and a.collied_with(s) and s.timer_immortal <= 0:
            __spaceship_lives_handler(screen)
            screen.canvas.remove(a.body)
            screen.asteroids.remove(a)
     

def __spaceship_lives_handler(screen: Screen):
      screen.spaceship.lives -=1
      screen.lives_remaining = str(screen.spaceship.lives)
      screen.spaceship.timer_immortal = 4 * FPS # 4 * FPS fps


def __collision_handler_asteroid_with_enemies(a: Asteroid, screen: Screen):
      list_e = screen.enemies
      for e in list_e:
            if a.projectile and a.collied_with(e):
                  screen.canvas.remove(a.body)
                  screen.asteroids.remove(a)
                  screen.canvas.remove(e.body)
                  screen.enemies.remove(e)


def __collision_handler_asteroid_with_screen_borders(a: Asteroid, screen: Screen):
      x,y = a.body.pos
      w, h = a.body.size
      if (
            x <= 0 
            or x >= SCREEN_WIDTH - w 
            or y <= 0 
            or y >= SCREEN_HEIGHT - h
            ):
            screen.canvas.remove(a.body)
            screen.asteroids.remove(a)