import pygame
import BodyModule


class Serpent:
    """Class for the snake character"""
    def __init__(self, screen):
        """Initialize snake sprite in the game"""
        super().__init__()

        # Used Pygame display
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        # Black colour for the background
        self.black = (0, 0, 0)

        # Store objects forming snake's body
        self.body = []

        # Store current and new body objects' positions
        self.body_positions = []
        self.new_body_positions = self.body_positions

        # Speed of snake
        self.speed = 5

        # Direction of moving
        self.directions = {"left": (-1, 0), "right": (1, 0), "down": (0, 1), "up": (0, -1), "stop": (0, 0)}

        self._create_body()

    def _create_body(self):
        """Create initial body of the snake"""

        # Fill list with body objects
        for i in range(3):
            self.body.append(BodyModule.BodyModule(self.screen))
        self.body_positions = [(0, 0)] * len(self.body)

        # Set position of the rest of the starting body objects
        for i in range(len(self.body)):
            if i == 0:
                # Set position of the first body part (head)
                self.body[0].rect.x = self.screen_width / 2
                self.body[0].rect.y = self.screen_height / 2
            else:
                self.body[i].rect.x = self.body[i-1].rect.x
                self.body[i].rect.y = self.body[i-1].rect.y + 50

            # Save current positions of modules
            self.body_positions[i] = (self.body[i].rect.x, self.body[i].rect.y)

    def update_body(self, command):
        """Update position of the snake's body modules"""
        self.body[0].rect.move_ip(self.directions[command])
        self.screen.fill(self.black)

        for i in range(len(self.body)):
            self.screen.blit(self.body[i].image, self.body[i].rect)
