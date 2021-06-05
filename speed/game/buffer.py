import random
from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """The player's current input buffer. Can be cleared with 'Enter' or 'Return'

    Stereotype:
        Information Holder

    Attributes: 
        _buffer (string): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes the buffer to an empty string, sets the position and updates the text.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        super().__init__()
        self._buffer = ""
        position = Point(1, constants.MAX_Y - 1)
        self.set_position(position)
        self.set_text(f"Buffer: {self._buffer}")
    
    def add_input(self, input):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Buffer): An instance of Buffer.
            input (char): The character to add to the buffer.
        """
        self._buffer += input
        self.set_text(f"Buffer: {self._buffer}")

    def clear_input(self):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        self._buffer = ""
        self.set_text(f"Buffer: ")

    def get_buffer(self):
        """ Returns the current buffer

        Args:
            self (Buffer): An instance of Buffer
        """
        return self._buffer