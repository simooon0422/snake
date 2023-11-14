import pygame
import Serpent
import Fruit
import time
import random


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
        self.fruits_position = []

    def run_game(self):
        """Main game loop"""
        while True:
            pygame.display.flip()
            self.snake.update_body(self.direction)
            self._handle_fruits()
            self._handle_collisions()
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
        """Function for displaying fruits for snake on the screen"""
        if not self.fruits_list:
            self.fruits_list.append(Fruit.Fruit(self.screen))
            self.fruits_position.append((random.randrange(200, 400, 10), random.randrange(200, 400, 10)))
        else:
            self.fruits_list[0].update(self.fruits_position[0][0], self.fruits_position[0][1])

    def _handle_collisions(self):
        """Function specifying action after collision of objects"""
        for i in range(len(self.fruits_list)):
            if pygame.Rect.colliderect(self.snake.body[0].rect, self.fruits_list[0].rect):
                del self.fruits_list[i]
                self.fruits_position.pop(i)
                self.snake.grow()
                print("Eat apple")

        for i in range(1, len(self.snake.body)):
            if pygame.Rect.colliderect(self.snake.body[0].rect, self.snake.body[i].rect):
                print("Game Over")
