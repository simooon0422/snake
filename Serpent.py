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
        self.directions = {"left": (-1, 0), "right": (0, 1), "down": (0, 1), "up": (0, -1), "stop": (0, 0)}
        # self.directions = [[0, 0], [-1, 0], [0, 1], [0, 1], [0, -1]]
        self.current_direction = self.directions["down"]
        # Display snake
        self.screen.blit(self.image, self.rect)

        self.update()

    def update(self):
        """Update position of the snake"""
        print(self.rect.center)
        self.rect.x = self.rect.x + self.current_direction[0]
        self.rect.y = self.rect.y + self.current_direction[1]
        print(self.rect.center)
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.image, self.rect)
