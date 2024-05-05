import pygame

class Snake:
    def __init__(self, game):
        self.game = game
        self.size = 1
        self.elements = [[100, 100]]  # Snake position
        self.direction = "RIGHT"
        self.dx = 10
        self.dy = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != "DOWN":
                self.direction = "UP"
                self.dx = 0
                self.dy = -10
            elif event.key == pygame.K_DOWN and self.direction != "UP":
                self.direction = "DOWN"
                self.dx = 0
                self.dy = 10
            elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                self.direction = "LEFT"
                self.dx = -10
                self.dy = 0
            elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                self.direction = "RIGHT"
                self.dx = 10
                self.dy = 0

    def move(self):
        head = self.elements[0][:]
        new = [head[0] + self.dx, head[1] + self.dy]
        self.elements.insert(0, new)
        if len(self.elements) > self.size:
            self.elements.pop()

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(self.game.screen, (255, 255, 255), pygame.Rect(element[0], element[1], 10, 10))

    def check_collision(self, food):
        if self.elements[0] == food.position:
            self.size += 1
            food.randomize_position()
