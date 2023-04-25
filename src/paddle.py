"""
A class to represent a paddle in the game of Pong.

Attributes
----------
- position : list[int, int]
    The x and y coordinates of the paddle's top-left corner.
- size : tuple[int, int]
    The width and height of the paddle.
- speed : int
    The speed at which the paddle can move up and down.
- velocity : int
    The current velocity of the paddle.
- player : bool, optional
    A boolean value indicating whether the paddle is controlled by a player or the computer.

Methods
-------
- move(ball: Ball) -> None:
    Moves the paddle up or down based on the position of the ball.
- draw(surface, colour: tuple[int, int, int]) -> None:
    Draws the paddle on the given surface with the given colour.
"""

import pygame
from ball import Ball

# Define Paddle class
class Paddle:
    """
    A class to represent a paddle in the game of Pong.

    Attributes
    ----------
    - position : list[int, int]
        The x and y coordinates of the paddle's top-left corner.
    - size : tuple[int, int]
        The width and height of the paddle.
    - speed : int
        The speed at which the paddle can move up and down.
    - velocity : int
        The current velocity of the paddle.
    - player : bool, optional
        A boolean value indicating whether the paddle is controlled by a player or the computer.

    Methods
    -------
    - move(ball: Ball) -> None:
        Moves the paddle up or down based on the position of the ball.
    - draw(surface, colour: tuple[int, int, int]) -> None:
        Draws the paddle on the given surface with the given colour.
    """

    def __init__(self, position: tuple[int, int], size: tuple[int, int], speed: int, player: bool = True) -> None:
        """
        Constructs all necessary attributes for the Paddle object.

        Parameters
        ----------
        - position : tuple[int, int]
            The x and y coordinates of the paddle's top-left corner.
        - size : tuple[int, int]
            The width and height of the paddle.
        - speed : int
            The speed at which the paddle can move up and down.
        - player : bool, optional
            A boolean value indicating whether the paddle is controlled by a player or the computer. Defaults to True.
        """
        # self.position = [position[0], position[1]/2 - size[1]/2]
        self.position = [position[0]/2 - size[0]/2, position[1]]
        self.size = size
        self.speed = speed
        self.velocity = 0
        self.player = player

    def move(self, ball: Ball) -> None:
        """
        Moves the paddle up or down based on the position of the ball.

        Args
        ----------
        - ball : Ball
            The ball object used to determine the direction of movement.
        """
        if not self.player:
            if ball.position[1] < self.position[1] + self.size[1]/2:
                self.velocity = -self.speed
            elif ball.position[1] > self.position[1] + self.size[1]/2:
                self.velocity = self.speed
            else:
                self.velocity = 0
        self.position[0] += self.velocity

    def draw(self, surface, colour: tuple[int, int, int]) -> None:
        """
        Draws the paddle on the given surface with the given colour.

        Parameters
        ----------
        - surface : pygame.Surface
            The surface on which to draw the paddle.
        - colour : tuple[int, int, int]
            The colour of the paddle.
        """
        pygame.draw.rect(surface, colour, [self.position[0], self.position[1], self.size[0], self.size[1]])
