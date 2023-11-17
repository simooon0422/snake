import pygame.font


class Button:

    def __init__(self, screen, msg, width, height):
        """Initialization of button's attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Size and properties of the button
        self.width, self.height = width, height
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create rectangle of the button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Button's text
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Generate text on the button and center it"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, x_pos, y_pos):
        """Display the button"""
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.msg_image_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def is_clicked(self, event):
        """Check if user clicked the button"""
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False
