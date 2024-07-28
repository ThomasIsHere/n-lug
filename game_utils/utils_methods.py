from kivy.uix.screenmanager import Screen
from math import sqrt, pow


def distance_2_points(x1, y1, x2, y2) -> float:
      return sqrt(pow(x1-x2,2) + pow(y1-y2,2))


def do_not_touch_spaceship(screen: Screen, go_x: int, go_y: int) -> bool:
    x, y = screen.spaceship.body.pos
    w, h = screen.spaceship.body.size
    center_x = x + w /2
    center_y = y + h /2
    if (
        (center_x - w < go_x and go_x < center_x + h)
        and (center_y - w < go_y and go_y < center_y + h)
    ):
        return False
    else:
        return True
    

def spaceship_stops(screen: Screen):
      x, y = screen.spaceship.body.pos
      screen.dict_destination = {
                                "go_to_x": x, 
                                "go_to_y": y, 
                                "speed_corrector_x": 0.0, 
                                "speed_corrector_y": 0.0,
                                "is_moving": False
                             }


def point_in_range(p1, p2, p3):
    if p1 >= p2 and p1 <= p3:
        return True
    else:
        return False