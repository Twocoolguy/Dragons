class Form:
    def __init__(self, name, multiplier, level_required, element):
        self.name = name
        self.multiplier = multiplier
        self.level_required = level_required
        self.element = element

    def has_form(self, level, element):
        """Returns a boolean if the level and element meet the requirements for this form."""
        if element == self.element:
            if level >= self.level_required:
                return True
        return False

    def equals(self, form):
        """Checks if two form objects are equal."""
        return form.name == self.name

    def get_file_lines(self):
        """Gets a list of each line of this form."""
        lines = [
            f"{self.multiplier}\n",
            f"{self.level_required}"
        ]
        return {"name": f"{self.element}/{self.name}.txt", "lines": lines}
