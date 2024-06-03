import pygame as pyg
from level import Level
from utils import load_png

# TODO: write classes for obstacles

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 480
FPS = 60

class Game:
    def __init__(self):
        # Setup
        pyg.init()
        self.screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pyg.display.set_caption("Square Boi")
        pyg.display.set_icon(load_png("icon"))
        self.clock = pyg.time.Clock()
        self.active = True

        # Loading
        self.level = Level(1)
        self.background = self.level.load_background()
        self.player = self.level.load_player()
        self.walls = self.level.load_walls()

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
        
        # self.player.move()
        self.player.move(self.walls)

    def _do_logic(self):
        if not self.active:
            return

        self.player.stay_on_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        # NOTE: TEMPORARY CODE
        # collision of player with lists
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
