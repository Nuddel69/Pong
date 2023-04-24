import random
import pygame

# Define Ball class
class Ball:
    def __init__(self, x: float, y: float, speed: int, radius: int) -> None:
        self.position = [x, y]
        self.velocity = [random.choice([-1, 1]) * speed, random.uniform(-1, 1) * speed]
        self.radius = radius

    def move(self) -> None:
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self, surface, colour: tuple[int, int, int]) -> None:
        pygame.draw.circle(surface, colour, [int(self.position[0]), int(self.position[1])], self.radius)
