from pygame import Surface
from objects.player import Player
from objects.wall import Wall
from objects.cannon import Cannon
from objects.saw import Saw
from objects.electric_current import ElectricCurrent
from utils import load_img

THEMES = {
    1: "space",
    2: "grassland",
    3: "caves"
}
CELL_LENGTH = 48

class Level:
    def __init__(self, lvl_num: int):
        self.lvl_num = lvl_num

        with open(f"data/lvl_{self.lvl_num}.txt", "r") as lvl_file:
            self.txt_layout = [line.strip() for line in lvl_file]

        self.txt_cannons = []
        self.txt_saws = []
        self.txt_electrics = []
        
        for line in self.txt_layout:
            match line[0]:
                case "t": # theme
                    self.txt_theme = line.split("|")
                case "p": # player
                    self.txt_player = line.split("|")
                case "w": # walls
                    self.txt_walls = line.split("|")
                case "c": # cannons
                    self.txt_cannons.append(line.split("|"))
                case "s": # saws
                    self.txt_saws.append(line.split("|"))
                case "e": # electric currents
                    self.txt_electrics.append(line.split("|"))

    def load_background(self) -> Surface:
        theme = THEMES[int(self.txt_theme[1])]
        bg_path = f"{theme}/bg_{theme}.png"
        background = load_img(bg_path)

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

            walls.append(Wall(pos, THEMES[int(self.txt_theme[1])]))
        
        return walls
    
    def load_cannons(self) -> list[Cannon]:
        cannons = []

        for txt_cannon in self.txt_cannons:
            txt_pos = txt_cannon[1].split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
            facing = txt_cannon[2]

            cannons.append(Cannon(pos, facing))
        
        return cannons
    
    def load_saws(self) -> list[Saw]:
        saws = []

        for txt_saw in self.txt_saws:
            txt_pos = txt_saw[1].split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
            facing = txt_saw[2]

            saws.append(Saw(pos, facing))
        
        return saws
    
    def load_electric_currents(self) -> list[ElectricCurrent]:
        electrics = []

        for txt_electric in self.txt_electrics:
            txt_pos = txt_electric[1].split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
            facing = txt_electric[2]

            electrics.append(ElectricCurrent(pos, facing))
        
        return electrics
