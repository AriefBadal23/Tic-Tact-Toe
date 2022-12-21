""" 
    Gameover window for the tic tac toe game
    ----------
    Attributes
    ----------
    self.font: numpy.ndarray obj


 """



""" 
    Game over window which is shown after a player has won the game
    It is required to install pygame to run the game.
    Contains the following methods:
        * draw_text() - draws the text if a player won the game
 """
import pygame
import pygwidgets


class GameOverScreen():
    """ A class to create a GameOverScreen object
         if a player has won the game"""
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 30)

    def show_popup(self, player, window, x_pos, y_pos):
        """ Draws the text for the winning player """
        game_over_text = f"Player {player} won the game!"
        rect = pygame.Rect(100,300,370,100)
        pygame.draw.rect(window, (255, 0,0), rect)
        text = self.font.render(game_over_text, True, (0, 0, 0))
        window.blit(text, (x_pos, y_pos))
        # restart_button = pygwidgets.TextButton(window, (130, 200), "Restart")
        # restart_button.draw()
        pygame.display.update()
        return text
