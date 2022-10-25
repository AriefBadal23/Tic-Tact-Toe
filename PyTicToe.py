import pygame
from Board import Board
from Window import Window

class Game():
    def __init__(self):
        self.running = True
        self.player = 1
        pygame.init()


    def run(self):
        window = Window(600,600)
        main_window = window.get_window()
        board = Board()
        board.draw_lines(main_window)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # The window has an height and width of 600 px; each square to mark is 200 px
                    mouse_y = int(event.pos[0] // 200)
                    mouse_x = int(event.pos[1] // 200)
                    # print(mouse_x, mouse_y)
                    board.check_available(mouse_x, mouse_y)
                    if self.player == 1:
                        board.draw_shape(mouse_x , mouse_y, self.player)
                        mouse_position = pygame.mouse.get_pos()
                        x, y = mouse_position
                        # TODO: circle draws but disappears
                        board.draw_circle(main_window,(0,255,0), x, y)
                        pygame.display.update()   
                        self.player = 2
                        
                    elif self.player == 2:
                        mouse_position = pygame.mouse.get_pos()
                        x, y = mouse_position
                        board.draw_shape(mouse_x, mouse_y, self.player)
                        board.draw_circle(main_window,(255,0,0), x, y)
                        pygame.display.update()   
                        self.player = 1










