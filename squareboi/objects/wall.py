from objects.game_object import GameObject
from utils import load_img

class Wall(GameObject):
    def __init__(self, pos: tuple[int, int], theme):
        super().__init__(load_img(f"{theme}/wall_{theme}.png"), pos)
