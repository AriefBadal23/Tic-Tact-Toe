""" The game loop of the tic-tac-toe game
It is required to install pygame to run the game.
it contains the follwoing methods:
    * run() - runs the game
"""
import pygame

from board import Board
from game_over_screen import GameOverScreen
from window import Window
import pickle
import socket
import threading
import pickle
from _thread import start_new_thread


class Network():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.PORT_NUMBER = 12345
        self.client_id = 0

    def connect_to_server(self):
        self.client_socket.connect((self.IP_ADDRESS, self.PORT_NUMBER))

    def send_pos(self, x_pos, y_pos):
            message = pickle.dumps([x_pos, y_pos])
            print(pickle.loads(message))
            # print(str(message))

            self.client_socket.send(message)
            print(f'sent: {message}')
            return message
    
    def parse_player_pos(self):
        # received_pos is in positions ipv bytes!
        received_pos = pickle.loads(self.client_socket.recv(1024))
        print(f'Parsed player pos now:{received_pos}')
        return received_pos
    

    

class Game():
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

    positions = []

    def __init__(self):
        self.__running = True
        self.__player = 0
        self.game_network = Network()
        self.is_player_1_turn = False
        self.is_player_2_turn = False
        self.player_2 = 2
        pygame.init()
    
    def get_pos(self, obj):
        Game.positions.append(obj)
        # print(Game.positions)
        return Game.positions

    def set_players(self):
        get_players = self.game_network.client_socket.recv(1024)
        return get_players
    
    def get_updated_pos(self, pos):
        pass




    def run(self):
        """Runs the tic-tac-toe game"""
        window = Window(600, 600)
        main_window = window.get_window()
        game_over_screen = GameOverScreen()
        board = Board()
        board.draw_lines(main_window)
        self.game_network.connect_to_server()
        # start_new_thread
        self.game_network.client_socket.recv(1024)
        new_playsers = self.set_players()

        if new_playsers:
            players = pickle.loads(new_playsers)
            joined_players = []
            joined_players.append(players)
            # available_players.append(recv_player)
            for player in joined_players:
                print(f'Received player:{player[0]}')
                if player[0]["player"] == 1 and player[0]["CAN_PLAY"] == True:
                    self.__player = 1
                    self.is_player_1_turn = True

                else:
                    self.player_2 = 2
        
                     


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
                        if self.__player == 1 and self.is_player_1_turn:
                            board.draw_game_board(mouse_x, mouse_y, self.__player)
                            if board._Board__mark_board_full(mouse_x, mouse_y):
                                self.__running = False

                            mouse_position = pygame.mouse.get_pos()
                            x_pos, y_pos = mouse_position


                            if board.draw_circle(main_window, (0, 255, 0), x_pos, y_pos):


                                if (board._Board__check_win(self.__player, main_window) is True):
                                    pygame.display.update()
                                    game_over_screen.show_popup(self.__player, main_window, 150, 300)
                                    # time.sleep(5)
                                    # self.running = False
                            print(f'Value: {self.player_2}')
                            self.is_player_1_turn = False
                            self.is_player_2_turn = True
                            self.game_network.send_pos(x_pos, y_pos)


                        elif self.player_2 == 2 and self.is_player_2_turn == True:
                            # mouse_x and mouse_y = uses the 3x3 raster
                            # and x_pos and y_post uses
                            # the real mouse position
                            mouse_position = pygame.mouse.get_pos()
                            x_pos, y_pos = mouse_position

                            board.draw_circle(main_window, (255, 0, 0), x_pos, y_pos)
                            if (board._Board__check_win(self.__player, main_window) is True):
                                pygame.display.update()
                                game_over_screen.show_popup(self.__player, main_window, 200, 300)
                                # time.sleep(5)
                                # self.running = False
                            self.is_player_2_turn = False
                            self.is_player_1_turn = True
                            self.__player = 1
                            self.game_network.send_pos(x_pos, y_pos)
                        start_new_thread(self.game_network.parse_player_pos, ())

                        # self.game_network.parse_player_pos()

                        