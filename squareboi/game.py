import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Square Boi")
        self._screen = pygame.display.set_mode((1000, 500))
        self._clock = pygame.time.Clock()

    def run_game(self):
        # Game loop
        while True:
            self._get_input()
            self._do_logic()
            self._do_output()

    def _get_input(self):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def _do_logic(self):
        pass

    def _do_output(self):
        self._screen.fill("#111111")

        pygame.display.flip()
        self._clock.tick(60)