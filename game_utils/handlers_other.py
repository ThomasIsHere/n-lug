from kivy.uix.screenmanager import Screen

from .go_init_canvas import init_asteroids, init_enemies
from .game_constants import ASTEROID_WAITING_COUNT, ENEMY_WAITING_COUNT
from game_utils.utils_methods import distance_2_points
from .game_objects.go_asteroid import AsteroidState

def immortal_color_handler(screen: Screen):
    s = screen.spaceship
    if s.timer_immortal <= 0:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, 1) # white
    else:
        screen.spaceship_canvas_color.rgba = (1, 1, 1, .4) # white 60% transparent


def immortal_timer_handler(screen: Screen):
    if screen.spaceship.timer_immortal > 0:
        screen.spaceship.timer_immortal -=1


def num_asteroids_handler(screen: Screen):
    if len(screen.asteroids) <=0:
        screen.wainting_asteroid_counter -= 1
        if screen.wainting_asteroid_counter <= 0:
            num = screen.game_level * 2
            screen.asteroids, screen.asteroids_canvas_color = init_asteroids(screen, num)
            screen.wainting_asteroid_counter = ASTEROID_WAITING_COUNT


def num_enemies_handler(screen: Screen):
    if len(screen.enemies) <=0:
        screen.wainting_enemy_counter -= 1
        if screen.wainting_enemy_counter <= 0:
            __game_level_icrement_handler(screen)
            num = screen.game_level * 3
            screen.enemies = init_enemies(screen, num)
            screen.wainting_enemy_counter = ENEMY_WAITING_COUNT


def __game_level_icrement_handler(screen: Screen):
      screen.game_level += 1
      screen.game_level_label = str(screen.game_level)


def asteroids_state_handler(screen: Screen):
    x2, y2 = screen.spaceship.body.pos
    w, h = screen.spaceship.body.size
    for a in screen.asteroids:
        x1, y1 = a.body.pos
        if (a.state == AsteroidState.RANDOM 
            and distance_2_points(x1, y1, x2, y2) <=  w * 6): # replace 6 with constant
            a.state = AsteroidState.FOLLOW
            screen.asteroids_canvas_color[a].rgba = (1, .8, .4, 1)
        elif (a.state == AsteroidState.FOLLOW
              and distance_2_points(x1, y1, x2, y2) <= w * 3): # replace 3 with constant
            a.state = AsteroidState.PROJECTILE
            screen.asteroids_canvas_color[a].rgba = (1, 1, 0, 1)