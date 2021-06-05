import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word_move:
    """A class that controls the random movement of each random word.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The total amount of random words on the screen at a given time (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word_move): an instance of Word_move.
        """
        super().__init__()
        self._segments = []
        self._prepare_body()
    
    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Word_move): an instance of Word_move.

        Returns:
            list: The words from the list.
        """
        return self._segments

    def get_body(self):
        """Gets the random words
        
        Args:
            self (Word_move): An instance of Word_move.

        Returns:
            list: The random words.
        """
        return self._segments[1:]

    def get_head(self):
        """Gets the first of many random words.
        
        Args:
            self (Word_move): An instance of Word_move.

        Returns:
            Actor: The first random word.
        """
        return self._segments[0]

    def grow_tail(self):
        """Grows the length of random words.
        
        Args:
            self (Word_move): an instance of Word_move.
        """
        tail = self._segments[-1]
        offset = tail.get_velocity().reverse()
        text = ""
        position = tail.get_position().add(offset)
        velocity = tail.get_velocity()
        self._add_segment(text, position, velocity)
    
    def move_head(self, direction):
        """Moves the words in a random direction.

        Args:
            self (Word_move): an instance of Word_move.
            direction (Point): The direction to move.
        """
        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Word_move): an instance of Word_move.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_body(self):
        """Prepares the random words by retreiving the words from a separate file.
        
        Args:
            self (Word_move): an instance of Word_move.
        """
        self.words = []
        self.chosen_words = []
        interval_x = [random.randint(1, 4), random.randint(5, 11), random.randint(12, 25), random.randint(26, 30), random.randint(31, 52)]
        interval_y = [random.randint(1, 3), random.randint(4, 7), random.randint(8, 12), random.randint(13, 15), random.randint(16, 18)]
        with open('game\words.txt', 'rt') as file:
            for word in file:
                word = word.strip()
                self.words.append(word)

        for _ in range(5):
            x = int(interval_x[-1])
            y = int(interval_y[-1])
            text = random.choice(self.words)
            self.chosen_words.append(text)
            position = Point(x, y)
            interval_x.pop()
            interval_y.pop()
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)

    def remove_word(self):
        self._segments = []
        interval_x = [random.randint(1, 4), random.randint(5, 11), random.randint(12, 25), random.randint(26, 30), random.randint(31, 52)]
        interval_y = [random.randint(1, 3), random.randint(4, 7), random.randint(8, 12), random.randint(13, 15), random.randint(16, 18)]

        # l represents the length of random words on the screen.
        for l in range(5):
            if l == 0:
                text = random.choice(self.words)
                self.chosen_words.append(text)
            x = int(interval_x[-1])
            y = int(interval_y[-1])
            position = Point(x, y)
            interval_x.pop()
            interval_y.pop()
            velocity = Point(1, 0)
            self._add_segment(self.chosen_words[l], position, velocity)

    def return_words(self):
        return self.chosen_words