from .utils_methods import speed_corrector


def on_touch_move(self, touch):
    update_spaceship_destination(self, touch)


def on_touch_down(self, touch):
    update_spaceship_destination(self, touch)


def update_spaceship_destination(self, touch):
    w, h = self.spaceship.body.size

    if touch.x < 0:
        go_to_x = 0
    elif touch.x > self.width - w:
        go_to_x = self.width - h
    else:
        go_to_x = touch.x
    
    if touch.y < 0:
        go_to_y = 0
    elif touch.y > self.height - w:
        go_to_y = self.height - h
    else:
        go_to_y = touch.y

    x, y = self.spaceship.body.pos
    speed_corrector_x, speed_corrector_y = speed_corrector(x, y, touch.x, touch.y)

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