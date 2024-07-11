from kivy.metrics import dp
from kivy.clock import Clock

from .game_constants import (
      SPACESHIP_HEIGHT,
      SPACESHIP_WIDTH
      )


def on_touch_move(self, touch):
    update_spaceship_destination(self, touch)


def on_touch_down(self, touch):
    update_spaceship_destination(self, touch)


'''def do_not_touch_spaceship(self, touch) -> bool:
    x, y = self.spaceship.body.pos
    center_x = x + SPACESHIP_WIDTH /2
    center_y = y + SPACESHIP_HEIGHT /2
    if (
        (center_x - SPACESHIP_WIDTH < touch.x and touch.x < center_x + SPACESHIP_WIDTH)
        and (center_y - SPACESHIP_HEIGHT < touch.y and touch.y < center_y + SPACESHIP_HEIGHT)
    ):
        return False
    else:
        return True'''


def update_spaceship_destination(self, touch):
    if touch.x < 0:
        go_to_x = 0
    elif touch.x > self.width - SPACESHIP_WIDTH:
        go_to_x = self.width - SPACESHIP_WIDTH
    else:
        go_to_x = touch.x
    
    if touch.y < 0:
        go_to_y = 0
    elif touch.y > self.height - SPACESHIP_HEIGHT:
        go_to_y = self.height - SPACESHIP_HEIGHT
    else:
        go_to_y = touch.y

    x, y = self.spaceship.body.pos
    dx = abs(x - touch.x)
    dy = abs(y - touch.y)

    speed_corrector_x = 1.0
    speed_corrector_y = 1.0

    if dx > dy and dx > 0:
        speed_corrector_y = dy / dx
    elif dy > dx and dy > 0:
        speed_corrector_x = dx/ dy

    self.dict_destination = {
                            "go_to_x": go_to_x, 
                            "go_to_y": go_to_y, 
                            "speed_corrector_x": speed_corrector_x, 
                            "speed_corrector_y": speed_corrector_y,
                            "is_moving": True
                            }


def on_touch_up(self, touch):
    x, y = self.spaceship.body.pos
    self.dict_destination = {
                                "go_to_x": x, 
                                "go_to_y": y, 
                                "speed_corrector_x": 0.0, 
                                "speed_corrector_y": 0.0,
                                "is_moving": False
                             }