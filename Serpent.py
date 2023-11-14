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

        # Initial length of snake (in modules)
        self.initial_length = 3

        # Store objects forming snake's body
        self.body = []

        # Store offsets to new positions
        self.offsets = [(0, 0)] * self.initial_length

        # Speed of snake
        self.speed = 5

        # Direction of moving
        self.directions = {"left": (-10, 0), "right": (10, 0), "down": (0, 10), "up": (0, -10), "stop": (0, 0)}

        self._create_body()

    def _create_body(self):
        """Create initial body of the snake"""

        # Fill list with body objects
        for i in range(self.initial_length):
            self.body.append(BodyModule.BodyModule(self.screen))

        # Set position of the rest of the starting body objects
        for i in range(len(self.body)):
            if i == 0:
                # Set position of the first body part (head)
                self.body[0].rect.x = self.screen_width / 2
                self.body[0].rect.y = self.screen_height / 2
            else:
                self.body[i].rect.x = self.body[i-1].rect.x
                self.body[i].rect.y = self.body[i-1].rect.y + 10

            # Display initial body
            self.screen.blit(self.body[i].image, self.body[i].rect)

    def update_body(self, command):
        """Update position of the snake's body modules"""
        if command != "stop":
            self.screen.fill(self.black)

            # Set offsets for body modules
            for i in range(len(self.body)):
                if i == 0:
                    self.offsets[i] = self.directions[command]
                else:
                    self.offsets[i] = (self.body[i-1].rect.x - self.body[i].rect.x,
                                       self.body[i-1].rect.y - self.body[i].rect.y)

            # Update position of body modules
            for i in range(len(self.body)):
                self.body[i].rect.move_ip(self.offsets[i])
                self.screen.blit(self.body[i].image, self.body[i].rect)
