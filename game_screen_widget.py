from kivy.metrics import dp
from kivy.properties import Clock, NumericProperty, ObjectProperty
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


from game_utils.game_methods import init_spaceship


class ScreenGame(Screen):
    def __init__(self, **kwargs):
        super(ScreenGame, self).__init__(**kwargs)


class GameWidget(Widget):
    from game_utils.game_player_actions import on_touch_down, on_touch_up, on_touch_move

    dict_destination = None
    spaceship = None
    fuel_value = NumericProperty(0)

    SPACESHIP_SPEED = dp(100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spaceship = init_spaceship(self, self.SPACESHIP_SPEED, 400, 400, 100.0, 3)
        self.dict_destination = {
                                "go_to_x": 400, 
                                "go_to_y": 400, 
                                "speed_corrector_x": 1.0, 
                                "speed_corrector_y": 1.0,
                                "is_moving": False
                                }
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

    def spaceship_moves_to(self, go_x: int, go_y: int, speed_corrector_x: float, speed_corrector_y: float, is_moving:bool, dt):
        x, y = self.spaceship.body.pos

        x_speed = dp(10) * speed_corrector_x * dt * 60
        y_speed = dp(10) * speed_corrector_y * dt * 60

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
            self.spaceship.fuel -=1
        elif self.spaceship.fuel < 100 and not is_moving:
            self.spaceship.fuel +=.5

        self.fuel_value = self.spaceship.fuel