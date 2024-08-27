from pygame import Surface
from pygame.sprite import Group
from objects.player import Player
from objects.wall import Wall
from utils import load_png

CELL_LENGTH = 32
THEMES = {
    1: "space"
}

class Level:
    def __init__(self, lvl_num: int):
        self.lvl_num = lvl_num

        with open(f"data/lvl_{self.lvl_num}.txt", "r") as lvl_file:
            self.txt_layout = [line.strip() for line in lvl_file]

        for line in self.txt_layout:
            match line[0]:
                case "t": # level theme
                    self.txt_theme = line.split("|")
                case "p": # player
                    self.txt_player = line.split("|")
                case "w": # walls
                    self.txt_walls = line.split("|")
    
    def load_background(self) -> Surface:
        theme = THEMES[int(self.txt_theme[1])]
        background = load_png(f"{theme}/bg_{theme}")

        return background

    def load_player(self) -> Player:
        txt_pos = self.txt_player[1].split(",")
        pos = tuple(int(num) *  CELL_LENGTH for num in txt_pos)
        speed = int(self.txt_player[2])
        player = Player(pos, speed)

        return player
    
    def load_walls(self) -> Group:
        walls = Group()

        self.txt_walls.pop(0)
        for text in self.txt_walls:
            txt_pos = text.split(",")
            pos = tuple(int(num) *  CELL_LENGTH for num in txt_pos)

            walls.add(Wall(pos, THEMES[int(self.txt_theme[1])]))

        return walls
