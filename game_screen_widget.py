from kivy.metrics import dp
from kivy.properties import Clock, NumericProperty, ObjectProperty, StringProperty
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from typing import List

from game_utils.game_objects import Enemy
from game_utils.game_methods import (
    init_spaceship,
    enemy_random_move,
    init_enemies,
    collision_handler_spaceship_enemies,
    collision_handler_between_enemies
    )



class ScreenGame(Screen):
    def __init__(self, **kwargs):
        super(ScreenGame, self).__init__(**kwargs)



class GameWidget(Widget):
    from game_utils.game_player_actions import on_touch_down, on_touch_up, on_touch_move

    dict_destination = None
    spaceship = None
    enemies = None
    fuel_value = NumericProperty(0)
    lives_remaining = StringProperty("")

    SPACESHIP_SPEED = dp(100)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spaceship = init_spaceship(self, self.SPACESHIP_SPEED, 400, 400, 100.0, 3, 0)
        self.enemies = init_enemies(self, 10)
        self.dict_destination = {
                                "go_to_x": 400, 
                                "go_to_y": 400, 
                                "speed_corrector_x": 1.0, 
                                "speed_corrector_y": 1.0,
                                "is_moving": False
                                }
        self.lives_remaining = str(self.spaceship.lives)
        Clock.schedule_interval(self.update, 1.0 / 60.0)


    #  'win', 'linux', 'android', 'macosx', 'ios' or 'unknown'
    '''def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False'''


    def update(self, dt):
        self.spaceship_moves_to(
            self.dict_destination["go_to_x"],
            self.dict_destination["go_to_y"],
            self.dict_destination["speed_corrector_x"],
            self.dict_destination["speed_corrector_y"],
            self.dict_destination["is_moving"],
            dt
            )
        collision_handler_spaceship_enemies(self, self.spaceship, self.enemies)
        collision_handler_between_enemies(self, self.enemies)
        self.immortal_timer_handler()
        self.enemies_random_move_handler(self.enemies)


    def spaceship_moves_to(self, go_x: int, go_y: int, speed_corrector_x: float, speed_corrector_y: float, is_moving:bool, dt):
        x, y = self.spaceship.body.pos

        x_speed = 30 * speed_corrector_x * dt * 60
        y_speed = 30 * speed_corrector_y * dt * 60

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

        if self.spaceship.fuel > 1 and is_moving:
            self.spaceship.body.pos = (x, y)
            self.spaceship.fuel -=.7
        elif self.spaceship.fuel < 100 and not is_moving:
            self.spaceship.fuel +=.5

        self.fuel_value = self.spaceship.fuel


    def immortal_timer_handler(self):
        if self.spaceship.timer_immortal > 0:
            self.spaceship.timer_immortal -=1


    def enemies_random_move_handler(self, le: List[Enemy]):
        for e in le:
            enemy_random_move(self, e)