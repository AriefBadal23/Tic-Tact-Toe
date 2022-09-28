import pygame
from Window import Window

class Game():
    def __init__(self):
        self.running = True
        pygame.init()


    def run(self):
        window = Window(600,600, (0, 153, 153))
        main_window = window.get_window()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if self.running:
                    main_window.fill((0, 153, 153))
                    pygame.draw.line(main_window, (255,255,255), (550, 200), (100, 200), 20)
                    pygame.draw.line(main_window, (255,255,255), (550, 350), (100, 350), 20)
                    
                                                #   color, start-end pos, 
                    pygame.draw.line(main_window, (255,255,255), (400, 500), (400, 50), 20)
                    pygame.draw.line(main_window, (255,255,), (220, 500), (220, 50), 20)


                    pygame.display.update()


