import pygame as pyg
from player import Player

class Game:
    def __init__(self):
        pyg.init()
        pyg.display.set_caption("Square Boi")
        self.screen = pyg.display.set_mode((960, 480))
        self.clock = pyg.time.Clock()

        self.player = Player()

    def run_game(self):
        # Game loop
        while True:
            self.get_input()
            self.do_logic()
            self.do_output()

    def get_input(self):
        # Event loop
        for event in pyg.event.get():
            # Alt+F4
            if event.type == pyg.QUIT or (
                event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE
            ):
                pyg.quit()
                quit()
        
        self.player.move()

    def do_logic(self):
        self.player.stay_on_screen()

    def do_output(self):
        self.screen.fill("#111111")
        self.screen.blit(self.player.surface, self.player.rect)

        pyg.display.flip()
        self.clock.tick(60)