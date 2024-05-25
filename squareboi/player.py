import pygame as pyg
from pygame.math import Vector2
from utils import load_png

class Player:
    def __init__(self, pos: tuple[int, int], speed: int):
        self.sprites = {
            "front":    load_png("player", "player_front"),
            "up":       load_png("player", "player_up"),
            "left":     load_png("player", "player_left"),
            "down":     load_png("player", "player_down"),
            "right":    load_png("player", "player_right"),
        }
        
        self.surf = self.sprites["front"]
        self.rect = self.surf.get_rect(topleft = pos)
        self.speed = speed
        
    def move(self):
        keys = pyg.key.get_pressed()
        direction = Vector2(0, 0)

        if keys[pyg.K_w]:
            direction.y -= 1
            self.surf = self.sprites["up"]
        if keys[pyg.K_a]:
            direction.x -= 1
            self.surf = self.sprites["left"]
        if keys[pyg.K_s]:
            direction.y += 1
            self.surf = self.sprites["down"]
        if keys[pyg.K_d]:
            direction.x += 1
            self.surf = self.sprites["right"]

        if direction.length() > 0:
            direction.normalize()
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed
        else:
            self.surf = self.sprites["front"] # default player sprite
    
    def stay_on_screen(self, width: int, height: int):
        self.rect.x = max(0, min(self.rect.x, width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, height - self.rect.height))

    def draw(self, screen: pyg.Surface):
        screen.blit(self.surf, self.rect)
