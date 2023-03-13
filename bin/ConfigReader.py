import os

import FileActions
from Moves import Move
from Form import Form
from Achievement import Achievement
from BossMove import BossMove
from Boss import Boss
from Story import Story
from Dialogue import Dialogue
from Dragon import Dragon


class ConfigReader:
    """This basically reads the config and gets data for everything."""
    def __init__(self, config_path):
        self.config_path = config_path
        gset = config_path.split("/")
        gset.pop()
        self.normal_path = "/".join(gset)
        self.exp_multi = int(FileActions.get_text_at_line(f"{config_path}/Other/expcalcmultiplier.txt", 1))
        self.font_size = int(FileActions.get_text_at_line(f"{config_path}/Other/fontsize.txt", 1))
        self.health_multi = int(FileActions.get_text_at_line(f"{config_path}/Other/healthmultiplier.txt", 1))
        self.max_prestige = int(FileActions.get_text_at_line(f"{config_path}/Other/maxprestige.txt", 1))
        self.version = FileActions.get_text_at_line(f"{config_path}/Other/ver.txt", 1)
        self.bosshealth_multiplier = int(FileActions.get_text_at_line(f"{config_path}/Other/bosshealthmultiplier.txt", 1))
        self.achievement_actions = ["level",
                                    "created",
                                    "createu",
                                    "prestige",
                                    "exp",
                                    "boss",
                                    "boss3",
                                    "story"
        ]  # This is a list of all of the valid actions for achievements.
        self.achievement_action_numbers = ["level",
                                          "prestige",
                                          "exp",
                                          "boss",
                                          "boss3",
                                          "story"
        ]  # This is a list of all of the actions that can use the numbers.
        move_files = FileActions.read_file_lines_in_folder(f"{config_path}/Moves/")
        moves_list = []
        for move_file in move_files:
            move_name = move_file["name"][0:move_file["name"].index(".")]
            move_element = move_file["lines"][1]
            move_damage = move_file["lines"][2]
            move_accuracy = move_file["lines"][3]
            move_level_required = move_file["lines"][4]
            move_unlock = move_file["lines"][5]
            move = {
                "name": move_name,
                "element": move_element,
                "damage": move_damage,
                "accuracy": move_accuracy,
                "level_required": move_level_required,
                "unlock": move_unlock
                    }
            moves_list.append(move)
        self.moves = []
        for move in moves_list:
            self.moves.append(Move(move["name"],
                                   move["element"],
                                   move["damage"],
                                   move["accuracy"],
                                   move["level_required"],
                                   move["unlock"]))
        element_files = FileActions.read_file_lines_in_folder(f"{config_path}/Elements/")
        self.elements = []
        for element_file in element_files:
            self.elements.append(element_file["name"][0:element_file["name"].index(".")])

        forms_folders = FileActions.read_folder_in_folder(f"{config_path}/Forms/")
        self.forms = []
        for form_folder in forms_folders:
            element = form_folder.lower()
            form_files = FileActions.read_file_lines_in_folder(f"{config_path}/Forms/{form_folder}/")
            for form_file in form_files:
                self.forms.append(Form(form_file["name"][0:form_file["name"].index(".")],
                                       int(form_file["lines"][0]),
                                       int(form_file["lines"][1]),
                                       element))

        self.achievements = []
        achievement_files = FileActions.read_file_lines_in_folder(f"{config_path}/Achievements/")
        for achievement_file in achievement_files:
            actions = []
            if "," in achievement_file['lines'][0]:
                actions = achievement_file["lines"][0].split(",")
            else:
                actions.append(achievement_file["lines"][0])

            numbers = []
            if "," in achievement_file["lines"][1]:
                numbers = [int(x) for x in achievement_file["lines"][1].split(",")]
            else:
                numbers.append(int(achievement_file["lines"][1]))
            number = achievement_file["name"][0:achievement_file["name"].index(".")]
            self.achievements.append(Achievement(actions, numbers, achievement_file["lines"][2], int(number)))

        boss_move_files = FileActions.read_file_lines_in_folder(f"{config_path}/DragonBosses/Moves/")
        self.boss_moves = []
        for boss_move_file in boss_move_files:
            self.boss_moves.append(BossMove(boss_move_file["lines"][0],
                                       int(boss_move_file["lines"][1]),
                                       int(boss_move_file["lines"][2])))

        boss_files = FileActions.read_file_lines_in_folder(f"{config_path}/DragonBosses/")
        self.bosses = []
        for boss_file in boss_files:
            name = boss_file["lines"][0]
            level = int(boss_file["lines"][1])
            move_str = boss_file["lines"][2]
            move = None
            boss_number = int(boss_file["lines"][3])
            for boss_move in self.boss_moves:
                if boss_move.name == move_str:
                    move = boss_move
                    break
            self.bosses.append(Boss(name, level, move, boss_number))


        boss_move_files3 = FileActions.read_file_lines_in_folder(f"{config_path}/DragonBosses3/Moves/")
        self.boss_moves3 = []
        for boss_move_file3 in boss_move_files3:
            self.boss_moves3.append(BossMove(boss_move_file3["lines"][0],
                                       int(boss_move_file3["lines"][1]),
                                       int(boss_move_file3["lines"][2])))

        boss_files3 = FileActions.read_file_lines_in_folder(f"{config_path}/DragonBosses3/")
        self.bosses3 = []
        for boss_file3 in boss_files3:
            name = boss_file3["lines"][0]
            level = int(boss_file3["lines"][1])
            move_str = boss_file3["lines"][2]
            move = None
            boss_number = int(boss_file3["lines"][3])
            for boss_move3 in self.boss_moves3:
                if boss_move3.name == move_str:
                    move = boss_move3
                    break
            b3 = Boss(name, level, move, boss_number)
            b3.boss3 = True
            self.bosses3.append(b3)

        self.stories = []
        story_order_files = FileActions.read_file_lines_in_folder(f"{config_path}/Story/Order/")
        story_boss_moves_files = FileActions.read_file_lines_in_folder(f"{config_path}/Story/Bosses/Moves/")
        story_boss_moves = []
        for story_boss_move_file in story_boss_moves_files:
            boss_move_name = story_boss_move_file["name"][0:story_boss_move_file["name"].index(".")]
            boss_move_damage = int(story_boss_move_file['lines'][0])
            boss_move_accuracy = int(story_boss_move_file['lines'][0])
            story_boss_moves.append(BossMove(boss_move_name, boss_move_damage, boss_move_accuracy))
        self.story_boss_moves = story_boss_moves
        story_boss_files = FileActions.read_file_lines_in_folder(f"{config_path}/Story/Bosses/")
        story_bosses = []
        for story_boss_file in story_boss_files:
            name = story_boss_file["name"][0:story_boss_file["name"].index(".")]
            level = int(story_boss_file["lines"][0])
            move = None
            for story_boss_move in story_boss_moves:
                if story_boss_move.string_equals(story_boss_file['lines'][1]):
                    move = story_boss_move
                    break
            story_bosses.append(Boss(name, level, move))
        self.story_bosses = story_bosses
        story_dialogues = FileActions.read_file_lines_in_folder(f"{config_path}/Story/Dialogue/")

        story_dragon_move_files = FileActions.read_file_lines_in_folder(f"{config_path}/Story/Dragons/Moves")
        story_dragon_moves = []
        for story_dragon_move_file in story_dragon_move_files:
            name = story_dragon_move_file["name"][0:story_dragon_move_file["name"].index(".")]
            damage = int(story_dragon_move_file["lines"][0])
            accuracy = int(story_dragon_move_file["lines"][1])
            element = story_dragon_move_file["lines"][2]
            story_dragon_moves.append(Move(name, element, damage, accuracy, 0, 0))
        self.story_dragon_moves = story_dragon_moves
        story_dragon_files = FileActions.read_file_lines_in_folder(f"{config_path}/Story/Dragons/")
        story_dragons = []
        for story_dragon_file in story_dragon_files:
            name = story_dragon_file["name"][0:story_dragon_file["name"].index(".")]
            move = None
            for story_dragon_move in story_dragon_moves:
                if story_dragon_move.string_equals(story_dragon_file['lines'][0]):
                    move = story_dragon_move
                    break

            element = story_dragon_file["lines"][1]
            level = int(story_dragon_file["lines"][2])
            prestige = int(story_dragon_file["lines"][3])
            dragon = Dragon(name, element, self, level, prestige)
            dragon.moves = [move]
            story_dragons.append(dragon)
        self.story_dragons = story_dragons
        for story_order_file in story_order_files:
            name = story_order_file["name"][0:story_order_file["name"].index(".")]
            dialogue_str = story_order_file["lines"][0]
            fight = story_order_file["lines"][1]
            fight_dragon_str = story_order_file["lines"][2]
            fight_boss_str = story_order_file["lines"][3]
            dialogue = None
            for dialog in story_dialogues:
                if dialog["name"][0:dialog["name"].index(".")] == dialogue_str:
                    dialogue = Dialogue(dialogue_str, dialog["lines"][0])
                    break
            dragon = None
            if not fight_dragon_str == "none":
                for story_dragon in story_dragons:
                    if story_dragon.name == fight_dragon_str:
                        dragon = story_dragon
                        break
            boss = None
            if not fight_boss_str == "none":
                for story_boss in story_bosses:
                    if story_boss.name == fight_boss_str:
                        boss = story_boss
                        break
            self.stories.append(Story(name, boss, dragon, dialogue))

    def get_boss(self, number):
        """Gets a boss by the number."""
        for boss in self.bosses:
            if boss.boss_number == number:
                return boss
        return None

    def get_story(self, number):
        """Gets a story by the number."""
        for story in self.stories:
            if story.name == str(number):
                return story
        return None

    def get_boss3(self, number):
        """Gets a boss3 by the number."""
        for boss3 in self.bosses3:
            if boss3.boss_number == number:
                return boss3
        return None

    def set_boss_health_mult(self, number):
        """Sets the boss health multiplier number. This is only used for create.py"""
        err = FileActions.overwrite_file(self.config_path + "/Other/bosshealthmultiplier.txt", str(number))
        if err == -1:
            print("File location not found. There may be an issue with your config.")
        else:
            print(f"Set boss health multiplier from {self.bosshealth_multiplier} to {number}!")

    def set_exp_calc_mult(self, number):
        """Sets the exp calc multiplier number. This is only used for create.py"""
        err = FileActions.overwrite_file(self.config_path + "/Other/expcalcmultiplier.txt", str(number))
        if err == -1:
            print("File location not found. There may be an issue with your config.")
        else:
            print(f"Set exp calc multiplier from {self.exp_multi} to {number}!")

    def _set_fontsize(self, number):
        """Sets the fontsize number. This is only used for create.py"""
        err = FileActions.overwrite_file(self.config_path + "/Other/fontsize.txt", str(number))
        if err == -1:
            print("File location not found. There may be an issue with your config.")
        else:
            print(f"Set font size from {self.font_size} to {number}!")

    def set_health_multi(self, number):
        """Sets the health multiplier number. This is only used for create.py"""
        err = FileActions.overwrite_file(self.config_path + "/Other/healthmultiplier.txt", str(number))
        if err == -1:
            print("File location not found. There may be an issue with your config.")
        else:
            print(f"Set health multiplier from {self.health_multi} to {number}!")

    def set_max_prestige(self, number):
        """Sets the max prestige number. This is only used for create.py"""
        err = FileActions.overwrite_file(self.config_path + "/Other/maxprestige.txt", str(number))
        if err == -1:
            print("File location not found. There may be an issue with your config.")
        else:
            print(f"Set max prestige from {self.max_prestige} to {number}!")

    def isElement(self, element):
        """Checks if the element parameter is an element already."""
        for ele in self.elements:
            if element == ele:
                return True
        return False

    def isForm(self, element, form):
        """Checks if the given form is already a thing in the given element."""
        for f in self.forms:
            if f.element == element:
                if f.name == form:
                    return True
        return False

    def isMove(self, element, move_name):
        """Checks with the given information if this is already a move."""
        for move in self.moves:
            if move.name == move_name:
                if element == move.element:
                    return True
        return False

    def create_form(self, element, form_name, form_mult, form_levelreq):
        """Creates a form with the given info."""
        form = Form(form_name, form_mult, form_levelreq, element)
        form_path = f"{self.config_path}/Forms/{element}/{form_name}.txt"
        FileActions.create_file(form_path)
        FileActions.overwrite_file_lines(form_path, form.get_file_lines()["lines"])
        print("Created form!")

    def create_move(self, name, element, damage, accuracy, level_needed, unlock):
        """Creates a move with the given info."""
        move = Move(name, element, damage, accuracy, level_needed, unlock)
        move_path = f"{self.config_path}/Moves/{name}.txt"
        FileActions.create_file(move_path)
        FileActions.overwrite_file_lines(move_path, move.get_file_lines()["lines"])
        print("Created move!")

    def isBossMove(self, name):
        """Checks if the given name is a boss move."""
        boss_movepath = f"{self.config_path}/DragonBosses/Moves/{name}.txt"
        if os.path.exists(boss_movepath):
            return True
        return False

    def get_new_boss_number(self):
        """Fetches the next possible boss number."""
        boss_path = f"{self.config_path}/DragonBosses/"
        return len(os.listdir(boss_path))

    def get_boss_move(self, name):
        """Gets the boss move with the given name. If it does not exists returns none"""
        for mv in self.boss_moves:
            if mv.name == name:
                return mv
        return None

    def create_boss(self, name, level, move, unlock):
        """This creates a new boss file."""
        boss = Boss(name, level, self.get_boss_move(move), unlock)
        boss_path = f"{self.config_path}/DragonBosses/{unlock}.txt"
        FileActions.create_file(boss_path)
        FileActions.overwrite_file_lines(boss_path, boss.get_file_lines()["lines"])
        print("Created boss!")

    def isBossMove3(self, name):
        """Checks if the given name is a boss3 move"""
        boss3_movepath = f"{self.config_path}/DragonBosses3/Moves/{name}.txt"
        if os.path.exists(boss3_movepath):
            return True
        return False

    def get_new_boss3_number(self):
        """Fetches the next possible boss3 number."""
        boss3_path = f"{self.config_path}/DragonBosses3/"
        return len(os.listdir(boss3_path))

    def get_boss3_move(self, name):
        """Gets the boss move with the given name. If it does not exists returns none"""
        for mv in self.boss_moves3:
            if mv.name == name:
                return mv
        return None

    def create_boss3(self, name, level, move, unlock):
        """This creates a new boss3 file."""
        boss = Boss(name, level, self.get_boss3_move(move), unlock)
        boss_path = f"{self.config_path}/DragonBosses3/{unlock}.txt"
        FileActions.create_file(boss_path)
        FileActions.overwrite_file_lines(boss_path, boss.get_file_lines()["lines"])
        print("Created boss3!")

    def create_boss_move(self, name, damage, accuracy):
        """This creates a new boss move file."""
        boss_move = BossMove(name, damage, accuracy)
        boss_move_path = f"{self.config_path}/DragonBosses/Moves/{name}.txt"
        FileActions.create_file(boss_move_path)
        FileActions.overwrite_file_lines(boss_move_path, boss_move.get_file_lines()["lines"])
        print("Created boss move!")

    def create_boss3_move(self, name, damage, accuracy):
        """This creates a new boss3 move file."""
        boss_move = BossMove(name, damage, accuracy)
        boss_move_path = f"{self.config_path}/DragonBosses3/Moves/{name}.txt"
        FileActions.create_file(boss_move_path)
        FileActions.overwrite_file_lines(boss_move_path, boss_move.get_file_lines()["lines"])
        print("Created boss3 move!")

    def get_next_ach_number(self):
        """This gets the next number achievements"""
        return len(self.achievements) + 1

    def create_achievement(self, actions, numbers, message):
        """This creates a new achievement file."""
        ach_number = self.get_next_ach_number()
        ach = Achievement(actions, numbers, message, ach_number)
        ach_path = f"{self.config_path}/Achievements/{ach_number}.txt"
        FileActions.create_file(ach_path)
        FileActions.overwrite_file_lines(ach_path, ach.get_file_lines()["lines"])
        print("Created new achievement!")
# cr = ConfigReader("C:/Users/TurtlesAreHot/Desktop/Dragons e/Config")
