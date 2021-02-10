class Achievement:
    def __init__(self, actions, numbers, message, number):
        self.actions = actions
        self.numbers = numbers
        self.message = message
        self.number = number

    def get_file_lines(self):
        """Gets a list of each line of this achievement."""
        str_actions = ""
        str_numbers = ""
        if len(self.actions) > 1:
            str_actions = ",".join(self.actions)
            str_numbers = ",".join(self.numbers)
        else:
            str_actions = self.actions[0]
            str_numbers = self.numbers[0]
        return {"name": f"{self.number}.txt", "lines": [f"{str_actions}\n", f"{str_numbers}\n", f"{self.message}"]}
