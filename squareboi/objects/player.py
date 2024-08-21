from objects.game_object import GameObject
from utils import load_png
from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
)

class Player(GameObject):
    def __init__(self, pos: tuple[int, int], speed):
        self.sprites = {
            # default
            "front": load_png("player/player_front"),
            # straights
            "up":    load_png("player/player_up"),
            "left":  load_png("player/player_left"),
            "down":  load_png("player/player_down"),
            "right": load_png("player/player_right")
            # diagonals
            # TODO: add diagonal sprites
        }
        
        super().__init__(self.sprites["front"], pos, speed)

    def update(self, keys: dict):
        if keys[K_w]:
            self.rect.move_ip(0, -4)
        if keys[K_s]:
            self.rect.move_ip(0, 4)
        if keys[K_a]:
            self.rect.move_ip(-4, 0)
        if keys[K_d]:
            self.rect.move_ip(4, 0)
