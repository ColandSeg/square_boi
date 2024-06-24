import pygame as pyg
from objects.game_object import GameObject
from objects.wall import Wall
from utils import load_img, clamp

class Player(GameObject):
    def __init__(self, pos: tuple[int, int], speed: int):
        self.sprites = {
            # default
            "front":        load_img("player/player_front.png"),
            # straight
            "up":           load_img("player/player_up.png"),
            "left":         load_img("player/player_left.png"),
            "down":         load_img("player/player_down.png"),
            "right":        load_img("player/player_right.png"),
            # diagonals
            "northeast":    load_img("player/player_NE.png"),
            "northwest":    load_img("player/player_NW.png"),
            "southeast":    load_img("player/player_SE.png"),
            "southwest":    load_img("player/player_SW.png")
        }

        super().__init__(self.sprites["front"], pos, speed)
        
    def move(self, walls: list[Wall]):
        # Perhaps the code for `move` is getting too cluttered...
        # TODO: Divide code for `move` into differente methods:
        #   - Moving
        #   - Collision handling
        keys = pyg.key.get_pressed()
        self.direction *= 0 # reset direction

        if keys[pyg.K_w]:
            self.direction.y -= 1
        if keys[pyg.K_a]:
            self.direction.x -= 1
        if keys[pyg.K_s]:
            self.direction.y += 1
        if keys[pyg.K_d]:
            self.direction.x += 1

        if self.direction.length() > 0:
            # I have difficulty understanding what this code does, but it'll work for now
            new_rect = self.rect.move(self.direction.x * self.speed, self.direction.y * self.speed)

            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect = new_rect
            else:
                temp_rect_x = self.rect.move(self.direction.x * self.speed, 0)
                temp_rect_y = self.rect.move(0, self.direction.y * self.speed)
                if not any(temp_rect_x.colliderect(wall.rect) for wall in walls):
                    self.rect.x += self.direction.x * self.speed
                if not any(temp_rect_y.colliderect(wall.rect) for wall in walls):
                    self.rect.y += self.direction.y * self.speed
    
    def change_sprite(self):
        self.surf = self.sprites["front"] # default sprite

        # straight sprites
        if self.direction == (1, 0):
            self.surf = self.sprites["right"]
        if self.direction == (0, 1):
            self.surf = self.sprites["down"]
        if self.direction == (-1, 0):
            self.surf = self.sprites["left"]
        if self.direction == (0, -1):
            self.surf = self.sprites["up"]
        
        # diagonal sprites
        if self.direction == (1, 1):
            self.surf = self.sprites["southeast"]
        if self.direction == (-1, 1):
            self.surf = self.sprites["southwest"]
        if self.direction == (1, -1):
            self.surf = self.sprites["northeast"]
        if self.direction == (-1, -1):
            self.surf = self.sprites["northwest"]

    def stay_on_screen(self, width: int, height: int):
        self.rect.x = clamp(self.rect.x, 0, width - self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, height - self.rect.height)

    def bump_with(self, objects: list[GameObject]):
        # TODO: add method in which the player bumps with an object
        # Collisions with said objects act like walls
        pass

    def crash_with(self, objects: list[GameObject]):
        # TODO: add method in which the player crashes with an object
        # Collisions with said objects act like Game Overs
        pass
