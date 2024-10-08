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
FPS = 30

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
        self.locks = self.level.load_lock_system_parts("lock")
        self.keys = self.level.load_lock_system_parts("key")
        self.saws = self.level.load_saws()
        self.cannons = self.level.load_cannons()
        self.fences = self.level.load_fences()

        # Solids for the player
        self.solids = Group()
        self.solids.add(self.walls)
        self.solids.add(self.locks)
        self.solids.add(self.cannons)
        self.solids.add(self.fences)

        # Solids for obstacles
        self.obstacle_solids = Group()
        self.obstacle_solids.add(self.walls)
        self.obstacle_solids.add(self.locks)

        # For drawing only
        self.all_sprites = Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.walls)
        self.all_sprites.add(self.locks)
        self.all_sprites.add(self.keys)
        self.all_sprites.add(self.saws)
        self.all_sprites.add(self.cannons)
        self.all_sprites.add(self.fences)

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
                # NOTE: temporary. Pressing escape should pause the game.
                self.running = False
                return
        
    def _do_logic(self):
        if not self.running:
            return

        # Input
        pressed_keys = pyg.key.get_pressed()
        self.player.update(pressed_keys, SCREEN_WIDTH, SCREEN_HEIGHT, self.solids)

        # Lock systems
        collided_keys = pyg.sprite.spritecollide(self.player, self.keys, True)
        for key in collided_keys:
            for lock in self.locks:
                if key.system_id == lock.system_id:
                    lock.open_lock()

        self.saws.update(SCREEN_WIDTH, SCREEN_HEIGHT, self.obstacle_solids)
        
    def _do_output(self):
        if not self.running:
            return
        
        self.screen.blit(self.background, (0, 0))

        for sprite in self.all_sprites:
            sprite.draw(self.screen)
        
        pyg.display.flip()
        self.clock.tick(FPS)
