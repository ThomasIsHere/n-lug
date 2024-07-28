from kivy.uix.screenmanager import Screen

from typing import List

from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy
from .utils_methods import do_not_touch_spaceship

from .game_constants import (
      SPACESHIP_SPEED,
      SPACESHIP_MAX_FUEL_100,
      SPACESHIP_FUEL_DECREASE,
      SPACESHIP_FUEL_INCREASE,
      #SPACESHIP_START_LIVES,
      #SCREEN_HEIGHT,
      #SCREEN_WIDTH,
      FPS
      )


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


def spaceship_moves_to_handler(screen: Screen, go_x: int, go_y: int, speed_corrector_x: float, speed_corrector_y: float, is_moving:bool, dt):
        x, y = screen.spaceship.body.pos

        x_speed = SPACESHIP_SPEED * speed_corrector_x * dt * FPS
        y_speed = SPACESHIP_SPEED * speed_corrector_y * dt * FPS
        
        if do_not_touch_spaceship(screen, screen.dict_destination["go_to_x"], screen.dict_destination["go_to_y"]):
            if x < go_x:
                x += x_speed
            elif x > go_x:
                x -= x_speed
            else:
                x = go_x
            
            if y < go_y:
                y += y_speed
            elif y > go_y:
                y -= y_speed
            else:
                y = go_y

        if screen.spaceship.fuel > 1 and is_moving:
            screen.spaceship.body.pos = (x, y)
            screen.spaceship.fuel -= SPACESHIP_FUEL_DECREASE
        elif screen.spaceship.fuel < SPACESHIP_MAX_FUEL_100 and not is_moving:
            screen.spaceship.fuel += SPACESHIP_FUEL_INCREASE

        screen.fuel_value = screen.spaceship.fuel