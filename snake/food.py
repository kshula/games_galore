import pygame
import random

class Food:
    def __init__(self, game):
        self.game = game
        self.position = [random.randrange(1, self.game.width // 10) * 10,
                         random.randrange(1, self.game.height // 10) * 10]

    def draw(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], 10, 10))

    def randomize_position(self):
        self.position = [random.randrange(1, self.game.width // 10) * 10,
                         random.randrange(1, self.game.height // 10) * 10]
