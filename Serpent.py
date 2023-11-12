import pygame


class Serpent(pygame.sprite.Sprite):
    """Class for the snake character"""
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        # Color of the snake
        self.green = (0, 255, 0)

        # Create an image of the snake and fill it with a color.
        self.image = pygame.Surface([50, 50])
        self.image.fill(self.green)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        self.rect.center = (self.screen_width / 2, self.screen_height / 2)

        self.screen.blit(self.image, self.rect)
