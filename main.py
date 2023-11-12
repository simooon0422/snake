import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.flip()

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
