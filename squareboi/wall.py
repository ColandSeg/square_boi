import pygame as pyg
from utils import load_img

class Wall:
    def __init__(self, pos: tuple[int, int]):
        self.surf = load_img("space/wall_space.png")
        self.rect = self.surf.get_rect(topleft = pos)

    def draw(self, screen: pyg.Surface):
        screen.blit(self.surf, self.rect)
