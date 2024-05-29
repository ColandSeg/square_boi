import pygame as pyg
from player import Player
from wall import Wall
from level import Level
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

        self.player = Player((48, 48), 4)
        # NOTE: TEMPORARY CODE
        self.walls = [
            Wall((144, 0)),
            Wall((144, 48)),
            Wall((144, 96)),
            Wall((144, 144)),
            Wall((0, 144))
        ]

    def run_game(self):
        # Game loop
        while self.active:
            self._get_input()
            self._do_logic()
            self._do_output()
        pyg.quit()

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
        
        self.player.move(self.walls)

    def _do_logic(self):
        if not self.active:
            return

        self.player.stay_on_screen(WIDTH, HEIGHT)
        # NOTE: TEMPORARY CODE
        if self.player.rect.collidelist(self.walls) != -1:
            pass

    def _do_output(self):
        if not self.active:
            return

        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        # NOTE: TEMPORARY CODE
        for wall in self.walls:
            wall.draw(self.screen)

        pyg.display.flip()
        self.clock.tick(FPS)
