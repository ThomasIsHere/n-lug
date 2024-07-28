from kivy.uix.screenmanager import Screen

from typing import List

from .game_objects.go_spaceship import Spaceship
from game_utils.game_objects.go_enemy import Enemy


def immortal_color_handler(screen: Screen, spaceship: Spaceship):
    if spaceship.timer_immortal <= 0:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, 1) # white
    else:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, .4) # white 60% transparent


def immortal_timer_handler(screen: Screen):
    if screen.spaceship.timer_immortal > 0:
        screen.spaceship.timer_immortal -=1


def enemies_random_move_handler(screen: Screen, le: List[Enemy]):
    for e in le:
        e.enemy_random_move(screen)