import pygame


class BodyModule(pygame.sprite.Sprite):
    """Class for creating body of the snake in parts"""
    def __init__(self, screen):
        super().__init__()

        # Pygame display screen
        self.screen = screen

        # Color of the body
        self.green = (0, 255, 0)

        # Create an image of the body module and fill it with a color.
        self.image = pygame.Surface([10, 10])
        self.image.fill(self.green)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def update(self, offset):
        """Update position of the body part"""
        self.rect.move_ip(offset)
        self.screen.blit(self.image, self.rect)

