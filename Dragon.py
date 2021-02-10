import math
from random import choice


class Dragon:
    def __init__(self, name, element, config_reader, level=1, prestige=1, boss_number=1, boss_number3=1, story_number=1, exp=0):
        self.name = name
        self.element = element
        self.exp = exp
        self.level = level
        self.boss_number = boss_number
        self.prestige = prestige
        self.boss3_number = boss_number3
        self.story_number = story_number
        self.moves = []
        self.forms = []
        self.check_moves_and_forms(config_reader)
        self.config_reader = config_reader
        self.boss = False

    def check_moves_and_forms(self, config_reader):
        """Basically checks if the dragon has new moves, or forms."""
        if config_reader is None:
            return -10
        moves_list = [x.name for x in self.moves]
        for move in config_reader.moves:
            if move.name in moves_list:
                continue
            if move.element == self.element:
                if move.level_needed <= self.level:
                    if move.unlock != 0:
                        if self.boss_number > move.unlock:
                            self.moves.append(move)
                            moves_list.append(move.name)
                    else:
                        self.moves.append(move)
                        moves_list.append(move.name)
        forms_list = [x.name for x in self.forms]
        for form in config_reader.forms:
            if form.name in forms_list:
                continue
            if form.element == self.element:
                if form.level_required <= self.level:
                    self.forms.append(form)
                    forms_list.append(form.name)

    def get_form(self, number):
        """Returns a form by the number. If there is no form with this number, then it returns none."""
        self.check_moves_and_forms(self.config_reader)
        for form in self.forms:
            if int(form) == number:
                return form
        return None

    def get_move(self, name):
        """Returns the move by the name. If there is no move with this name it returns none."""
        self.check_moves_and_forms(self.config_reader)
        for move in self.moves:
            if move.name == name:
                return move
        return None

    def get_random_move(self):
        """Returns a random move from the moveset the dragon has."""
        self.check_moves_and_forms(self.config_reader)  # Get the moves that they have access to.
        if len(self.moves) == 0:
            return None
        return choice(self.moves)

    def get_random_form(self):
        """Returns a random form from the forms the dragon has."""
        self.check_moves_and_forms(self.config_reader)
        if len(self.forms) == 0:
            return None
        return choice(self.forms)

    def prestige_up(self):
        """Basically puts the dragon to the next prestige as long as it is smaller than the max."""
        if self.prestige < self.config_reader.max_prestige:
            if self.level == 3000:
                self.prestige += 1
                self.level = 1
                return 0
            return -2
        return -1

    def gain_exp(self, exp):
        """Gains the dragon exp. Updates the dragon basically."""
        level = self.level
        if level >= 3000:
            print(f"Your dragon is already the max level so it did not level up.")
        while float(level) <= math.floor(0.1 * math.sqrt(self.exp + exp)):
            if level >= 3000:
                break
            level += 1
        times = level - self.level
        if times == 0:
            if level >= 3000:
                print(f"Your dragon is already the max level so it did not level up. You should prestige if you can!")
                return -1
            else:
                print("Your dragon did not level up.")
        if times == 1:
            print(f"Your dragon leveled up 1 time and is now level {level}!")
        if times == 2:
            print(f"Your dragon level up {times} times and is now level {level}!")
        self.exp += exp
        self.level = level
        return 0

    def equals(self, dragon):
        """Checks if two dragon objects have the same name (which means they are equal)"""
        return dragon.name == self.name

    def string_equals(self, name):
        """Checks if one string has the same string as the name of the dragon."""
        return name == self.name

    def get_dragon_dictionary(self):
        """Returns a dictionary object of all of the information for this dragon."""
        dict = {"name": self.name,
                "element": self.element,
                "exp": self.exp,
                "level": self.level,
                "boss_number": self.boss_number,
                "prestige": self.prestige,
                "boss3_number": self.boss3_number,
                "story_number": self.story_number
        }
        return dict

    def reset(self):
        """Resets the dragons stats to default"""
        self.exp = 0
        self.level = 1
        self.boss_number = 1
        self.prestige = 1
        self.boss3_number = 1
        self.story_number = 1
        self.moves = []
        self.forms = []
        self.check_moves_and_forms(self.config_reader)

    def get_file_lines(self):
        """Gets a list of each line of this Dragon."""
        lines = [
            f"{self.moves[0].name}\n",
            f"{self.element}\n",
            f"{self.level}\n",
            f"{self.prestige}"
        ]
        return {"name": f"{self.name}.txt", "lines": lines}


def create_dragon_with_dict(dict, config_reader):
    """Returns a dragon object based on a dictionary."""
    return Dragon(dict["name"], dict["element"], config_reader, dict["level"], dict["prestige"], dict["boss_number"], dict["boss3_number"], dict["story_number"], dict["exp"])
