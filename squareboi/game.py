import pygame as pyg
from pygame.sprite import Group
from level import Level
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

        # Loading level
        self.level = Level(1)
        self.background = self.level.load_background()
        self.player = self.level.load_player()
        self.walls = self.level.load_walls()

        self.solids = Group()
        self.solids.add(self.walls)

        self.all_sprites = Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.walls)

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
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT, self.solids)
        
    def _do_output(self):
        if not self.running:
            return
        
        self.screen.blit(self.background, (0, 0))

        for sprite in self.all_sprites:
            sprite.draw(self.screen)
        
        pyg.display.flip()
        self.clock.tick(FPS)
