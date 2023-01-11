""" 
    The tic-tac-toe game board to play tic tac toe
    
    ----------
    Attributes
    ----------
    rows : int
    columns: int
    self.__board: numpy.ndarray obj
    self.color: tupl
    self.square_width: int
    self.line_width: int
    self.width: int
    self.line_color: tupl
    Methods
    ------
    draw_shape(col=int, row=int, player=int)
        draws the players move on the tic tac toe board
    
    __check_available_square(col=int, row=int)
        checks if the selected square is available to be marked
    
    draw_circle(window = window, color = tupl, x= int, y=int)
        Draws the circle for the player
    draw_lines(window= window)
        draws the line that makes it a 3x3 grid
    
    __draw_horizontal_winning_line(window= Window obj, col=int)
        draws a horizontal winning line
    __draw_diagonal_winning_line_2(window = Window obj, row= int)
        draws a diagonal_line for the ... side
    __draw_vertical_winning_line(window = Window obj, row= int)
        draws a vertical line
    
    __draw_left_diagonal_winning_line(window = Window obj, row=int)
        draws the left diagnal winning line
    __draw_diagonal_winning_line_2(window = Window obj, row = int)
        draws the diagnal winning_line from the right corner
    __check_win(player = int, window = Window obj)
        Checks if a player has won the game
    __mark_board_full(row = int, col = int)
        Marks the board full if no the grid is full
 """
import numpy
import pygame


class Board:
    """A class to create the tic-tac-toe play board"""

    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.__board = numpy.zeros((self.rows, self.columns))
        self.color = (255, 255, 255)
        self.square_width = 200
        self.line_width = 20
        self.width = 600
        self.line_color = (255, 255, 255)
        print(self.__board)
        
    
    def get_board(self):
        return self.__board

    def draw_shape(self, col, row, player):
        """Creates the tic tac toe player board with rows and columns 3x3
            Parameters
            ----------
            col : int
                column to draw the shape
            row : int
                row to draw the shape
            player : int
                player which draw the shape
        """
        # Starts with zero so, 0,1,2
        game_board = self.get_board()
        game_board[col][row] = player
        # self.__board[col][row] = player
        # print(self.board)

    def __check_available_square(self, col, row):
        """Checks if the square is already marked
            Parameters
            ----------
            col : int
                Marked column to check if available
            row : int
                Marked row to check if available
        """
        if self.__board[col][row] == 0:
            return True
        elif self.__board[col][row] == 1 or self.__board[col][row] == 2:
            return False

    def draw_circle(self, window, color, x, y):
        """Draws a circle on the surface
           window : Window object
            window where the shape will be drawn on
           color : tuple
            tuple to pass the rgb values for the color
           x : int
            x value to draw the circle
           y: int
            y value to draw the circle
           
        """
        circle = pygame.draw.circle(window, color, (x, y), 50, 10)
        pygame.display.update()
        print(self.__board)
        return circle

    def draw_lines(self, window):
        """Draw the horizontal and vertical lines for the tic tac toe game
           window : Window object
            window where the shape will be drawn on
        """
        pygame.draw.line(
            window,
            self.color,
            (self.square_width, 0),
            (self.square_width, 600),
            self.line_width,
        )
        pygame.draw.line(
            window,
            self.color,
            (self.square_width * 2, 0),
            (self.square_width * 2, 600),
            self.line_width,
        )

        # color, start-end pos
        # x,y, x, y
        pygame.draw.line(
            window,
            self.color,
            (0, self.square_width),
            (self.width, self.square_width),
            self.line_width,
        )

        pygame.draw.line(
            window,
            self.color,
            (0, self.square_width * 2),
            (self.width, self.square_width * 2),
            self.line_width,
        )
        pygame.display.update()

    def __draw_horizontal_winning_line(self, window, col):
        """Draws hortizontal winning line
            window: Window object
                window where the shape will be drawn on
            col: int
                columns to draw the horizontal winning line
        """
        pos_y = col * 200 + 100
        pygame.draw.line(window, (255, 0, 0), (15, pos_y), (self.width - 15, pos_y), 15)
        pygame.display.update()
        return True

    def __draw_vertical_winning_line(self, window, row):
        """Draws the vertical winning line
           window: Window object
                window where the shape will be drawn on
            row: int
                rows to draw the vertical winning line
        
        """
        pos_x = row * 200 + 100
        pygame.draw.line(
            window, (self.line_color), (pos_x, 25), (pos_x, self.width - 15), 15
        )
        pygame.display.update()
        return True

    def __draw_left_diagonal_winning_line(self, window, row):
        """Draw the left diagnal winning line
            window: Window object
                window where the shape will be drawn on
            row: int
                rows to draw the left diagonal winning line
        """
        pos_x = row * 200 + 100
        pygame.draw.line(
            window, (self.line_color), (90, 25), (pos_x, self.width - 15), 15
        )
        pygame.display.update()
        return True

    def __draw_diagonal_winning_line_2(self, window):
        """Draw the right diagnal winning line
           window: Window object
                window where the shape will be drawn on    
        """
        pygame.draw.line(
            window, (self.line_color), (self.width - 100, 90), (100, self.width), 15
        )
        pygame.display.update()
        return True

    def __check_win(self, player, window):
        """Method which checks if the player has won
            player: int
                Player who wins the game
            window: Window object
                window where the shape will be drawn on   
            
        """
        for col in range(self.columns):
            if (
                self.__board[col][0] == player
                and self.__board[col][1] == player
                and self.__board[col][2] == player
            ):
                self.__draw_horizontal_winning_line(window, col)
                return True

        for row in range(self.rows):
            if (
                self.__board[0][row] == player
                and self.__board[1][row] == player
                and self.__board[2][row] == player
            ):
                self.__draw_vertical_winning_line(window, row)
                return True

        # check diagnal win
        if (
            self.__board[0][0] == player
            and self.__board[1][1] == player
            and self.__board[2][2] == player
        ):
            self.__draw_left_diagonal_winning_line(window, row)
            return True

        elif (
            self.__board[2][0] == player
            and self.__board[1][1] == player
            and self.__board[0][2] == player
        ):
            self.__draw_diagonal_winning_line_2(window)
            return True

    def __mark_board_full(self, row, col):
        """ Checks if the 3x3 grid is full 
            row: int
                rows to check if they are full
            col: int
                columns to check if they are full
        """
        marked_spots = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if self.__board[col][row] == 1 or self.__board[col][row] == 2:
                    marked_spots += 1
                    # print(marked_spots)
                    if marked_spots == 9:
                        print("All spotts have been marked!")
                        return True