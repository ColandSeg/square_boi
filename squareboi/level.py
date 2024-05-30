from wall import Wall

class Level:
    # Looks terrible
    # TODO: clean up this code

    def __init__(self, level_num: int):
        self.level_num = level_num
        self.layout = []

    def load_level(self) -> list[list[Wall]]:
        with open(f"data/lvl_{self.level_num}.txt", "r") as level_file:
            layout_text = [line.strip() for line in level_file]
        
        for text in layout_text:
            text_list = text.split("|")
            match text_list[0]:
                case "w":
                    self.layout.append(self._load_walls(text_list))
        
        return self.layout

    def _load_player(self):
        pass

    def _load_walls(self, text_list: list[str]):
        wall_list = []
        text_list.pop(0)
        for text in text_list:
            pos = text.split(",")
            t = (int(pos[0]) * 48, int(pos[1]) * 48)
            wall_list.append(Wall(t))
        return wall_list
