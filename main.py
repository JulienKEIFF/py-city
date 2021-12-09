import pygame, sys 
from settings import settings
from pygame.locals import *

WHITE = (200, 200, 200)

def draw_grid():
    blockSize = 20  # Set the size of the grid block
    for x in range(720):
        for y in range(480):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(pygame.display.get_surface(), WHITE, rect, 1)

# Beginning Game Loop
def loop():
    FramePerSec = pygame.time.Clock()

    while True:
        pygame.display.update()
        draw_grid()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        FramePerSec.tick(settings.FPS_COUNTER)

# Initiate game engine
def main():
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((720, 480))
    pygame.display.set_caption(settings.GAME_NAME)

    loop()
    return 

main()