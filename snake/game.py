import pygame
import sys
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self)
        self.food = Food(self)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.snake.handle_event(event)

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(10)  # Adjust snake speed

    def update(self):
        self.snake.move()
        self.snake.check_collision(self.food)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill screen with black
        self.snake.draw()
        self.food.draw()

