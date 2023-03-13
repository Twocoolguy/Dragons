class Boss:
    def __init__(self, name, level, move, boss_number=-1):
        self.name = name
        self.level = level
        self.move = move
        self.boss_number = boss_number
        self.prestige = 1
        self.boss3 = False
        self.boss = True

    def get_file_lines(self):
        """Gets a list of each line of this boss."""
        lines = [
            f"{self.name}\n",
            f"{self.level}\n",
            f"{self.move.name}\n",
            f"{self.boss_number}"
        ]
        return {"name": f"{self.boss_number}.txt", "lines": lines}
