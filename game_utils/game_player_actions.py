from kivy.metrics import dp


def on_touch_move(self, touch):
    update_spaceship_destination(self, touch)


def on_touch_down(self, touch):
    update_spaceship_destination(self, touch)


def update_spaceship_destination(self, touch):
    print(self.spaceship.fuel)
    if touch.x < 0:
        go_to_x = 0
    elif touch.x > self.width - dp(40):
        go_to_x = self.width - dp(40)
    else:
        go_to_x = int(touch.x)
    
    if touch.y < 0:
        go_to_y = 0
    elif touch.y > self.height - dp(40):
        go_to_y = self.height - dp(40)
    else:
        go_to_y = int(touch.y)

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