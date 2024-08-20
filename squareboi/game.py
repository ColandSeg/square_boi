import pygame as pyg
from objects.player import Player
from utils import load_png

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 480
FPS = 60

class Game:
    def __init__(self):
        pyg.init()

        self.screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pyg.time.Clock()
        self.running = True

        self.background = load_png("space/bg_space_v1")

        self.player = Player((0, 0), 4)

    def run_game(self):
        while self.running:
            self._get_input()
            self._do_logic()
            self._do_output()
        pyg.quit()
    
    def _get_input(self):
        for event in pyg.event.get():
            # Quit condition
            if event.type == pyg.QUIT:
                self.running = False
                return
            
        keys = pyg.key.get_pressed()
        self.player.update(keys)
        
    def _do_logic(self):
        if not self.running:
            return
        
    def _do_output(self):
        if not self.running:
            return
        
        self.screen.blit(self.background, (0, 0))
        
        pyg.display.flip()
        self.clock.tick(FPS)
