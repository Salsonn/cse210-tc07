from game import output_service
import sys
import random
from game.point import Point
from game.buffer import Buffer
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _directions (Dict): A dictionary containing Points for U, D, L and R.
        _current (Point): The last direction that was pressed.
    """

    def __init__(self, screen, output_service):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        self._buffer = Buffer()
        self._output_service = output_service
        self._directions = {}
        self._directions[119] = Point(0, -1) # UP
        self._directions[97] = Point(-1, 0) # DOWN
        self._directions[100] = Point(1, 0) # RIGHT
        self._directions[115] = Point(0, 1) # LEFT
        self._current = self._directions[100]
        
    def get_direction(self):
        """Gets the selected direction. If one hasn't been selected the last 
        one is returned.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        directional = [119, 97, 100, 115]
        event = self._screen.get_key()
        if not event is None:
            if event == 27:
                sys.exit()
            self._current = self._directions.get(event, self._current)
        return self._directions[random.choice(directional)], event