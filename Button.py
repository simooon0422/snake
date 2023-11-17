import pygame.font
import Label


class Button(Label.Label):
    """Class for creating buttons"""
    def __init__(self, screen, msg, width, height):
        super().__init__(screen, msg, width, height)

    def is_clicked(self, event):
        """Check if user clicked the button"""
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False
