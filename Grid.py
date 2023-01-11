import pygame
import numpy
import os

letter_X = pygame.image.load(os.path.join('img', 'circle.png'))
letter_O = pygame.image.load(os.path.join('img', 'cross.png'))


class Grid():
    def __init__(self):
        self.grid_lines = [((0, 200), (600, 200)),
                            ((0, 400), (600, 400)),
                            ((200, 0), (200, 600)), 
                            ((400, 0), (400, 600))]
        self.board = [[0 for x in range(3)] for y in range(3)]
    
    def print_grid(self):
        """ Printing the grid of the game (only for debugging) """
        for pos in self.board:
            print(pos)

    def get_cell_value(self, pos_x, pos_y):
        """ Getter method to retrieve the row and column of the value """
        return self.board[pos_x][pos_y]
    
    def set_cell_value(self, pos_x, pos_y, value):
        self.board[pos_x][pos_y] = value


    def draw(self, surface):
        "Draw method to draw the grid of the board"
        for line in self.grid_lines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.get_cell_value(x, y) == 'X':
                    surface.blit(letter_X, (x*200, y*200))

                elif self.get_cell_value(x, y) == 'O':
                    surface.blit(letter_O, (x*200, y*200))
            


    def get_mouse(self, x, y, player):
        """ Retreive the mouse positions with the right player """
        if player == "X":
            self.set_cell_value(x, y, "X")
        elif player == "O":
            self.set_cell_value(x, y, "O")