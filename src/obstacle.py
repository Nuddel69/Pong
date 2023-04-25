import random
import pygame

class Obstacle:
    def __init__(self, position: tuple[int, int], size: tuple[int, int]) -> None:
        """
        Initializes a new obstacle object with the given position and size.

        Args
        ----
        - position: a tuple containing the x and y coordinates of the obstacle's top-left corner
        - size: a tuple containng the width and height dimensions of the obstacle
        """
        self.position = position
        self.size = size

    def draw(self, surface, colour: tuple[int, int, int]) -> None:
        """
        Draws the obstacle on the given surface with the given colour.

        Parameters
        ----------
        - surface : pygame.Surface
            The surface on which to draw the paddle.
        - colour : tuple[int, int, int]
            The colour of the paddle.
        """
        pygame.draw.rect(surface, colour, [self.position[0], self.position[1], self.size[0], self.size[1]])
