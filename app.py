import pygame
pygame.init()

BLACK  = (0,0,0)
WHITE = (255,255,255)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

RUNNING = True

window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
caption = pygame.display.set_caption("TIC-Tac-Toe")


while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
        if RUNNING:
            pygame.display.update()
            window.fill(WHITE)

