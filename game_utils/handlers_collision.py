from kivy.uix.screenmanager import Screen

from typing import List

from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy

from .game_constants import FPS

from .game_methods import spaceship_stops


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
            spaceship.lives -=1
            screen.lives_remaining = str(spaceship.lives)
            screen.spaceship.timer_immortal = 4 * FPS # 4 * FPS fps


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