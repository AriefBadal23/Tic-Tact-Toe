import pygame

class GameOverScreen():
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
    
    def draw_text(self, screen, text, x, y):
        text = self.font.render(text, True, (0,0,0))
        screen.blit(text,(x, y))
        pygame.display.update()
        return text
        
