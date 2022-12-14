""" Window for the pygame application
    It is required to install the pygame library to run it
    It contains the following methods:
        * get_window()
 """
import pygame


class Window():
    """ Class to create a Window object for the pygame application

        Attributes
        -----------
        width: int
        height: int

        Methods
        -------
        get_window(self)
            Retrieves the pygame window
     """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (0, 153, 153)

    def get_window(self):
        """ Retrieves the pygame window """
        window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic-Tac-Toe")
        
        window.fill(self.color)
        return window
