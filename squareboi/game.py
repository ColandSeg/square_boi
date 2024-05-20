import pygame as pyg
from player import Player

WIDTH = 960
HEIGHT = 480

class Game:
    def __init__(self):
        pyg.init()
        pyg.display.set_caption("Square Boi")
        self.screen = pyg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pyg.time.Clock()

        self.player = Player()

    def run_game(self):
        # Game loop
        while True:
            self._get_input()
            self._do_logic()
            self._do_output()

    def _get_input(self):
        # Event loop
        for event in pyg.event.get():
            # Alt+F4
            if event.type == pyg.QUIT or (
                event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE
            ):
                pyg.quit()
                quit()
        
        self.player.move()

    def _do_logic(self):
        self.player.stay_on_screen(WIDTH, HEIGHT)

    def _do_output(self):
        self.screen.fill("#111111")
        self.screen.blit(self.player.surf, self.player.rect)

        pyg.display.flip()
        self.clock.tick(60)