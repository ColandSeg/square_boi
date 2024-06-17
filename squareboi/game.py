import pygame as pyg
from level import Level
from squareboi.objects.cannon import Cannon # NOTE: temporary (?)
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
        self.obstacles = [
            Cannon((7*48, 1*48), "S"),
            Cannon((18*48, 6*48), "N"),
            Cannon((13*48, 8*48), "W")
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
        # self.player.move()
        self.player.move(self.walls)
        self.player.change_sprite()

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
        for wall in self.walls:
            wall.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        pyg.display.flip()
        self.clock.tick(FPS)
