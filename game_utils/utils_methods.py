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
    

def speed_corrector(x_pos, y_pos, x_target, y_target) -> tuple[int, int]:
    dx = abs(x_pos - x_target)
    dy = abs(y_pos - y_target)

    speed_corrector_x = 1.0
    speed_corrector_y = 1.0

    if dx > dy and dx > 0:
        speed_corrector_y = dy / dx
    elif dy > dx and dy > 0:
        speed_corrector_x = dx/ dy
    
    return (speed_corrector_x, speed_corrector_y)


def a_b_function(x1, y1, x2, y2) -> tuple[float, float]:
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a, b