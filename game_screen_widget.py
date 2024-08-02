from kivy.properties import Clock, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from typing import List

from game_utils.game_objects.go_asteroid import Asteroid
from game_utils.game_objects.go_enemy import Enemy
from game_utils.game_objects.go_spaceship import Spaceship

from game_utils.go_init_canvas import (
    init_spaceship,
    init_enemies,
    init_asteroids
    )
from game_utils.handlers_collision import (
    collision_handler_spaceship_enemies,
    collision_handler_between_enemies,
    collision_handler_asteroids
    )
from game_utils.handlers_other import (
    immortal_color_handler,
    immortal_timer_handler
    )
from game_utils.handlers_moves import (
    enemies_random_move_handler,
    spaceship_moves_to_handler,
    asteroids_moves_handler,
    )
from game_utils.game_constants import (
      SPACESHIP_SPEED,
      SPACESHIP_MAX_FUEL_100,
      SPACESHIP_START_LIVES,
      SCREEN_HEIGHT,
      SCREEN_WIDTH,
      FPS
      )



class ScreenGame(Screen):
    def __init__(self, **kwargs):
        super(ScreenGame, self).__init__(**kwargs)



class GameWidget(Widget):
    from game_utils.game_player_actions import on_touch_down, on_touch_up, on_touch_move

    dict_destination = None
    spaceship = None
    enemies = None
    asteroids = None
    fuel_value = NumericProperty(0)
    lives_remaining = StringProperty("")
    spaceship_canvas_color = None


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.asteroids = init_asteroids(self, 2)
        self.spaceship = init_spaceship(
                self,
                SPACESHIP_SPEED,
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                SPACESHIP_MAX_FUEL_100,
                SPACESHIP_START_LIVES,
                0
            )
        self.enemies = init_enemies(self, 10)
        self.dict_destination = {
                                "go_to_x": SCREEN_WIDTH / 2, 
                                "go_to_y": SCREEN_HEIGHT / 2, 
                                "speed_corrector_x": 0.0, 
                                "speed_corrector_y": 0.0,
                                "is_moving": False
                                }
        self.lives_remaining = str(self.spaceship.lives)
        Clock.schedule_interval(self.update, 1.0 / FPS)


    #  'win', 'linux', 'android', 'macosx', 'ios' or 'unknown'
    '''def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False'''


    def update(self, dt):
        # Moves
        spaceship_moves_to_handler(self, dt)
        enemies_random_move_handler(self)
        asteroids_moves_handler(self, dt)
        # Collisions
        collision_handler_spaceship_enemies(self)
        collision_handler_between_enemies(self)
        collision_handler_asteroids(self)
        # Others
        immortal_color_handler(self)
        immortal_timer_handler(self)