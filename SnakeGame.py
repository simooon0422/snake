import pygame


class SnakeGame:
    """Main game class"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def run_game(self):
        """Main game loop"""
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
