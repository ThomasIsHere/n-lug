from kivy.uix.screenmanager import Screen
#from kivy.clock import Clock

from .go_init_canvas import init_asteroid
from .game_constants import ASTEROID_WAITING_COUNT

def immortal_color_handler(screen: Screen):
    s = screen.spaceship
    if s.timer_immortal <= 0:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, 1) # white
    else:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, .4) # white 60% transparent


def immortal_timer_handler(screen: Screen):
    if screen.spaceship.timer_immortal > 0:
        screen.spaceship.timer_immortal -=1


def num_asteroid_handler(screen: Screen):
    if len(screen.asteroids) <=0:
        screen.wainting_counter -= 1
        if screen.wainting_counter <= 0:
            screen.asteroids.append(init_asteroid(screen))
            screen.wainting_counter = ASTEROID_WAITING_COUNT