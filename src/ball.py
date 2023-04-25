"""
A class representing a ball in a Pong game.

Attributes
----------
- position: a list containing the x and y coordinates of the center of the ball
- velocity: a list containing the x and y components of the velocity of the ball
- radius: the radius of the ball

Methods
-------
- move(): moves the ball according to its velocity
- draw(surface, colour): draws the ball on the given surface with the given colour
"""

import random
import pygame

# Define Ball class
class Ball:
    """
    A class representing a ball in a Pong game.

    Attributes
    ----------
    - position: a list containing the x and y coordinates of the center of the ball
    - velocity: a list containing the x and y components of the velocity of the ball
    - radius: the radius of the ball

    Methods
    -------
    - move(): moves the ball according to its velocity
    - draw(surface, colour): draws the ball on the given surface with the given colour
    """

    def __init__(self, position: tuple[float, float], speed: int, radius: int) -> None:
        """
        Initializes a new Ball object with the given position, speed, and radius.
        The velocity of the ball is initialized randomly.

        Args
        ----
        - position: a tuple containing the x and y coordinates of the center of the ball
        - speed: the speed of the ball
        - radius: the radius of the ball
        """
        self.position = [position[0], position[1]]
        self.velocity = [random.choice([-1, 1]) * speed, random.uniform(-1, 1) * speed]
        self.radius = radius

    def move(self) -> None:
        """
        Updates the position of the ball according to its velocity.
        """
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self, surface, colour: tuple[int, int, int]) -> None:
        """
        Draws the ball on the given surface with the given colour.

        Args
        ----
        - surface: the surface on which to draw the ball
        - colour: a tuple containing the RGB values of the colour to draw the ball
        """
        pygame.draw.circle(surface, colour, [int(self.position[0]), int(self.position[1])], self.radius)
