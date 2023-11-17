import pygame.font


class Label:
    """Class for creating and displaying labels with text"""
    def __init__(self, screen, msg, width, height, color):
        """Initialization of label's attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Size and properties of the button
        self.width, self.height = width, height
        self.color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create rectangle of the button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Button's text
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Generate text on the button and center it"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self, x_pos, y_pos):
        """Display the button"""
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.msg_image_rect.center = self.rect.center
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
