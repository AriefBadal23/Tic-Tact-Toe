import numpy
import pygame

class Board():
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.board = numpy.zeros((self.rows, self.columns))
        self.color = (255, 255,255)
        self.width = 20


    def draw_shape(self,col, row, player):
        """ Creates the tic tac toe player board with rows and columns 3x3 """
        # Starts with zero so, 0,1,2
        self.board[col][row] = player
        print(self.board)


    def check_available(self, col, row):
        """ Checks if the square is already marked """
        # TODO: kijkt of row en col gelijk is aan 1 ipv kijken naar player
        if self.board[col][row] == 0:
            print(self.board[col][row])
            return True
        else:
            print(self.board[col][row])

            return False


    def draw_lines(self, window):
        """ Draw the lines for the tic tac toe game """
        window.fill((0, 153, 153))
                                            
        pygame.draw.line(window, self.color, (550, 200), (100, 200), self.width)
        pygame.draw.line(window, self.color, (550, 350), (100, 350), self.width)
        
                                    #   color, start-end pos, 
        pygame.draw.line(window, self.color, (400, 500), (400, 50), self.width)
        pygame.draw.line(window, self.color, (220, 500), (220, 50), self.width)
        pygame.display.update()



    # def mark_board_full(self):
    #     for row in self.board:
    #         print(row)


            


        


