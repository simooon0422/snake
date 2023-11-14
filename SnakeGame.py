import pygame
import Serpent
import Fruit
import time


class SnakeGame:
    """Main game class"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        pygame.display.set_caption("Super Snake")
        self.screen = pygame.display.set_mode((500, 500))
        self.snake = Serpent.Serpent(self.screen)
        self.direction = "stop"

        self.fruits_list = []

    def run_game(self):
        """Main game loop"""
        while True:
            pygame.display.flip()
            self.snake.update_body(self.direction)
            self._handle_fruits()
            self._handle_events()

            time.sleep(0.1)  # delay for snake's movement

    def _handle_events(self):
        """Function to handle pressing keys"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = "right"
                elif event.key == pygame.K_LEFT:
                    self.direction = "left"
                elif event.key == pygame.K_UP:
                    self.direction = "up"
                elif event.key == pygame.K_DOWN:
                    self.direction = "down"

    def _handle_fruits(self):
        if not self.fruits_list:
            self.fruits_list.append(Fruit.Fruit(self.screen))
        else:
            self.fruits_list[0].update(100, 300)
