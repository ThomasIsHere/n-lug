from kivy.uix.screenmanager import Screen

from .go_init_canvas import init_asteroids, init_enemies
from .game_constants import ASTEROID_WAITING_COUNT, ENEMY_WAITING_COUNT
from game_utils.utils_methods import distance_2_points, a_b_function, linear_function
from .game_objects.go_asteroid import AsteroidState


def immortal_png_handler(screen: Screen):
    s = screen.spaceship
    if s.timer_immortal <= 0:
        s.body.source = 'assets/spaceship.png'
    else:
        s.body.source = 'assets/spaceship_shield.png'


def immortal_timer_handler(screen: Screen):
    if screen.spaceship.timer_immortal > 0:
        screen.spaceship.timer_immortal -=1


def num_asteroids_handler(screen: Screen):
    if len(screen.asteroids) <=0:
        screen.wainting_asteroid_counter -= 1
        if screen.wainting_asteroid_counter <= 0:
            num = screen.game_level * 2
            screen.asteroids = init_asteroids(screen, num)
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
    xs, ys = screen.spaceship.body.pos
    ws, hs = screen.spaceship.body.size
    for a in screen.asteroids:
        xa, ya = a.body.pos
        if (a.state == AsteroidState.RANDOM 
            and distance_2_points(xa, ya, xs, ys) <=  ws * 6): # replace 6 with constant
            a.state = AsteroidState.FOLLOW
        elif (a.state == AsteroidState.FOLLOW
            and distance_2_points(xa, ya, xs, ys) <= ws * 3): # replace 3 with constant
            a.state = AsteroidState.PROJECTILE
            la, lb = a_b_function(xs, ys, xa, ya)
            if __going_right(xa, xs):
                y_target = linear_function(la, lb, screen.width)
                a.projectile_target_x = screen.width
                a.projectile_target_y = y_target
            else:
                y_target = linear_function(la, lb, 0)
                a.projectile_target_x = 0
                a.projectile_target_y = y_target


def __going_right(x_asteroid: float, x_spaceship: float) -> bool:
    if x_asteroid < x_spaceship:
        return True
    else:
        return False
    

def asteroids_png_handler(screen: Screen):
    list_a = screen.asteroids
    for a in list_a:
        if a.state == AsteroidState.FOLLOW:
            a.body.source = 'assets/asteroid_follow.png'
        elif a.state == AsteroidState.PROJECTILE:
            a.body.source = 'assets/asteroid_missile.png'
        elif a.state == AsteroidState.RANDOM:
            a.body.source = 'assets/asteroid.png'