#def keyboard_closed(self):
#    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
#    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
#    self._keyboard = None


def on_key_down(self, window, key, scancode, codepoint, modifier):
    if key in (273, 274, 275, 276):  # Arrow keys key codes
        self.keys_pressed.add(key)
    return True


def on_key_up(self, window, key, scancode):
    if key in (273, 274, 275, 276):
        self.keys_pressed.discard(key)
    return True


def on_touch_move(self, touch):
    update_spaceship_destination(self, touch)


def on_touch_down(self, touch):
    update_spaceship_destination(self, touch)


def update_spaceship_destination(self, touch):
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
                                "go_to_x": int(touch.x), 
                                "go_to_y": int(touch.y), 
                                "speed_corrector_x": speed_corrector_x, 
                                "speed_corrector_y": speed_corrector_y
                             }


def on_touch_up(self, touch):
    x, y = self.spaceship.body.pos
    self.dict_destination = {
                                "go_to_x": x, 
                                "go_to_y": y, 
                                "speed_corrector_x": 0.0, 
                                "speed_corrector_y": 0.0
                             }
