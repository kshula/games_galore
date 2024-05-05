import pygame
import random
import sys

# Constants
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40
MAZE_SIZE = 10  # Maze grid size (MAZE_SIZE x MAZE_SIZE)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class MazeGame:
    def __init__(self):
        self.maze = self.generate_maze()
        self.player_pos = (0, 0)
        self.finish_pos = (MAZE_SIZE - 1, MAZE_SIZE - 1)
        self.cell_size = CELL_SIZE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Game")
        self.clock = pygame.time.Clock()

    def generate_maze(self):
        # Generate a random maze grid
        maze = [[' ' for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                if random.random() < 0.3:  # 30% chance of obstacle
                    maze[i][j] = '#'
        
        return maze

    def draw_maze(self):
        self.screen.fill(WHITE)
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                color = BLACK if self.maze[i][j] == '#' else WHITE
                pygame.draw.rect(self.screen, color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
        
        # Draw player
        pygame.draw.circle(self.screen, GREEN, (self.player_pos[1] * self.cell_size + self.cell_size // 2,
                                                self.player_pos[0] * self.cell_size + self.cell_size // 2), self.cell_size // 3)

        pygame.display.flip()

    def move_player(self, dx, dy):
        # Move the player in the specified direction (dx, dy)
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        if 0 <= new_x < MAZE_SIZE and 0 <= new_y < MAZE_SIZE and self.maze[new_x][new_y] != '#':
            self.player_pos = (new_x, new_y)

    def check_game_over(self):
        # Check if the player reached the finish
        return self.player_pos == self.finish_pos


def main():
    pygame.init()
    game = MazeGame()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.move_player(-1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move_player(1, 0)
                elif event.key == pygame.K_LEFT:
                    game.move_player(0, -1)
                elif event.key == pygame.K_RIGHT:
                    game.move_player(0, 1)

        game.draw_maze()

        if game.check_game_over():
            font = pygame.font.Font(None, 36)
            text = font.render("Congratulations! You reached the finish!", True, RED)
            game.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(3000)  # Display message for 3 seconds
            game = MazeGame()  # Restart the game

        game.clock.tick(30)  # Limit frame rate


if __name__ == '__main__':
    main()
