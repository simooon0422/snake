import pygame
import Serpent
import Fruit
import Button
import time
import random


class SnakeGame:
    """Main game class"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        pygame.display.set_caption("Super Snake")
        self.screen = pygame.display.set_mode((500, 500))
        self.snake = Serpent.Serpent(self.screen)
        self.direction = "stop"

        self.fruits_list = []
        self.fruits_position = []

        self.running_state = 0

        # Create button objects used in menus
        self.play_button = Button.Button(self.screen, "Play", 100, 50, 200, 150)
        self.quit_button = Button.Button(self.screen, "Quit", 100, 50, 200, 350)
        self.game_over_label = Button.Button(self.screen, "Game Over", 100, 50, 200, 150)
        self.restart_button = Button.Button(self.screen, "Restart", 100, 50, 200, 250)
        self.pause_label = Button.Button(self.screen, "Pause", 100, 50, 200, 100)
        self.resume_button = Button.Button(self.screen, "Resume", 100, 50, 200, 150)

    def run_game(self):
        """Main game loop, Running states of the game:
        0 - main menu,
        1 - game,
        2 - game over screen,
        3 - pause screen"""
        while True:
            self._handle_events()
            pygame.display.flip()
            if self.running_state == 0:
                self._display_menu("main")
            elif self.running_state == 1:
                self.snake.update_body(self.direction)
                self._handle_fruits()
                self._handle_collisions()
            elif self.running_state == 2:
                self._display_menu("game over")

            time.sleep(0.1)  # delay for snake's movement

    def _handle_events(self):
        """Function to handle pressing keys and clicking"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = "right"
                elif event.key == pygame.K_LEFT:
                    self.direction = "left"
                elif event.key == pygame.K_UP:
                    self.direction = "up"
                elif event.key == pygame.K_DOWN:
                    self.direction = "down"
                elif event.key == pygame.K_p:
                    self.running_state = 3
                    self._display_menu("pause")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._menu_clicks(pygame.mouse.get_pos())

    def _handle_fruits(self):
        """Function for displaying fruits for snake on the screen"""
        if not self.fruits_list:
            self.fruits_list.append(Fruit.Fruit(self.screen))
            self.fruits_position.append((random.randrange(200, 400, 10), random.randrange(200, 400, 10)))
        else:
            self.fruits_list[0].update(self.fruits_position[0][0], self.fruits_position[0][1])

    def _handle_collisions(self):
        """Function specifying action after collision of objects"""
        self._check_fruits_collisions()
        self._check_game_over_collisions()

    def _check_fruits_collisions(self):
        """Function handling collisions with fruits"""
        for i in range(len(self.fruits_list)):
            if pygame.Rect.colliderect(self.snake.body[0].rect, self.fruits_list[0].rect):
                del self.fruits_list[i]
                self.fruits_position.pop(i)
                self.snake.grow()
                self.snake.grow()
                self.snake.grow()
                self.snake.grow()
                self.snake.grow()
                print("Eat apple")

    def _check_game_over_collisions(self):
        """Function handling collisions causing game over"""
        if self._is_game_over():
            self.running_state = 2
            print("Game Over")

    def _is_game_over(self):
        """Function checking game over conditions"""
        for i in range(1, len(self.snake.body)):
            if pygame.Rect.colliderect(self.snake.body[0].rect, self.snake.body[i].rect):
                return True
        if self.snake.body[0].rect.x > 500 - self.snake.size[0] or self.snake.body[0].rect.x < 0:
            return True
        elif self.snake.body[0].rect.y > 500 - self.snake.size[1] or self.snake.body[0].rect.y < 0:
            return True
        else:
            return False

    def _display_menu(self, menu_type):
        """Function displaying main menu of the game"""
        if menu_type == "main":
            self.play_button.draw_button()
            self.quit_button.draw_button()
        elif menu_type == "game over":
            self.game_over_label.draw_button()
            self.restart_button.draw_button()
            self.quit_button.draw_button()
        elif menu_type == "pause":
            self.pause_label.draw_button()
            self.resume_button.draw_button()
            self.restart_button.draw_button()
            self.quit_button.draw_button()

    def _menu_clicks(self, mouse_pos):
        """Handle clicking on menu buttons"""
        if self.running_state == 0:
            if self.play_button.rect.collidepoint(mouse_pos):
                self._start()
            elif self.quit_button.rect.collidepoint(mouse_pos):
                pygame.quit()

        elif self.running_state == 2:
            if self.restart_button.rect.collidepoint(mouse_pos):
                self._restart()
            elif self.quit_button.rect.collidepoint(mouse_pos):
                pygame.quit()

        elif self.running_state == 3:
            if self.restart_button.rect.collidepoint(mouse_pos):
                self._restart()
            elif self.resume_button.rect.collidepoint(mouse_pos):
                self._resume()
            elif self.quit_button.rect.collidepoint(mouse_pos):
                pygame.quit()

    def _start(self):
        """Creates the snake and starts the game"""
        self.running_state = 1
        self.screen.fill((0, 0, 0))
        self.snake.create_body()

    def _restart(self):
        """Deletes current snake and fruits and creates them once again"""
        del self.snake
        del self.fruits_list[0]
        self.fruits_position.pop(0)
        self.running_state = 1
        self.screen.fill((0, 0, 0))
        self.snake = Serpent.Serpent(self.screen)
        self.direction = "stop"
        self.snake.create_body()

    def _resume(self):
        """Resume game from pause"""
        self.running_state = 1
