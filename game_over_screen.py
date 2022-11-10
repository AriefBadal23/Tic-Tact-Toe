import pygame

class GameOverScreen():
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
        # self.screen = screen
    
    def draw_text(self, player, window, x, y):
        game_over_text = f"Player {player} has won the game"
        text = self.font.render(game_over_text, True, (0,0,0))
        window.blit(text,(x, y))
        pygame.display.update()
        return text

    # def draw_rectangle(self, window, color):
    #     rect = pygame.Rect((200,200), (20,20))
    #     return pygame.draw.rect(window, color, rect)
        