import pygame
from Window import Window


class App():
    def __init__(self):
        self.running = True

    def run(self):
        window = Window(600,600, (0,0,0))
        main_window = window.get_window()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if self.running:
                    pygame.display.update()
                    main_window.fill((0,0,0))


