from pygame.transform import rotate
from objects.game_object import GameObject
from utils import load_png

class Cannon(GameObject):
    def __init__(self, pos: tuple[int, int], facing: str):
        super().__init__(load_png("obstacles/cannon", True), pos, 0, facing)

        match self.facing:
            case "N":
                self.surf = rotate(self.surf, 0)
            case "S":
                self.surf = rotate(self.surf, 180)
            case "E":
                self.surf = rotate(self.surf, 270)
            case "W":
                self.surf = rotate(self.surf, 90)
