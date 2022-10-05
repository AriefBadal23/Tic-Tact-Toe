import pygame
from Board import Board
from Window import Window

class Game():
    def __init__(self):
        self.running = True
        self.player = 1
        pygame.init()


    def run(self):
        window = Window(600,600, (0, 153, 153))
        main_window = window.get_window()
        board = Board()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if self.running:
                    board.draw_lines(main_window)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # TODO: self.board blijft op 0,0,0 ??? hoe te fixen?
                        # Bepaalde square geeft False terug en klik verander niet naar --> 2
                        # The window has an height and width of 600 px; each square to mark is 200 px
                        mouse_y = int(event.pos[0] // 200)
                        mouse_x = int(event.pos[1] // 200)
                        # TODO: player does not change if one player has already marked a spot

                        if board.check_available(mouse_x, mouse_y):
                            if self.player == 1:
                                board.draw_shape(mouse_x, mouse_y, self.player)
                                self.player = 2
                            elif self.player == 2:
                                board.draw_shape(mouse_x, mouse_y, self.player)
                                self.player = 1
                                









