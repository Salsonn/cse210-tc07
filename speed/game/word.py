import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):

    def __init__(self):
        self._points = 0
        self.set_text('3')
        self.reset()

    def get_points(self, word):
        self._points = len(word)
        return self._points

    def reset(self):
        x = constants.MAX_X - constants.MAX_X - 4
        y = constants.MAX_Y - constants.MAX_Y - 3
        position = Point(x, y)
        self.set_position(position)