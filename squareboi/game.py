import pygame as pyg
from player import Player
from level import Level

WIDTH = 960
HEIGHT = 480
FPS = 60

class Game:
    def __init__(self):
        pyg.init()
        pyg.display.set_caption("Square Boi")
        self.screen = pyg.display.set_mode((WIDTH, HEIGHT))
        self.background = pyg.image.load("assets/sprites/space/bg_space.png").convert()
        self.clock = pyg.time.Clock()

        self.player = Player((WIDTH // 2, HEIGHT // 2), 4)

    def run_game(self):
        # Game loop
        while True:
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
                pyg.quit()
                quit()
        
        self.player.move()

    def _do_logic(self):
        self.player.stay_on_screen(WIDTH, HEIGHT)

    def _do_output(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)

        pyg.display.flip()
        self.clock.tick(FPS)
