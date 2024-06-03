from player import Player
from wall import Wall

THEMES = {
    1: "space",
    2: "grass_hills",
    3: "caves"
}
CELL_LENGTH = 48

class Level:
    # maybe this code can benefit from a match-case?

    def __init__(self, lvl_num: int):
        self.lvl_num = lvl_num
        self.txt_layout = None

        with open(f"data/lvl_{self.lvl_num}.txt", "r") as lvl_file:
            self.txt_layout = [line.strip() for line in lvl_file]

    def load_background_path(self):
        txt_theme = None
        for line in self.txt_layout:
            if line[0] == "t":
                txt_theme = line.split("|")
        
        theme = THEMES[int(txt_theme[1])]

        return f"{theme}/bg_{theme}"
    
    def load_player(self) -> Player:
        txt_player = None
        for line in self.txt_layout:
            if line[0] == "p":
                txt_player = line.split("|")
        
        txt_pos = txt_player[1].split(",")
        pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)
        speed = int(txt_player[2])
        player = Player(pos, speed)

        return player
    
    def load_walls(self) -> list[Wall]:
        txt_walls = None
        walls = []
        for line in self.txt_layout:
            if line[0] == "w":
                txt_walls = line.split("|")
        
        txt_walls.pop(0)
        for line in txt_walls:
            txt_pos = line.split(",")
            pos = tuple(int(num) * CELL_LENGTH for num in txt_pos)

            walls.append(Wall(pos))
        
        return walls
