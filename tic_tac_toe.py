""" The game loop of the tic-tac-toe game
It is required to install pygame to run the game.
it contains the follwoing methods:
    * run() - runs the game
"""
import pygame
from board import Board
from Window import Window


class Game:
    """A class to create tic-tac-toe game


    Attributes
    -----------
    running: bool
    player: int

    Methods
    -----------
    run(self)
        runs the tic-tac-toe game
    """
    def __init__(self):
        self.running = True
        self.player = 1
        pygame.init()

    def run(self):
        """ Runs the tic-tac-toe game """
        window = Window(600, 600)
        main_window = window.get_window()
        board = Board()
        board.draw_lines(main_window)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # The window has an height and width of 600 px;
                    #  each square to mark is 200 px
                    mouse_y = int(event.pos[0] // 200)
                    mouse_x = int(event.pos[1] // 200)


                    if board.check_available(mouse_x, mouse_y) is True:
                        if self.player == 1:
                            board.draw_shape(mouse_x, mouse_y, self.player)
                            if board.mark_board_full(mouse_x, mouse_y):
                                self.running = False
                            mouse_position = pygame.mouse.get_pos()
                            x_pos, y_pos = mouse_position
                            if board.draw_circle(main_window, (0, 255, 0), x_pos, y_pos):
                                if board.check_win(self.player, main_window) is True:
                                    pygame.display.update()
                                    # self.running = False
                                    print(f"Player {self.player} has won the game!")
                            self.player = 2

                        elif self.player == 2:

                            mouse_position = pygame.mouse.get_pos()
                            x_pos, y_pos = mouse_position
                            board.draw_shape(mouse_x, mouse_y, self.player)
                            if board.mark_board_full(mouse_x, mouse_y):
                                self.running = False


                            board.draw_circle(main_window, (255, 0, 0), x_pos, y_pos)
                            if board.check_win(self.player, main_window) is True:
                                pygame.display.update()
                                # self.running = False
                                print(f"Player {self.player} has won the game!")
                            self.player = 1