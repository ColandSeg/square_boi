from objects.game_object import GameObject
from utils import load_png

class Wall(GameObject):
    def __init__(self, pos: tuple[int, int], theme: str):
        if theme == "fence":
            super().__init__(load_png(f"obstacles/wire_fence", True), pos)

        else:
            super().__init__(load_png(f"{theme}/wall_{theme}"), pos)
