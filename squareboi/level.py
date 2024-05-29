class Level:
    def __init__(self, level_num: int):
        self.level_num = level_num

    def load_level(self):
        with open(f"data/level_{self.level_num}.txt", "r") as level_file:
            pass
