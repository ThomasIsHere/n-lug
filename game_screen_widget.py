from kivy.properties import Clock, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from typing import List

from game_utils.game_objects.go_asteroid import Asteroid
from game_utils.game_objects.go_enemy import Enemy
from game_utils.game_methods import (
    init_spaceship,
    enemy_random_move,
    init_enemies,
    do_not_touch_spaceship
    )
from game_utils.collision_handlers import (
    collision_handler_spaceship_enemies,
    collision_handler_between_enemies,
    immortal_color_handler
    )
from game_utils.game_constants import (
      SPACESHIP_SPEED,
      SPACESHIP_MAX_FUEL_100,
      SPACESHIP_FUEL_DECREASE,
      SPACESHIP_FUEL_INCREASE,
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
    fuel_value = NumericProperty(0)
    lives_remaining = StringProperty("")
    spaceship_canvas_color = None
    a = None


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Asteroid(None, None, None)
        self.a.init_asteroid_canvas(self)
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
        self.a.move(1, 1)
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
        immortal_color_handler(self, self.spaceship)
        self.immortal_timer_handler()
        self.enemies_random_move_handler(self.enemies)


    def spaceship_moves_to(self, go_x: int, go_y: int, speed_corrector_x: float, speed_corrector_y: float, is_moving:bool, dt):
        x, y = self.spaceship.body.pos

        x_speed = SPACESHIP_SPEED * speed_corrector_x * dt * FPS
        y_speed = SPACESHIP_SPEED * speed_corrector_y * dt * FPS
        
        if do_not_touch_spaceship(self, self.dict_destination["go_to_x"], self.dict_destination["go_to_y"]):
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
            self.spaceship.fuel -= SPACESHIP_FUEL_DECREASE
        elif self.spaceship.fuel < SPACESHIP_MAX_FUEL_100 and not is_moving:
            self.spaceship.fuel += SPACESHIP_FUEL_INCREASE

        self.fuel_value = self.spaceship.fuel


    def immortal_timer_handler(self):
        if self.spaceship.timer_immortal > 0:
            self.spaceship.timer_immortal -=1


    def enemies_random_move_handler(self, le: List[Enemy]):
        for e in le:
            enemy_random_move(self, e)