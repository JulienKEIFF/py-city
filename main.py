import pygame, sys 
from settings import settings
from pygame.locals import *

# Beginning Game Loop
def main_loop():
    FramePerSec = pygame.time.Clock()

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        FramePerSec.tick(settings.FPS_COUNTER)

# Initiate game engine
def init_game():
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((720, 480))
    pygame.display.set_caption(settings.GAME_NAME)

    main_loop()
    return 

init_game()