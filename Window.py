import pygame

class Window():
    def __init__(self, width, height):
        self.widht = width
        self.height = height
        self.running = True
        self.color = (0, 153, 153)


    def get_window(self):
        window = pygame.display.set_mode((self.widht, self.height))
        window.fill(self.color)
        return window



