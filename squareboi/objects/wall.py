from objects.game_object import GameObject
from utils import load_png

class Wall(GameObject):
    def __init__(self, pos: tuple[int, int], theme:str):
        super().__init__(load_png(f"{theme}/wall_{theme}"), pos)
