import pygame
from ball import Ball

# Define Paddle class
class Paddle:
    def __init__(self, position: tuple[int, int], size: tuple[int, int], speed: int, player: bool = True) -> None:
        self.position = [position[0], position[1]/2 - size[1]/2]
        self.size = size
        self.speed = speed
        self.velocity = 0
        self.player = player

    def move(self, ball: Ball) -> None:
        if not self.player:
            if ball.position[1] < self.position[1] + self.size[1]/2:
                self.velocity = -self.speed
            elif ball.position[1] > self.position[1] + self.size[1]/2:
                self.velocity = self.speed
            else:
                self.velocity = 0
        self.position[1] += self.velocity

    def draw(self, surface, colour: tuple[int, int, int]) -> None:
        pygame.draw.rect(surface, colour, [self.position[0], self.position[1], self.size[0], self.size[1]])
