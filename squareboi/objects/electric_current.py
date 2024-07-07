import pygame as pyg
from objects.game_object import GameObject
from utils import load_img

class ElectricCurrent(GameObject):
    def __init__(self, pos: tuple[int, int], facing: str):
        super().__init__(load_img("obstacles/electric1.png", True), pos)
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
