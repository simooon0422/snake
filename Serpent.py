import pygame


class Serpent(pygame.sprite.Sprite):
    """Class for the snake character"""
    def __init__(self, game):
        """Initialize snake sprite in the game"""
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

        # Coordinates of snake's rect
        self.rect.x = self.screen_width / 2
        self.rect.y = self.screen_height / 2

        # Speed of snake
        self.speed = 5

        # Direction of moving
        self.directions = {"left": (-1, 0), "right": (1, 0), "down": (0, 1), "up": (0, -1), "stop": (0, 0)}

        # Display snake
        self.screen.blit(self.image, self.rect)

        self.update("up")

    def update(self, command):
        """Update position of the snake"""
        self.rect.move_ip(self.directions[command])
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.image, self.rect)

