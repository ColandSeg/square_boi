import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Square Boi")
        self._screen = pygame.display.set_mode((800, 600))
        self._clock = pygame.time.Clock()

    def run_game(self):
        # Game loop
        while True:
            self._get_inputs()
            self._do_logic()
            self._do_outputs()

    def _get_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def _do_logic(self):
        pass

    def _do_outputs(self):
        self._screen.fill("black")
        pygame.display.flip()
        self._clock.tick(60)