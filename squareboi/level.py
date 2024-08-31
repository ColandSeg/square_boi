from pygame import Surface
from pygame.sprite import Group
from objects.player import Player
from objects.wall import Wall
from objects.saw import Saw
from objects.lock_system import LockSystem
from utils import load_png

CELL_LENGTH = 32
THEMES = {
    1: "space"
}

class Level:
    def __init__(self, lvl_num: int):
        self.lvl_num = lvl_num

        # Read level file
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
                case "l": # locks
                    self.txt_locks = line.split("|")
                case "k": # keys
                    self.txt_keys = line.split("|")
                case "s":
                    self.txt_saws = line.split("|")
                case "f": # wire fences
                    self.txt_fences = line.split("|")
    
    def load_background(self) -> Surface:
        theme = THEMES[int(self.txt_theme[1])]
        background = load_png(f"{theme}/bg_{theme}")

        return background

    def load_player(self) -> Player:
        txt_pos = self.txt_player[1].split(",")
        pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
        speed = float(self.txt_player[2])
        player = Player(pos, speed)

        return player
    
    def load_walls(self) -> Group:
        walls = Group()
        theme = THEMES[int(self.txt_theme[1])]

        self.txt_walls.pop(0)
        for text in self.txt_walls:
            txt_pos = text.split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)

            walls.add(Wall(pos, theme))

        return walls

    def load_lock_system_parts(self, part: str) -> Group:
        part_group = Group()

        match part:
            case "lock":
                txt_parts = self.txt_locks
            case "key":
                txt_parts = self.txt_keys

        txt_parts.pop(0)
        for text in txt_parts:
            split_text = text.split(";")

            txt_pos = split_text[0].split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
            part_id = int(split_text[1])
            color = split_text[2]

            part_group.add(LockSystem(pos, part_id, color, part))

        return part_group
    
    def load_saws(self):
        saws = Group()

        self.txt_saws.pop(0)
        for text in self.txt_saws:
            split_text = text.split(";")

            txt_pos = split_text[0].split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
            facing = split_text[1]

            saws.add(Saw(pos, facing))

        return saws
    
    def load_fences(self):
        fences = Group()

        self.txt_fences.pop(0)
        for text in self.txt_fences:
            txt_pos = text.split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)

            fences.add(Wall(pos, "fence"))

        return fences
