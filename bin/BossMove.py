class BossMove:
    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy

    def equals(self, boss_move):
        """Checks if another instance of this object is equal to this object"""
        return boss_move.name == self.name

    def string_equals(self, name):
        """Checks if the name of this object is the same as the string provided."""
        return self.name == name

    def get_file_lines(self):
        """Gets a list of each line of this bossmove."""
        lines = [
            f"{self.name}\n",
            f"{self.damage}\n",
            f"{self.accuracy}"
        ]
        return {"name": f"{self.name}.txt", "lines": lines}
