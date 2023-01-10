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

    # create new methods for the client side how to handle new sended data





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
        self.game_network = Network()
        pygame.init()
    
    def run(self):
        """Runs the tic-tac-toe game"""
        window = Window(600, 600)
        main_window = window.get_window()
        game_over_screen = GameOverScreen()
        board = Board()
        board.draw_lines(main_window)
        self.game_network.connect_to_server()

        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                   pass
                # rewrite the logic for the entire game
                   



                        