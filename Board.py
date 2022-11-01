import numpy
import pygame

class Board():
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.board = numpy.zeros((self.rows, self.columns))
        self.color = (255, 255,255)
        self.SQUARE_WIDTH = 200
        self.line_width = 20
        self.WIDTH = 600
        self.line_color = (255,255,255)


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
        """ Draw the horizontal and vertical lines for the tic tac toe game """                                            
        pygame.draw.line(window, self.color, (self.SQUARE_WIDTH, 0), (self.SQUARE_WIDTH, 600), self.line_width)
        pygame.draw.line(window, self.color, (self.SQUARE_WIDTH*2, 0), (self.SQUARE_WIDTH*2, 600), self.line_width)

                                    #   color, start-end pos, 
                                    # x,y, x, y
        pygame.draw.line(window, self.color, (0, self.SQUARE_WIDTH), (self.WIDTH, self.SQUARE_WIDTH), self.line_width)
        pygame.draw.line(window, self.color, (0, self.SQUARE_WIDTH *2), (self.WIDTH , self.SQUARE_WIDTH *2), self.line_width)
        pygame.display.update()


    def draw_horizontal_winning_line(self, window, col):
        """ Draws hortizontal winning line """
        pos_y = col * 200 + 100
        pygame.draw.line(window, (255, 0,0), (15, pos_y), (self.WIDTH - 15, pos_y), 15)
        pygame.display.update()
        True


    def draw_vertical_winning_line(self, window, row):
        """ Draws the vertical winning line """
        pos_x = row * 200 + 100
        pygame.draw.line(window, (self.line_color), (pos_x, 25), (pos_x, self.WIDTH - 15), 15)
        pygame.display.update()
        return True

    def draw_left_diagonal_winning_line(self, window, row):
        pos_x = row * 200 + 100
        pygame.draw.line(window, (self.line_color), (90, 25), (pos_x, self.WIDTH - 15), 15)
        pygame.display.update()
        return True

    def draw_diagonal_winning_line_2(self, window, row):
        pos_x = row * 200 + 100
        pygame.draw.line(window, (self.line_color), (self.WIDTH -100, 90), (100, self.WIDTH), 15)
        pygame.display.update()
        return True



    def check_win(self, player, window):
        for col in range(self.columns):
            if self.board[col][0] == player and self.board[col][1] == player and self.board[col][2] == player:
                self.draw_horizontal_winning_line(window, col)
                return True


        for row in range(self.rows):
            if self.board[0][row] == player and self.board[1][row] == player and self.board[2][row] == player:
                self.draw_vertical_winning_line(window, row)
                return True

        if self.board[0][0] == player and self.board[1][1] and self.board[2][2]:
            print('Diagonal win!')
            self.draw_left_diagonal_winning_line(window, row)
        
        elif self.board[2][0] == player and self.board[1][1] == player and self.board[0][2]:
            self.draw_diagonal_winning_line_2(window, row)
            print('Other diagonal!!')

    
    # def mark_board_full(self):
    #     for row in self.board:
    #         print(row)


            


        


