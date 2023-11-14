import pygame


class Fruit(pygame.sprite.Sprite):
    """Class for objects for the snake to eat"""
    def __init__(self, screen):
        super().__init__()

        # Pygame display screen
        self.screen = screen

        # Size of fruit
        self.size = [10, 10]

        # Color of the fruit
        self.red = (255, 0, 0)

        # Create an image of the fruit and fill it with a color.
        self.image = pygame.Surface(self.size)
        self.image.fill(self.red)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def update(self, x, y):
        """Place fruit in specified coordinates"""
        self.rect.x = x
        self.rect.y = y
        self.screen.blit(self.image, self.rect)
