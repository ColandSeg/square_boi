import pygame as pyg
from level import Level
# NOTE: temporary
from objects.cannon import Cannon
from objects.saw import Saw
from utils import load_img

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 480
FPS = 60

class Game:
    def __init__(self):
        # Initialization
        pyg.init()
        pyg.display.set_caption("Square Boi")
        
        # Window
        self.screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pyg.display.set_icon(load_img("icon.png"))
        self.clock = pyg.time.Clock()
        self.active = True

        # Loading objects
        self.level = Level(1) # NOTE: temporary
        self.background = self.level.load_background()
        self.player = self.level.load_player()
        self.walls = self.level.load_walls()
        # NOTE: temporary code
        self.cannons = [
            Cannon((7*48, 1*48), "S"),
            Cannon((18*48, 6*48), "N"),
            Cannon((13*48, 8*48), "W")
        ]
        self.saws = [
            Saw((4*48, 2*48), "n")
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
            # Quit condition (Alt + f4 or Esc)
            if event.type == pyg.QUIT or (
                event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE
                # TODO: Implement code for a pausing screen which is activated
                # when Esc is pressed
            ):
                # Quit the game
                self.active = False
                return
        
        # Player movement
        self.player.move(self.walls)

    def _do_logic(self):
        if not self.active:
            return

        self.player.change_sprite()
        self.player.stay_on_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

        for saw in self.saws:
            saw.move(self.walls)

    def _do_output(self):
        if not self.active:
            return

        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        for wall in self.walls:
            wall.draw(self.screen)
        for cannon in self.cannons:
            cannon.draw(self.screen)
        for saw in self.saws:
            saw.draw(self.screen)

        pyg.display.flip()
        self.clock.tick(FPS)
