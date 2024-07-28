from kivy.uix.screenmanager import Screen

from .game_objects.go_spaceship import Spaceship


def immortal_color_handler(screen: Screen, spaceship: Spaceship):
    if spaceship.timer_immortal <= 0:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, 1) # white
    else:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, .4) # white 60% transparent