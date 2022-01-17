from asyncio.windows_events import NULL
import pygame as pg
from game.game import Game

def main():
    running = True
    playing = True

    pg.init()
    pg.mixer.init()
    pg.mixer.music.load("assets/sound/music/bg.mp3")
    pg.mixer.music.set_volume(0.01)
    pg.mixer.music.play(5)
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()

    #implement menu

    # implement game
    game = Game(screen, clock)

    while running:
        # start menu

        while playing:
            # game loop
            game.run()


if __name__ == '__main__':
    main()