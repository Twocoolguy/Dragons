class Move:
    def __init__(self, name, element, damage, accuracy, level_needed=0, unlock=0):
        self.name = name
        self.element = element
        self.damage = int(damage)
        self.accuracy = int(accuracy)
        self.level_needed = int(level_needed)
        self.unlock = int(unlock)

    def has_move(self, level, element):
        """Checks if the level and element allow the dragon to use this move."""
        if level >= self.level_needed:
            if element == "all":
                return True
            if element == self.element:
                return True
        return False

    def equals(self, move):
        """Checks if the name of this object and the name of the other object are the same."""
        return move.name == self.name

    def string_equals(self, name):
        """Checks if the name of this object and the string that is passed are the same."""
        return self.name == name

    def get_file_lines(self):
        """Gets a list of each line of this move."""
        lines = [
            f"{self.name}\n",
            f"{self.element}\n",
            f"{self.damage}\n",
            f"{self.accuracy}\n",
            f"{self.level_needed}\n",
            f"{self.unlock}"
        ]
        return {"name": f"{self.name}.txt", "lines": lines}
