from pygame.math import Vector2
from pygame.sprite import Group
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

    def update(self, keys: dict, width: int, height: int, solids: Group):
        self._move(keys, solids)
        self._stay_on_screen(width, height)
        self._change_sprite()

    def _move(self, keys: dict, solids: Group):
        self.direction *= 0

        if keys[K_w]:
            self.direction.y -= 1
        if keys[K_a]:
            self.direction.x -= 1
        if keys[K_s]:
            self.direction.y += 1
        if keys[K_d]:
            self.direction.x += 1

        # NOTE: the player can get stuck in the corner of a wall when moving diagonally.
        # Other than that, this code works for now.
        # TODO: find a way such that the player can't get stuck inside a wall and can
        # freely move diagonally
        if self.direction.length() > 0:
            new_rect = self.rect.move(self.direction.x * self.speed, self.direction.y * self.speed)

            if not any(new_rect.colliderect(obj.rect) for obj in solids):
                self.rect = new_rect

            else: # Handle collisions with solids
                temp_rect_x = self.rect.move(self.direction.x * self.speed, 0)
                temp_rect_y = self.rect.move(0, self.direction.y * self.speed)
                if not any(temp_rect_x.colliderect(obj.rect) for obj in solids):
                    self.rect.x += self.direction.x * self.speed
                if not any(temp_rect_y.colliderect(obj.rect) for obj in solids):
                    self.rect.y += self.direction.y * self.speed
            

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
