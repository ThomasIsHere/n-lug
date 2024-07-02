from kivy.config import Config
Config.set('graphics', 'width', '1299')
Config.set('graphics', 'height', '540')


from kivy.uix.widget import Widget
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import Clock
from kivy.core.window import Window
from kivy import platform
from kivy.metrics import dp


from game_utils.game_methods import init_spaceship
from game_utils.game_objects import Spaceship


class MainWidget(Widget):
    from game_utils.game_player_actions import on_key_down, on_key_up, on_touch_down, on_touch_up, on_touch_move

    #keys_pressed = None
    dict_destination = None
    spaceship = None

    SPACESHIP_SPEED = dp(250)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spaceship = init_spaceship(self, self.SPACESHIP_SPEED)
        self.dict_destination = {"go_to_x": 400, "go_to_y": 400, "speed_corrector_x": 1.0, "speed_corrector_y": 1.0}
        # if desktop we use the keyboard arrows to control spaceship
        #if self.is_desktop():
            #self.keys_pressed = set()
            #self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            #self._keyboard.bind(on_key_down=self.on_keyboard_down)
            #self._keyboard.bind(on_key_up=self.on_keyboard_up)
            #Window.bind(on_key_down=self.on_key_down)
            #Window.bind(on_key_up=self.on_key_up)
        #else:
            #print("Not a computer")
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    #  'win', 'linux', 'android', 'macosx', 'ios' or 'unknown'
    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    def update(self, dt):
        self.spaceship_moves_to(
            self.dict_destination["go_to_x"],
            self.dict_destination["go_to_y"],
            self.dict_destination["speed_corrector_x"],
            self.dict_destination["speed_corrector_y"],
            dt
            )

    def spaceship_moves_to(self, go_x: int, go_y: int, speed_corrector_x: float, speed_corrector_y: float, dt):
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

        self.spaceship.body.pos = (x, y)


class NlugApp(App):
    pass


if __name__ == "__main__":
    NlugApp().run()
