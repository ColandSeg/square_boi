import pygame as pyg
from utils import load_png

# TODO: write code for class Cannon
class Cannon:
    def __init__(self, pos: tuple[int, int], facing: str):
        self.surf = load_png("obstacles/cannon")
        self.rect = self.surf.get_rect(topleft = pos)
        self.facing = facing # N, S, E, W
