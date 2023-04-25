"""
A simple Tennis game implemented using Pygame.

Controls:
- Player 1: Left and Right arrow keys to move left and right.

Scoring:
- A player scores a point if the ball hits the paddle.

End Game:
- The game ends when if the ball hits the bottom edge of the screen.

Classes:
- Paddle: Represents a paddle object.
- Ball: Represents the ball object.
- Game: Represents the game object and runs the game loop.

Global Constants:
- WIDTH: An integer representing the width of the game screen.
- HEIGHT: An integer representing the height of the game screen.
- FRAMERATE: An integer representing the frame rate of the game.

Usage:
- Run the script to start the game.

Authors:
- Mats Bjønnes

Date Created:
- 25 april 2023
"""

import pygame

from ball import Ball
from obstacle import Obstacle
from paddle import Paddle

# Define game constants
WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10
BALL_SPEED = 5
FRAMERATE = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()

# Define Game class
class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.ball = Ball((WIDTH/2, HEIGHT/2), BALL_SPEED, BALL_RADIUS)
        self.player_paddle = Paddle((WIDTH, HEIGHT - 30), (PADDLE_WIDTH, PADDLE_HEIGHT), PADDLE_SPEED)
        self.score = 0
        self.obstacles = [Obstacle([WIDTH/2, HEIGHT/3], [50, 50]), Obstacle([WIDTH/3, HEIGHT/3], [50, 75])]

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player_paddle.velocity = -PADDLE_SPEED
                elif event.key == pygame.K_RIGHT:
                    self.player_paddle.velocity = PADDLE_SPEED
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.player_paddle.velocity = 0

    def detect_collisions(self) -> None:
        # Detect collision between ball and player paddle
        if self.ball.position[1] + BALL_RADIUS >= self.player_paddle.position[1]\
           and self.player_paddle.position[0] <= self.ball.position[0] <= self.player_paddle.position[0] + PADDLE_WIDTH:
            self.score += 1
            self.ball.velocity[1] = -self.ball.velocity[1]

        # Detect collision between ball and top edge of screen
        if self.ball.position[1] - BALL_RADIUS <= 0:
            self.ball.velocity[1] = -self.ball.velocity[1]

        # Detect collision between ball and left or right edge of screen
        if (self.ball.position[0] - BALL_RADIUS <= 0) or \
           (self.ball.position[0] + BALL_RADIUS >= WIDTH):
            self.ball.velocity[0] = -self.ball.velocity[0]

        # Detect collision between player paddle and top or bottom edge of screen
        if self.player_paddle.position[1] <= 0:
            self.player_paddle.position[1] = 0
        elif self.player_paddle.position[1] + PADDLE_HEIGHT >= HEIGHT:
            self.player_paddle.position[1] = HEIGHT - PADDLE_HEIGHT

        if self.player_paddle.position[0] <= 0:
            self.player_paddle.position[0] = 0
        elif self.player_paddle.position[0] + PADDLE_WIDTH >= WIDTH:
            self.player_paddle.position[0] = WIDTH - PADDLE_WIDTH

        # Check if ball goes out of bounds
        if self.ball.position[1] + BALL_RADIUS >= HEIGHT:
            self.show_end_screen("Game over.")
            # self.ball.__init__((WIDTH/2, HEIGHT/2), BALL_SPEED, BALL_RADIUS)

        # Check if ball collides with any obstacle - Based on the AABB collision-test
        for obstacle in self.obstacles:
            if (self.ball.position[0] + self.ball.radius >= obstacle.position[0] and \
                obstacle.position[0] + obstacle.size[0] >= self.ball.position[0] and \
                self.ball.position[1] + self.ball.radius >= obstacle.position[1] and \
                obstacle.position[1] + obstacle.size[1] >= self.ball.position[1]):
                self.ball.velocity[0] = -self.ball.velocity[0]
                # self.ball.velocity[1] = -self.ball.velocity[1]


    def draw_score(self) -> None:
        font = pygame.font.Font(None, 36)
        player_score = font.render(str(self.score), True, WHITE)
        self.screen.blit(player_score, (WIDTH/2, 15))

    def quit(self) -> None:
        pygame.quit()
        quit()

    def show_end_screen(self, message):
        font = pygame.font.Font(None, 36)

        text = font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))

        score = font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score.get_rect(center=(WIDTH/2, (HEIGHT/2) + 36))

        self.screen.blit(text, text_rect)
        self.screen.blit(score, score_rect)
        pygame.display.update()
        pygame.time.wait(3000) # Display the screen for 3 seconds
        self.quit()

    def run(self) -> None:
        while True:
            self.handle_events()
            self.detect_collisions()

            self.screen.fill(BLACK)

            self.ball.move()
            self.ball.draw(self.screen, WHITE)

            self.player_paddle.move(self.ball)
            self.player_paddle.draw(self.screen, WHITE)

            for obstacle in self.obstacles:
                obstacle.draw(self.screen, WHITE)

            self.draw_score()

            pygame.display.update()
            self.clock.tick(FRAMERATE)

if __name__ == "__main__":
    game = Game()
    game.run()
