import pygame
from Board import Board
from Window import Window

class Game():
    def __init__(self):
        self.running = True
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
                        
                        # if board.check_available(mouse_y, mouse_x) == True:
                        #     player = 1
                        #     if player == 1:
                        #         board.draw_shape(mouse_x, mouse_y, player)
                        #     player = 2
                        #         # print(f'Player: {player} is aan de beurt')
                            
                        #     if player == 2:
                        #         board.draw_shape(mouse_x, mouse_y, player)
                        #     player = 1
                        #             # print(f'Player: {player} is aan de beurt')









