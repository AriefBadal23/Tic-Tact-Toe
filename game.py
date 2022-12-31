""" The game loop of the tic-tac-toe game
It is required to install pygame to run the game.
it contains the follwoing methods:
    * run() - runs the game
"""
import time

import pygame

from board import Board
from game_over_screen import GameOverScreen
from window import Window


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
        self.__running = True
        self.__current_player = 1
        self.__p2 = 0
        self.joined_players = []
        self.player_positions = []
        pygame.init()

    def set_player(self, player_list: list) -> list:
        """ Stores the players that has been connected to the server """
        if '1' in str(player_list):
            global player_1
            player_1 = player_list[0]
            self.__current_player = player_1
            self.joined_players.append(self.__current_player)
            print(len(self.joined_players))

            
        if '2' in str(player_list):
            global player_2
            player_2 = player_list[1]
            self.__p2 = player_2
            self.joined_players.append(self.__p2)
            print(len(self.joined_players))

        else:
            False

    def get_player(self, playerlist):
        """ retrieves the current player which has joined """
        player = self.set_player(playerlist)
        return player

    def get_positions(self, player, position):
        """ Retrieves the positions of the players """
        self.player_positions.append({str(player): position})
        print(self.player_positions)
        return self.player_positions

    def run(self):
        """Runs the tic-tac-toe game"""
        window = Window(600, 600)
        main_window = window.get_window()
        game_over_screen = GameOverScreen()
        board = Board()
        board.draw_lines(main_window)

        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # The window has an height and width of 600 px;
                    #  each square to mark is 200 px
                    mouse_y = int(event.pos[0] // 200)
                    mouse_x = int(event.pos[1] // 200)

                    if board._Board__check_available_square(mouse_x, mouse_y) is True:
                        if self.__player == 1:
                            board.draw_shape(mouse_x, mouse_y, self.__player)
                            if board._Board__mark_board_full(mouse_x, mouse_y):
                                self.__running = False
                            mouse_position = pygame.mouse.get_pos()
                            x_pos, y_pos = mouse_position
                            if board.draw_circle(
                                main_window, (0, 255, 0), x_pos, y_pos
                            ):
                                if (
                                    board._Board__check_win(self.__player, main_window)
                                    is True
                                ):
                                    pygame.display.update()
                                    game_over_screen.show_popup(
                                        self.__player, main_window, 150, 300
                                    )
                                    # time.sleep(5)
                                    # self.running = False
                            self.__player = 2

                        elif self.__player == 2:
                            # mouse_x and mouse_y = uses the 3x3 raster
                            # and x_pos and y_post uses
                            # the real mouse position

                            mouse_position = pygame.mouse.get_pos()
                            x_pos, y_pos = mouse_position
                            board.draw_shape(mouse_x, mouse_y, self.__player)
                            board.draw_circle(main_window, (255, 0, 0), x_pos, y_pos)
                            if (
                                board._Board__check_win(self.__player, main_window)
                                is True
                            ):
                                pygame.display.update()
                                game_over_screen.show_popup(
                                    self.__player, main_window, 200, 300
                                )
                                # time.sleep(5)
                                # self.running = False
                            self.__player = 1
