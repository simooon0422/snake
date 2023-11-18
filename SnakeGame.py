import pygame
import Serpent
import Fruit
import Label
import Button
import time


class SnakeGame:
    """Main game class"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        pygame.display.set_caption("Super Snake")

        # Display parameters
        self.screen = pygame.display.set_mode((500, 550))
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        # Colors
        self.red = (255, 0, 0)
        self.purple = (128, 0, 128)
        self.orange = (255, 165, 0)
        self.black = (0, 0, 0)
        self.gold = (255, 215, 0)

        # Initial snake attributes (snake object initialized in _start() function)
        self.snake_init_length = 3
        self.snake = None
        self.direction = "stop"

        # Store fruits objects
        self.fruits_list = []

        # State of the game (running game or menus)
        self.running_state = 1

        # Score counter
        self.score = 0
        self.score_message = f"Score: {self.score}"
        self.score_label = Label.Label(self.screen, self.score_message, self.screen_width, 50, self.gold)

        # Create button objects used in menus
        self.play_button = Button.Button(self.screen, "Play", 150, 50, self.purple)
        self.quit_button = Button.Button(self.screen, "Quit", 100, 50, self.purple)
        self.game_over_label = Label.Label(self.screen, "Game Over", 200, 50, self.red)
        self.restart_button = Button.Button(self.screen, "Restart", 150, 50, self.purple)
        self.pause_label = Label.Label(self.screen, "Paused", 200, 50, self.orange)
        self.resume_button = Button.Button(self.screen, "Resume", 150, 50, self.purple)

    def run_game(self):
        """Main game loop, Running states of the game:
        0 - game,
        1 - main menu,
        2 - game over screen,
        3 - pause screen"""
        while True:
            self._handle_events()
            pygame.display.flip()
            if self.running_state == 0:
                self._run()
            elif self.running_state == 1:
                self._display_menu("main")
            elif self.running_state == 2:
                self._display_menu("game over")
            elif self.running_state == 3:
                self._display_menu("pause")

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
                elif event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    self.running_state = 3
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.running_state != 0:
                    self._menu_clicks(event)

    def _run(self):
        """Executes functions to play the game"""
        self.screen.fill(self.black)
        self.score_label.draw(0, 0)
        self.snake.update_body(self.direction)
        self._handle_fruits()
        self._handle_collisions()

    def _handle_fruits(self):
        """Function for displaying fruits for snake on the screen"""
        if not self.fruits_list:
            self.fruits_list.append(Fruit.Fruit(self.screen))
        else:
            for i in range(len(self.fruits_list)):
                self.fruits_list[i].update()

    def _handle_collisions(self):
        """Function specifying action after collision of objects"""
        self._handle_fruits_collisions()
        self._handle_game_over_conditions()

    def _handle_fruits_collisions(self):
        """Function handling collisions with fruits"""
        index = self._check_fruits_collisions()
        if index != -1:
            del self.fruits_list[index]
            self._increase_score()
            self.snake.grow()

    def _check_fruits_collisions(self):
        """Function checking if head collides with any fruit"""
        for i in range(len(self.fruits_list)):
            if pygame.Rect.colliderect(self.snake.head.rect, self.fruits_list[i].rect):
                return i
        return -1

    def _increase_score(self):
        """Increase score counter and update text of label"""
        self.score += 1
        self.score_message = self.score_message = f"Score: {self.score}"
        self.score_label._prep_msg(self.score_message)

    def _reset_score(self):
        self.score = 0
        self.score_message = self.score_message = f"Score: {self.score}"
        self.score_label._prep_msg(self.score_message)

    def _handle_game_over_conditions(self):
        """Function handling collisions causing game over"""
        if self._check_game_over_collisions():
            self.running_state = 2

    def _check_game_over_collisions(self):
        """Function checking game over conditions"""
        for i in range(1, len(self.snake.body)):
            if pygame.Rect.colliderect(self.snake.head.rect, self.snake.body[i].rect):
                return True
        if self.snake.head.rect.x > self.screen_width - self.snake.size[0] or self.snake.head.rect.x < 0:
            return True
        elif self.snake.head.rect.y > self.screen_height - self.snake.size[1] or self.snake.head.rect.y < 50:
            return True
        else:
            return False

    def _display_menu(self, menu_type):
        """Displays menus of the game"""
        self._hide_buttons()
        if menu_type == "main":
            self.play_button.draw(175, 200)
        elif menu_type == "game over":
            self.game_over_label.draw(150, 100)
            self.restart_button.draw(175, 250)
        elif menu_type == "pause":
            self.pause_label.draw(150, 100)
            self.resume_button.draw(175, 200)
            self.restart_button.draw(175, 275)

        self.quit_button.draw(200, 350)

    def _hide_buttons(self):
        """Hide buttons outside the screen to prevent overlapping on menu change"""
        hide_x = -500
        hide_y = -500
        self.play_button.draw(hide_x, hide_y)
        self.restart_button.draw(hide_x, hide_y)
        self.resume_button.draw(hide_x, hide_y)
        self.quit_button.draw(hide_x, hide_y)

    def _menu_clicks(self, event):
        """Handle clicking on menu buttons"""
        if self.play_button.is_clicked(event) and self.running_state == 1:
            self._start()
        elif self.resume_button.is_clicked(event) and self.running_state == 3:
            self._resume()
        elif self.restart_button.is_clicked(event) and (self.running_state == 2 or self.running_state == 3):
            self._restart()
        elif self.quit_button.is_clicked(event):
            pygame.quit()

    def _start(self):
        """Creates the snake and starts the game"""
        self.running_state = 0
        self.screen.fill(self.black)
        self.snake = Serpent.Serpent(self.screen, self.snake_init_length)

    def _restart(self):
        """Deletes current snake and fruits and creates them once again"""
        del self.snake
        for i in range(len(self.fruits_list)):
            del self.fruits_list[i]
        self._reset_score()
        self.direction = "stop"
        self._start()

    def _resume(self):
        """Resume game from pause"""
        self.running_state = 0
