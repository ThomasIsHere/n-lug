from kivy.config import Config
Config.set('graphics', 'width', '1299')
Config.set('graphics', 'height', '540')


from kivy.app import App
from screen_manager import NlugScreenManager


class NlugApp(App):
    def build(self):
        return NlugScreenManager()


if __name__ == "__main__":
    NlugApp().run()
