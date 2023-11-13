import pygame
import BodyModule


class Serpent:
    """Class for the snake character"""
    def __init__(self, screen):
        """Initialize snake sprite in the game"""
        super().__init__()

        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        self.body = [BodyModule.BodyModule(self.screen)]

        self.body[0].rect.x = self.screen_width / 2
        self.body[0].rect.y = self.screen_height / 2

        self.body[0].screen.blit(self.body[0].image, self.body[0].rect)

        # Speed of snake
        self.speed = 5

        # Direction of moving
        self.directions = {"left": (-1, 0), "right": (1, 0), "down": (0, 1), "up": (0, -1), "stop": (0, 0)}

    def update(self, command):
        """Update position of the snake"""
        self.body[0].rect.move_ip(self.directions[command])
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.body[0].image, self.body[0].rect)
