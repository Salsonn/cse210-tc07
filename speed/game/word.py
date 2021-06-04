import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):

    def __init__(self):
        self._points = 0
        self.set_text('@')
        self.reset()

    def get_points(self):
        return self._points

    def reset(self):
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 15)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)