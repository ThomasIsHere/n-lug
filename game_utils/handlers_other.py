from kivy.uix.screenmanager import Screen

from typing import List

from .game_objects.go_spaceship import Spaceship
from .game_objects.go_enemy import Enemy
from .utils_methods import do_not_touch_spaceship, speed_corrector, distance_2_points

from .game_constants import (
      #SPACESHIP_SPEED,
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
        spaceship_speed = screen.spaceship.speed

        x_speed = spaceship_speed * speed_corrector_x * dt * FPS
        y_speed = spaceship_speed * speed_corrector_y * dt * FPS
        
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


def asteroid_moves_handler(screen: Screen, dt: int):
    print(screen.asteroid.projectile)
    ax, ay = screen.asteroid.body.pos
    a_speed = screen.asteroid.speed

    #if not screen.asteroid.projectile:
    target_x, target_y = screen.spaceship.body.pos
    speed_corrector_x, speed_corrector_y = speed_corrector(ax, ay, target_x, target_y)
    __projectile_handler(screen, ax, target_x, ay, target_y)
    '''else:
        target_x, target_y = screen.spaceship.body.pos
        speed_corrector_x, speed_corrector_y = speed_corrector(ax, ay, target_x, target_y)'''

    x_speed = a_speed * speed_corrector_x * dt * FPS
    y_speed = a_speed * speed_corrector_y * dt * FPS

    if ax < target_x:
        ax += x_speed
    elif ax > target_x:
        ax -= x_speed
    else:
        ax = target_x
    
    if ay < target_y:
        ay += y_speed
    elif ay > target_y:
        ay -= y_speed
    else:
        ay = target_y
    
    screen.asteroid.body.pos = ax, ay


def __projectile_handler(screen: Screen, x1, x2, y1, y2):
    w, h = screen.asteroid.body.size
    if distance_2_points(x1, y1, x2, y2) <=  2 * w:
        screen.asteroid.projectile = True
