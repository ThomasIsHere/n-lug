from kivy.properties import Clock, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

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
    immortal_png_handler,
    immortal_timer_handler,
    num_asteroids_handler,
    num_enemies_handler,
    asteroids_state_handler,
    asteroids_png_handler
    )
from game_utils.handlers_moves import (
    enemies_random_move_handler,
    spaceship_moves_to_handler,
    asteroids_moves_handler
    )
from game_utils.game_constants import (
      SPACESHIP_SPEED,
      SPACESHIP_MAX_FUEL_100,
      SPACESHIP_START_LIVES,
      FPS,
      ASTEROID_WAITING_COUNT,
      ENEMY_WAITING_COUNT
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
    game_level_label = StringProperty("")
    game_level = None
    
    wainting_asteroid_counter = 0
    wainting_enemy_counter = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.init_game)

    def init_game(self, *args):
        ws = self.width
        hs = self.height
        self.game_level = 1
        self.spaceship = init_spaceship(
                self,
                SPACESHIP_SPEED,
                ws / 2,
                hs / 2,
                SPACESHIP_MAX_FUEL_100,
                SPACESHIP_START_LIVES,
                0
            )
        self.asteroids = init_asteroids(self, self.game_level * 2)
        self.enemies = init_enemies(self, self.game_level * 3)
        self.dict_destination = {
                                "go_to_x": ws / 2, 
                                "go_to_y": hs / 2, 
                                "speed_corrector_x": 0.0, 
                                "speed_corrector_y": 0.0,
                                "is_moving": False
                                }
        self.lives_remaining = str(self.spaceship.lives)
        self.game_level_label = str(self.game_level)
        self.wainting_asteroid_counter = ASTEROID_WAITING_COUNT
        self.wainting_enemy_counter = ENEMY_WAITING_COUNT
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
        immortal_png_handler(self)
        immortal_timer_handler(self)
        num_asteroids_handler(self)
        num_enemies_handler(self)
        asteroids_state_handler(self)
        asteroids_png_handler(self)