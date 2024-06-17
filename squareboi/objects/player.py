import pygame as pyg
from pygame.math import Vector2
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

        super().__init__(self.sprites["front"], pos)       

        self.speed = speed
        self.direction = Vector2(0, 0)
        
    def move(self, walls: list[Wall]):
        # Perhaps the code for `move` is getting too cluttered...
        # TODO: Divide code for `move` into differente methods:
        #   - Moving
        #   - Collision handling
        keys = pyg.key.get_pressed()
        self.direction = Vector2(0, 0) # reset direction

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
        keys = pyg.key.get_pressed()

        if self.direction.length() > 0:
            # straight
            if keys[pyg.K_w] and not ( # W
                keys[pyg.K_s]
            ):
                self.surf = self.sprites["up"]

            if keys[pyg.K_a] and not ( # A
                keys[pyg.K_d]
            ):
                self.surf = self.sprites["left"]

            if keys[pyg.K_s] and not ( # S
                keys[pyg.K_w]
            ):
                self.surf = self.sprites["down"]

            if keys[pyg.K_d] and not ( # D
                keys[pyg.K_a]
            ):
                self.surf = self.sprites["right"]
            
            # diagonals
            if keys[pyg.K_w] and keys[pyg.K_a] and not ( # W + A
                keys[pyg.K_s] or keys[pyg.K_d]
            ):
                self.surf = self.sprites["northwest"]

            if keys[pyg.K_w] and keys[pyg.K_d] and not ( # W + D
                keys[pyg.K_s] or keys[pyg.K_a]
            ):
                self.surf = self.sprites["northeast"]

            if keys[pyg.K_s] and keys[pyg.K_a] and not ( # S + A
                keys[pyg.K_w] or keys[pyg.K_d]
            ):
                self.surf = self.sprites["southwest"]

            if keys[pyg.K_s] and keys[pyg.K_d] and not ( # S + D
                keys[pyg.K_w] or keys[pyg.K_a]
            ):
                self.surf = self.sprites["southeast"]

        else:
            self.surf = self.sprites["front"] # default player sprite
    
    def stay_on_screen(self, width: int, height: int):
        self.rect.x = clamp(self.rect.x, 0, width - self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, height - self.rect.height)

    
