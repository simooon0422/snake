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

        # Size of one body module
        self.size = [10, 10]

        # Store objects forming snake's body
        self.body = []

        # Store offsets to new positions
        self.offsets = [(0, 0)] * self.initial_length

        # Directions of moving
        self.directions = {"left": (-self.size[0], 0),
                           "right": (self.size[0], 0),
                           "down": (0, self.size[1]),
                           "up": (0, -self.size[1]),
                           "stop": (0, 0)}

        # Store current direction
        self.current_direction = "stop"

        # Create initial body
        self._create_body()

        # Store current and previous last body module's coordinates
        self.last_module_x = [self.body[-1].rect.x, 0]
        self.last_module_y = [self.body[-1].rect.y, 0]

    def _create_body(self):
        """Create initial body of the snake"""
        # Fill list with body objects
        for i in range(self.initial_length):
            self.body.append(BodyModule.BodyModule(self.screen, self.size))

        # Set position of the starting body objects
        for i in range(len(self.body)):
            if i == 0:
                # Set position of the first body part (head)
                self.body[0].rect.x = self.screen_width / 2
                self.body[0].rect.y = self.screen_height / 2
            else:
                self.body[i].rect.x = self.body[i-1].rect.x
                self.body[i].rect.y = self.body[i-1].rect.y + self.size[1]

            # Display initial body
            self.screen.blit(self.body[i].image, self.body[i].rect)

    def update_body(self, command):
        """Update position of the snake's body modules"""
        if command != "stop":
            if command != self._get_opposite_direction(self.current_direction):
                self.current_direction = command

            self.screen.fill(self.black)
            self._set_offsets(self.current_direction)
            self._update_positions()
            self._update_last_module_position()

    def _set_offsets(self, command):
        """Set offsets for body modules"""
        for i in range(len(self.body)):
            if i == 0:
                self.offsets[i] = self.directions[command]
            else:
                self.offsets[i] = (self.body[i - 1].rect.x - self.body[i].rect.x,
                                   self.body[i - 1].rect.y - self.body[i].rect.y)

    def _update_positions(self):
        """Move and display body modules"""
        for i in range(len(self.body)):
            self.body[i].update(self.offsets[i])

    def _update_last_module_position(self):
        self.last_module_x[1] = self.last_module_x[0]
        self.last_module_y[1] = self.last_module_y[0]
        self.last_module_x[0] = self.body[-1].rect.x
        self.last_module_y[0] = self.body[-1].rect.y

    def _get_opposite_direction(self, direction):
        """Return direction opposite to the current direction"""
        if direction == "left":
            return "right"
        elif direction == "right":
            return "left"
        elif direction == "up":
            return "down"
        elif direction == "down":
            return "up"
        else:
            return "no direction"

    def grow(self):
        """Increase length of snake by 1 module"""
        grow_direction = self._get_grow_direction()
        self.body.append(BodyModule.BodyModule(self.screen, self.size))
        self.offsets.append((0, 0))

        self.body[-1].rect.x = self.body[-2].rect.x + grow_direction[0]
        self.body[-1].rect.y = self.body[-2].rect.y + grow_direction[1]

    def _get_grow_direction(self):
        """Function for specifying snake grow directions"""
        x = self.last_module_x[0] - self.last_module_x[1]
        y = self.last_module_y[0] - self.last_module_y[1]

        if x == 0 and y < 0:
            return self.directions["down"]
        elif x == 0 and y > 0:
            return self.directions["up"]
        elif x < 0 and y == 0:
            return self.directions["right"]
        elif x > 0 and y == 0:
            return self.directions["left"]
