import pygame as pyg
from objects.player import Player
from utils import load_png
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE
)

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 480
FPS = 60

class Game:
    def __init__(self):
        # Initialize pygame
        pyg.init()

        # Window setup
        self.screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pyg.display.set_caption("Square BOI")
        pyg.display.set_icon(load_png("icon"))

        # Game tools
        self.clock = pyg.time.Clock()
        self.running = True

        # Surfaces and objects
        self.background = load_png("space/bg_space_v1")
        self.player = Player((0, 0), 4)

    def run_game(self):
        while self.running:
            self._do_events()
            self._do_logic()
            self._do_output()
        pyg.quit()
    
    def _do_events(self):
        for event in pyg.event.get():
            # Quit condition
            if event.type == QUIT or (
                event.type == KEYDOWN and event.key == K_ESCAPE
            ):
                self.running = False
                return
        
    def _do_logic(self):
        if not self.running:
            return

        # Input
        keys = pyg.key.get_pressed()
        self.player.update(keys)
        
    def _do_output(self):
        if not self.running:
            return
        
        self.screen.blit(self.background, (0, 0))

        self.player.draw(self.screen)
        
        pyg.display.flip()
        self.clock.tick(FPS)
