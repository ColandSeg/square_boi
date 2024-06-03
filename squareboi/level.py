import pygame as pyg
from player import Player
from wall import Wall
from utils import load_png

THEMES = {
    1: "space",
    2: "grass_hills",
    3: "caves"
}
CELL_LENGTH = 48

class Level:
    def __init__(self, lvl_num: int):
        self.lvl_num = lvl_num

        self.txt_layout = None
        self.txt_theme = None
        self.txt_player = None
        self.txt_walls = None

        with open(f"data/lvl_{self.lvl_num}.txt", "r") as lvl_file:
            self.txt_layout = [line.strip() for line in lvl_file]
        
        for line in self.txt_layout:
            match line[0]:
                case "t": # theme
                    self.txt_theme = line.split("|")
                case "p": # player
                    self.txt_player = line.split("|")
                case "w": # walls
                    self.txt_walls = line.split("|")

    def load_background(self) -> pyg.Surface:
        theme = THEMES[int(self.txt_theme[1])]
        bg_path = f"{theme}/bg_{theme}"
        background = load_png(bg_path)

        return background
    
    def load_player(self) -> Player:    
        txt_pos = self.txt_player[1].split(",")
        pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
        speed = int(self.txt_player[2])
        player = Player(pos, speed)

        return player
    
    def load_walls(self) -> list[Wall]:
        walls = []
        
        self.txt_walls.pop(0)
        for line in self.txt_walls:
            txt_pos = line.split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)

            walls.append(Wall(pos))
        
        return walls
