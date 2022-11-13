""" 
    Game over window which is shown after a player has won the game
    It is required to install pygame to run the game.
    Contains the following methods:
        * draw_text() - draws the text if a player won the game
 """
import pygame


class GameOverScreen():
    """ A class to create a GameOverScreen object
         if a player has won the game"""
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 30)

    def draw_text(self, player, window, x_pos, y_pos):
        """ Draws the text for the winning player """
        game_over_text = f"Player {player} has won the game!"
        text = self.font.render(game_over_text, True, (0, 0, 0))
        window.blit(text, (x_pos, y_pos))
        pygame.display.update()
        return text
