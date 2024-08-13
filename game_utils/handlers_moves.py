from kivy.uix.screenmanager import Screen

from .game_objects.go_asteroid import AsteroidState
from .utils_methods import do_not_touch_spaceship

from .game_constants import (
      SPACESHIP_MAX_FUEL_100,
      SPACESHIP_FUEL_DECREASE,
      SPACESHIP_FUEL_INCREASE,
      FPS,
      ASTEROID_SPEED,
      ASTEROID_SPEED_PROJECTILE
      )


def enemies_random_move_handler(screen: Screen):
    le = screen.enemies
    for e in le:
        e.enemy_random_move(screen)


def spaceship_moves_to_handler(screen: Screen, dt):
        go_x = screen.dict_destination["go_to_x"]
        go_y = screen.dict_destination["go_to_y"]
        speed_corrector_x = screen.dict_destination["speed_corrector_x"]
        speed_corrector_y = screen.dict_destination["speed_corrector_y"]
        is_moving = screen.dict_destination["is_moving"]

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


def asteroids_moves_handler(screen: Screen, dt: int):
    list_a = screen.asteroids
    for a in list_a:
        if a.state == AsteroidState.FOLLOW:
            xs, ys = screen.spaceship.body.pos
            a.speed_x = ASTEROID_SPEED
            a.speed_y = ASTEROID_SPEED
            a.moves_to_target(xs, ys, dt)
        elif a.state == AsteroidState.PROJECTILE:
            a.speed_x = ASTEROID_SPEED_PROJECTILE
            a.speed_y = ASTEROID_SPEED_PROJECTILE
            a.moves_to_target(a.projectile_target_x, a.projectile_target_y, dt)
        elif a.state == AsteroidState.RANDOM:
            a.random_move(screen)