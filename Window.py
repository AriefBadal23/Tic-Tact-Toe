import pygame

class Window():
    def __init__(self, width, height, color):
        self.widht = width
        self.height = height
        self.running = True
        self.color = color


    def get_window(self):
        window = pygame.display.set_mode((self.widht, self.height))
        return window



