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
        if self.board[col][row] == 0:
            return True
        else:
            return False

    def draw_circle(self, window, color, x, y):
        circle = pygame.draw.circle(window, color, (x, y),50, 10)
        pygame.display.update()
        return circle

    def draw_lines(self, window):
        """ Draw the lines for the tic tac toe game """                                            
        pygame.draw.line(window, self.color, (550, 200), (100, 200), self.width)
        pygame.draw.line(window, self.color, (550, 350), (100, 350), self.width)
        
                                    #   color, start-end pos, 
        pygame.draw.line(window, self.color, (400, 500), (400, 50), self.width)
        pygame.draw.line(window, self.color, (220, 500), (220, 50), self.width)
        pygame.display.update()


    def draw_vertical_winning_line(self, window):
        pygame.draw.line(window, (255, 0,0), (100,100),(400,400), self.width)
        pygame.display.update()

    def check_win(self, player, window):
        for col in range(self.columns):
            if self.board[col][0] == player and self.board[col][1] == player and self.board[col][2] == player:
                self.draw_vertical_winning_line(window)


        for row in range(self.rows):
            if self.board[0][row] == player and self.board[1][row] == player and self.board[2][row] == player:
                print(True)

    
    # def mark_board_full(self):
    #     for row in self.board:
    #         print(row)


            


        


