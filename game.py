""" The game loop of the tic-tac-toe game
It is required to install pygame to run the game.
it contains the follwoing methods:
    * run() - runs the game
"""

import pygame

from Window import Window
from Grid import Grid


def run():
    """Runs the tic-tac-toe game"""
    window = Window(600, 600)
    main_window = window.get_window()
    grid = Grid()
    player = "X"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    pos = pygame.mouse.get_pos()
                    grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                    # if player is X switch to O and vice versa
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
                    grid.print_grid()
        
        grid.draw(main_window)
        pygame.display.update()
    
                




if __name__ == "__main__":
    run()