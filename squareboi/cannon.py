import pygame as pyg
from utils import load_png

SHELL_SPEED = 3

class Cannon:
    def __init__(self, pos: tuple[int, int], facing: str):
        self.surf = load_png("obstacles/cannon", True)
        self.rect = self.surf.get_rect(topleft = pos)
        self.facing = facing # N, S, E, W

        match self.facing:
            case "N":
                self.surf = pyg.transform.rotate(self.surf, 0)
            case "S":
                self.surf = pyg.transform.rotate(self.surf, 180)
            case "E":
                self.surf = pyg.transform.rotate(self.surf, 270)
            case "W":
                self.surf = pyg.transform.rotate(self.surf, 90)
    
    def draw(self, screen: pyg.Surface):
        screen.blit(self.surf, self.rect)

    def fire(self):
        pass

class Shell:
    def __init__(self):
        pass
