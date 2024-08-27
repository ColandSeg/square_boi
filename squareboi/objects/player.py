from pygame.math import Vector2
from objects.game_object import GameObject
from utils import load_png, clamp
from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
)

class Player(GameObject):
    def __init__(self, pos: tuple[int, int], speed: int):
        self.sprites = {
            # default
            "front":     load_png("player/player_front"),
            # straights
            "up":        load_png("player/player_up"),
            "left":      load_png("player/player_left"),
            "down":      load_png("player/player_down"),
            "right":     load_png("player/player_right"),
            # diagonals
            "northeast": load_png("player/player_NE"),
            "northwest": load_png("player/player_NW"),
            "southeast": load_png("player/player_SE"),
            "southwest": load_png("player/player_SW")
        }
        
        super().__init__(self.sprites["front"], pos, speed)

    def update(self, keys: dict, width: int, height: int):
        self._move(keys)
        self._stay_on_screen(width, height)
        self._change_sprite()

    def _move(self, keys: dict):
        self.direction *= 0

        if keys[K_w]:
            self.direction.y -= 1
        if keys[K_a]:
            self.direction.x -= 1
        if keys[K_s]:
            self.direction.y += 1
        if keys[K_d]:
            self.direction.x += 1
        
        self.rect.move_ip(
            self.direction.x * self.speed,
            self.direction.y * self.speed
        )

    def _stay_on_screen(self, width: int, height: int):
        self.rect.x = clamp(self.rect.x, 0, width - self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, height - self.rect.height)
    
    def _change_sprite(self):
        # Default sprite if `direction` = 0
        self.surf = self.sprites["front"]

        # Change to straight sprites
        if self.direction == Vector2(0, -1):
            self.surf = self.sprites["up"]
        elif self.direction == Vector2(-1, 0):
            self.surf = self.sprites["left"]
        elif self.direction == Vector2(0, 1):
            self.surf = self.sprites["down"]
        elif self.direction == Vector2(1, 0):
            self.surf = self.sprites["right"]
        # Change to diagonal sprites
        elif self.direction == Vector2(1, -1):
            self.surf = self.sprites["northeast"]
        elif self.direction == Vector2(-1, -1):
            self.surf = self.sprites["northwest"]
        elif self.direction == Vector2(1, 1):
            self.surf = self.sprites["southeast"]
        elif self.direction == Vector2(-1, 1):
            self.surf = self.sprites["southwest"]
