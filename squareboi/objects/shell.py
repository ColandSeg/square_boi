from objects.game_object import GameObject
from utils import load_png

class Shell(GameObject):
    def __init__(self, pos: tuple[int, int]):
        super().__init__(load_png("obstacles/shell", True), pos)

    def update(self):
        pass
