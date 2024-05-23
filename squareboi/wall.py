import pygame as pyg
from utils import load_png

class Wall:
    def __init__(self, pos: tuple[int, int]):
        self.surf = load_png("space", "wall_space")
        self.rect = self.surf.get_rect(topleft = pos)

    def draw(self, screen: pyg.Surface):
        screen.blit(self.surf, self.rect)
