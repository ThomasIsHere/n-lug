from kivy.uix.screenmanager import ScreenManager
from screen_score import ScreenScore
from screen_welcome import ScreenWelcome
from game_screen_widget import ScreenGame


class NlugScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(NlugScreenManager, self).__init__(**kwargs)
        self.add_widget(ScreenWelcome(name='welcome'))
        self.add_widget(ScreenScore(name='score'))
        self.add_widget(ScreenGame(name='game'))

