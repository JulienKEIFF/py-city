import pygame as pg
import pygame_menu
from game.game import Game

class Launcher:

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.mixer.music.load("assets/sound/music/bg.mp3")
        pg.mixer.music.set_volume(0.01)
        pg.mixer.music.play(5)
        self.screen = pg.display.set_mode((1440, 960))
        self.clock = pg.time.Clock()
        self.game = Game(self.screen, self.clock)
        self.create_theme()
        self.main_menu()

    def main_menu(self):
        menu = pygame_menu.Menu('PY CITY', 800, 600, theme=self.THEME)
        menu.add.button('Lancer la partie', self.start_game)
        menu.mainloop(self.screen)

    def create_theme(self):
        font = pygame_menu.font.FONT_8BIT
        self.THEME = pygame_menu.Theme(
            background_color=(0,0,0,0),
            title_background_color=(100,100,100),
            title_font=font,
            title_font_shadow=True,
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
            widget_padding=25,
            widget_font=font
        )


    def start_game(self):
        running = True
        playing = True
        while running:
            pg.event.set_grab(True)
            while playing:
                self.game.run()

def main():
    Launcher()

if __name__ == '__main__':
    main()