import pygame
import random


class Fruit(pygame.sprite.Sprite):
    """Class for objects for the snake to eat"""
    def __init__(self, screen):
        super().__init__()

        # Pygame display screen
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        # Size of fruit
        self.size = [10, 10]

        # Color of the fruit
        self.red = (255, 0, 0)

        # Margin for fruit placement
        self.margin = 100

        # Create an image of the fruit and fill it with a color.
        self.image = pygame.Surface(self.size)
        self.image.fill(self.red)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Set position of the fruit
        self.rect.x = random.randrange(0 + self.margin, self.screen_width - self.margin, 10)
        self.rect.y = random.randrange(0 + self.margin, self.screen_height - self.margin, 10)

    def update(self):
        """Place fruit in specified coordinates"""
        self.screen.blit(self.image, self.rect)
