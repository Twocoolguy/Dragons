import os

from FileActions import create_folder, read_file_lines_in_folder, delete_file
import json
from Dragon import create_dragon_with_dict


class User:
    def __init__(self, name, config_reader):
        self.name = name
        self.dragons = []
        self.config_reader = config_reader
        if self.name == "default":
            self.path = f"{config_reader.normal_path}/Dragons/"
        else:
            self.path = f"{config_reader.normal_path}/Dragons/{self.name}/"
        self.achievements = []

    def create(self):
        """Basically creates the folder where the dragons are stored."""
        if self.name == "default":
            return -1
        err1 = create_folder(self.path)
        if err1 == -1:
            return -2
        err2 = create_folder(f"{self.path}data/")
        if err2 == -1:
            return -3
        with open(f"{self.path}data/data.json", "w+") as f:
            json.dump(self.achievements, f)
            return 0

    def equals(self, user):
        """Basically checks if self object and user object are equal user objects."""
        return user.name == self.name

    def string_equals(self, name):
        """Checks if a string is equal to a user object name."""
        return name == self.name

    def get_achievements(self):
        """Gets the achievement numbers in the data.json file."""
        if self.name == "default":
            return 1
        try:
            with open(f"{self.path}data/data.json", "r") as f:
                self.achievements = json.load(f)
                return 0
        except FileNotFoundError:
            return -1

    def add_achievement(self, achievement):
        """Adds an the given achievements number to the achievements list, and adds it to the file."""
        if self.name == "default":
            return 1
        err = self.get_achievements()
        if err == -1:
            return -2
        try:
            with open(f"{self.path}data/data.json", "w+") as f:
                self.achievements.append(achievement.number)
                json.dump(self.achievements, f)
                return 0
        except FileNotFoundError:
            return -1

    def check_achievements(self):
        """Checks to see if an achievement has been made."""
        if self.name == "default":
            return -1
        self.get_dragons()
        for achievement in self.config_reader.achievements:
            fail = True
            for index in range(0, len(achievement.actions)):
                action = achievement.actions[index]
                last = False
                if len(achievement.actions)-1 == index:
                    last = True
                if action == "level":
                    number = achievement.numbers[index]
                    ifail = True
                    for dragon in self.dragons:
                        if dragon.level >= number:
                            ifail = False
                            if last:
                                fail = False
                            break
                    if not ifail:
                        continue
                    else:
                        break
                if action == "created":
                    if len(self.dragons) > 0:
                        if last:
                            fail = False
                            break
                    else:
                        break
                if action == "createu":
                    if last:
                        fail = False
                        break
                    continue
                if action == "prestige":
                    number = achievement.numbers[index]
                    ifail = True
                    for dragon in self.dragons:
                        if dragon.prestige >= number:
                            ifail = False
                            if last:
                                fail = False
                            break
                    if not ifail:
                        continue
                    else:
                        break
                if action == "exp":
                    number = achievement.numbers[index]
                    ifail = True
                    for dragon in self.dragons:
                        if dragon.exp >= number:
                            ifail = False
                            if last:
                                fail = False
                            break
                    if not ifail:
                        continue
                    else:
                        break
                if action == "boss":
                    number = achievement.numbers[index]
                    ifail = True
                    for dragon in self.dragons:
                        if dragon.boss >= number:
                            ifail = False
                            if last:
                                fail = False
                            break
                    if not ifail:
                        continue
                    else:
                        break
                if action == "boss3":
                    number = achievement.numbers[index]
                    ifail = True
                    for dragon in self.dragons:
                        if dragon.boss3_number >= number:
                            ifail = False
                            if last:
                                fail = False
                            break
                    if not ifail:
                        continue
                    else:
                        break
                if action == "story":
                    number = achievement.numbers[index]
                    ifail = True
                    for dragon in self.dragons:
                        if dragon.story_number >= number:
                            ifail = False
                            if last:
                                fail = False
                            break
                    if not ifail:
                        continue
                    else:
                        break
            if not fail:
                print(achievement.message)
                self.add_achievement(achievement)

    def get_dragons(self):
        """Gets all of the dragons in the user folder."""
        if not os.path.exists(self.path):
            os.mkdir("Dragons")
        dragon_files = read_file_lines_in_folder(self.path)
        try:
            int(dragon_files)
            return int(dragon_files)
        except TypeError:
            try:
                for dragon_file in dragon_files:
                    with open(f"{self.path}{dragon_file['name']}", "r") as f:
                        dragon_dict = json.load(f)
                        for drag in self.dragons:
                            if drag.name == dragon_dict["name"]:
                                self.dragons.remove(drag)
                                break
                        self.dragons.append(create_dragon_with_dict(dragon_dict, self.config_reader))
            except FileNotFoundError:
                return -2 + -1000

        return 0

    def get_dragon(self, name):
        """Gets a specific dragon a user has by name."""
        for dragon in self.dragons:
            if dragon.name == name:
                return dragon
        return None

    def add_dragon(self, dragon):
        """Adds a dragon."""
        err = self.get_dragons()
        if err == -1:
            return -1
        for drag in self.dragons:
            if dragon.equals(drag):
                return -2
        if err == -1:
            return -3
        try:
            with open(f"{self.path}{dragon.name}.json", "r") as f:
                return -5
        except FileNotFoundError:
            with open(f"{self.path}{dragon.name}.json", "w+") as f:
                json.dump(dragon.get_dragon_dictionary(), f)
                self.dragons.append(dragon)
                return 0

    def modify_dragon(self, dragon):
        """Modifies the given dragon from the user. First it checks if it is from the user though."""
        if dragon not in self.dragons:
            return -1

        dragon_file = f"{self.path}{dragon.name}.json"
        with open(f"{dragon_file}", "w+") as f:
            json.dump(dragon.get_dragon_dictionary(), f)

        return 0

    def delete_dragon(self, dragon):
        """Deletes the given dragon from the user."""
        if not dragon in self.dragons:
            return -1

        dragon_file = f"{self.path}{dragon.name}.json"
        err = delete_file(dragon_file)
        if err == -1:
            return -2
        self.dragons.remove(dragon)
        return 0

    def delete_dragons(self):
        for dragon in self.dragons:
            err = self.delete_dragon(dragon)
            if err != 0:
                return dragon.name

        return "Done"

    def reset_achievements(self):
        """Resets the users achievements."""
        if self.name == "default":
            return -1
        with open(f"{self.path}data/data.json", "w+") as f:
            self.achievements = []
            json.dump(self.achievements, f)
            return 0

    def reset_all(self):
        """This resets everything from the user."""
        err1 = self.delete_dragons()
        if not self.name == "default":
            err2 = self.reset_achievements()
        if err1 != "Done":
            return err1
        if err2 != 0:
            return err2 -10000
        return 0

    def rename_dragon(self, name, new_name):
        """Renames a dragon with the given name to the new name"""
        for dragon in self.dragons:
            if dragon.name == name:
                dragon.name = new_name
                self.modify_dragon(dragon)
                break
