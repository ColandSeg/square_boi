import pygame as pyg
from player import Player
from wall import Wall
from utils import load_png

WIDTH = 960
HEIGHT = 480
FPS = 60

class Game:
    def __init__(self):
        pyg.init()
        pyg.display.set_caption("Square Boi")
        self.screen = pyg.display.set_mode((WIDTH, HEIGHT))
        self.background = load_png("space", "bg_space")
        self.clock = pyg.time.Clock()
        self.active = True

        self.player = Player((WIDTH // 2, HEIGHT // 2), 4)

    def run_game(self):
        # Game loop
        while self.active:
            self._get_input()
            self._do_logic()
            self._do_output()

    def _get_input(self):
        # Event loop
        for event in pyg.event.get():
            # Quit condition
            if event.type == pyg.QUIT or (
                event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE
            ):
                # Quit the game
                self.active = False
                return
        
        self.player.move()

    def _do_logic(self):
        if not self.active:
            return

        self.player.stay_on_screen(WIDTH, HEIGHT)

    def _do_output(self):
        if not self.active:
            return

        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)

        pyg.display.flip()
        self.clock.tick(FPS)
