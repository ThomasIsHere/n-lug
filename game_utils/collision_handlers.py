from kivy.uix.screenmanager import Screen

from typing import List

from .game_objects.go import GameObjet
from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy

from .game_constants import FPS

from .game_methods import distance_2_points, spaceship_stops, overlap, enemy_change_direction


def __is_collision(obj1: GameObjet, obj2: GameObjet) -> bool:
      x1, y1 = obj1.body.pos
      w1, h1 = obj1.body.size
      x2, y2 = obj2.body.pos
      w2, h2 = obj2.body.size

      obj1_left = False
      obj1_down = False

      if x1 < x2:
            obj1_left = True

      if y1 < y2:
            obj1_down = True

      diameter_sub = 0.0

      if obj1_left and obj1_down:
            diameter_sub = w1
      elif not obj1_left and obj1_down:
            diameter_sub = w1
      elif not obj1_left and not obj1_down:
            diameter_sub = w2
      elif obj1_left and not obj1_down:
            diameter_sub = w2

      d = distance_2_points(x1, y1, x2, y2) - diameter_sub
      if d < 0:
            return True
      else:
            return False


def __collision_handler_spaceship_enemy(screen: Screen, spaceship: Spaceship, enemy: Enemy):
      if not overlap(spaceship, enemy) and enemy in spaceship.listOverlap:
                  spaceship.listOverlap.remove(enemy)
      if __is_collision(spaceship, enemy):
            spaceship_stops(screen)
            if enemy not in spaceship.listOverlap:
                  enemy_change_direction(enemy)
            if overlap(spaceship, enemy) and enemy not in spaceship.listOverlap:
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
                        if not overlap(e1, e2) and e2 in e1.listOverlap:
                              e1.listOverlap.remove(e2)
                        if __is_collision(e1, e2):
                              if e2 not in e1.listOverlap:
                                    enemy_change_direction(e1)
                              if overlap(e1, e2) and e2 not in e1.listOverlap:
                                    e1.listOverlap.append(e2)


def immortal_color_handler(screen: Screen, spaceship: Spaceship):
      if spaceship.timer_immortal <= 0:
            screen.spaceship_canvas_color.rgba = (1, 1, 1, 1) # white
      else:
            screen.spaceship_canvas_color.rgba = (1, 1, 1, .4) # white 60% transparent