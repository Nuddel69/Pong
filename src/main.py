"""
A simple Pong game implemented using Pygame.

Controls:
- Player 1: Up and Down arrow keys to move up and down.
- Player 2: Computer

Scoring:
- A player scores a point if the ball goes past the opposing paddle.

End Game:
- The game ends when one player reaches a score of 3.

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
from paddle import Paddle

# Define game constants
WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
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
        self.WINNING_SCORE = 3
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.ball = Ball((WIDTH/2, HEIGHT/2), BALL_SPEED, BALL_RADIUS)
        self.player_paddle = Paddle((0, HEIGHT), (PADDLE_WIDTH, PADDLE_HEIGHT), PADDLE_SPEED)
        self.computer_paddle = Paddle(((WIDTH - PADDLE_WIDTH), HEIGHT), (PADDLE_WIDTH, PADDLE_HEIGHT), PADDLE_SPEED, False)
        self.score = [0, 0]

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player_paddle.velocity = -PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    self.player_paddle.velocity = PADDLE_SPEED
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player_paddle.velocity = 0

    def detect_collisions(self) -> None:
        # Detect collision between ball and player paddle
        if self.ball.position[0] - BALL_RADIUS <= self.player_paddle.position[0] + PADDLE_WIDTH \
                and self.player_paddle.position[1] <= self.ball.position[1] <= self.player_paddle.position[1] + PADDLE_HEIGHT:
            self.ball.velocity[0] = BALL_SPEED
        # Detect collision between ball and computer paddle
        elif self.ball.position[0] + BALL_RADIUS >= self.computer_paddle.position[0] \
                and self.computer_paddle.position[1] <= self.ball.position[1] <= self.computer_paddle.position[1] + PADDLE_HEIGHT:
            self.ball.velocity[0] = -BALL_SPEED
        # Detect collision between ball and top or bottom edge of screen
        if self.ball.position[1] - BALL_RADIUS <= 0 or self.ball.position[1] + BALL_RADIUS >= HEIGHT:
            self.ball.velocity[1] = -self.ball.velocity[1]
        # Detect collision between player paddle and top or bottom edge of screen
        if self.player_paddle.position[1] <= 0:
            self.player_paddle.position[1] = 0
        elif self.player_paddle.position[1] + PADDLE_HEIGHT >= HEIGHT:
            self.player_paddle.position[1] = HEIGHT - PADDLE_HEIGHT
        # Detect collision between computer paddle and top or bottom edge of screen
        if self.computer_paddle.position[1] <= 0:
            self.computer_paddle.position[1] = 0
        elif self.computer_paddle.position[1] + PADDLE_HEIGHT >= HEIGHT:
            self.computer_paddle.position[1] = HEIGHT - PADDLE_HEIGHT

    def update_score(self) -> None:
        # Check if ball goes out of bounds on player side
        if self.ball.position[0] + BALL_RADIUS >= WIDTH:
            self.score[0] += 1
            self.ball.__init__((WIDTH/2, HEIGHT/2), BALL_SPEED, BALL_RADIUS)
        # Check if ball goes out of bounds on computer side
        elif self.ball.position[0] - BALL_RADIUS <= 0:
            self.score[1] += 1
            self.ball.__init__((WIDTH/2, HEIGHT/2), BALL_SPEED, BALL_RADIUS)

        if self.score[0] >= self.WINNING_SCORE:
            self.show_end_screen("Player wins!")
        elif self.score[1] >= self.WINNING_SCORE:
            self.show_end_screen("Computer wins!")

    def draw_score(self) -> None:
        font = pygame.font.Font(None, 36)
        player_score = font.render(str(self.score[0]), True, WHITE)
        computer_score = font.render(str(self.score[1]), True, WHITE)
        self.screen.blit(player_score, (WIDTH/4, 10))
        self.screen.blit(computer_score, (3*WIDTH/4, 10))

    def quit(self) -> None:
        pygame.quit()
        quit()

    def show_end_screen(self, message):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000) # Display the screen for 3 seconds
        self.quit()


    def run(self) -> None:
        while True:
            self.handle_events()
            self.detect_collisions()
            self.update_score()

            self.screen.fill(BLACK)

            self.ball.move()
            self.ball.draw(self.screen, WHITE)

            self.player_paddle.move(self.ball)
            self.player_paddle.draw(self.screen, WHITE)

            self.computer_paddle.move(self.ball)
            self.computer_paddle.draw(self.screen, WHITE)

            self.draw_score()

            pygame.display.update()
            self.clock.tick(FRAMERATE)

if __name__ == "__main__":
    game = Game()
    game.run()
