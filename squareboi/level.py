class Level:
    def __init__(self, level_num: int):
        self.level_num = level_num

    def load_level(self):
        with open(f"data/level_{self.level_num}.txt", "r") as level_file:
            content = level_file.read()
            print(content)
            positions = content.split(";")
            print(positions)
            for pos in positions:
                new_pos = tuple(pos.split(","))
                print(new_pos, end=" | ")

level_1 = Level(1)
level_1.load_level()
