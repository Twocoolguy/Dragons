import os

import FileActions
from ConfigReader import ConfigReader
import Getter
from User import User
from Dragon import Dragon
from fight import start_fight, gen_rand, boss3_start


class RunMustBeByMainError(Exception):
    """Error raised when the file must be runned by main."""


class GUI:
    def __init__(self, config_location):
        self.config_reader = ConfigReader(config_location)
        self._setup()

    def _setup(self):
        """Helps setup Commandline."""
        # Font setup will be available in the future.
        return None

    def start(self):
        last_cmd_special = False
        move_s = None
        drag_s = None
        form_s = None
        formes = []
        drages = []
        movees = []
        old_cmd = ""
        print(f"Welcome to Dragons {self.config_reader.version} in Python. Type help to see all commands.")
        user = User("default", self.config_reader)
        user.get_dragons()
        while True:
            if user.name != "default":
                user.get_achievements()
            user.get_dragons()
            command = input("Command (q to quit): ")
            args = []
            if command != "boss" and command != "fight" and command != "boss3" and command != "":
                last_cmd_special = False
                move_s = None
                drag_s = None
                form_s = None
                movees = []
                drages = []
                formes = []
            if " " in command:
                args = command.split(" ")
                args.pop(0)
            if command == "q":
                print("q Exit.")
                exit(0)
            elif command == "help":
                print("help - lists all of the different commands and what they do.")
                print("tutorial - explains simple functions of the game.")
                print("fight - initiates a fight with a CPU dragon.")
                print("boss - initiates a fight with a boss CPU dragon.")
                print("boss3 - initiates a fight with 3 of your dragons against a boss3 CPU dragon.")
                print("story - starts the story on the dragon you input.")
                print("users - lists all of the different users.")
                print("setuser - allows you to choose a user to set to.")
                print("logout - allows you to logout of a user.")
                print("createdragon - allows you to create a dragon.")
                print("deletedragon - allows you to delete a dragon.")
                print("createuser - allows you to create a user.")
                print("deleteuser - allows you to delete a user.")
                print("renameuser - allows you to rename a user.")
                print("userinfo - gets you information about a user name you input.")
                print("achievements - lists all the achievements with all of their requirements and messages (spoiler warning).")
                print("dragonprestige - allows you to prestige a dragon of your choosing.")
                print("dragons - lists all of the dragons under the current user you are on.")
                print("dragoninfo - gets you information about a dragon name you input.")
                print("dragonreset - resets a dragon to its default stats.")
                print("deletedragons - deletes all of a user (or in the logged out state) dragons.")
                print("dragonrename - allows you to rename a dragon.")
                print("dragonmove - allows you to move a dragon to a different user.")
                print("movedragons - allows you to move all of your dragons to a different user.")
                print("userreset - resets everything about your user, deletes all dragons, and resets achievement stats.")
                print("achievementreset - resets all achievement stats about the user.")
                print("properties - lists information about the program and some of the numbers for the game.")
                print("elements - lists all of the elements.")
                print("moves - lists all of the moves.")
                print("bosses - lists all of the bosses.")
                print("bosses3 - lists all of the boss3 bosses.")
                print("quests - lists information about stories. Mainly how much of each statistic is in story mode. (Slight Spoiler warning).")
                print("moveinfo - gets you information about a move you input (spoiler warning).")
                print("bossinfo - gets you information about a boss you input (spoiler warning).")
                print("boss3info - gets you information about a boss3 you input (spoiler warning).")
                print("storyinfo - gets you information about a story number you input (spoiler warning).")
                print("checkachievements - checks and sees if your dragons have completed any achievements and that it needed updating.")
            elif command == "users":
                Getter.get_users(self.config_reader.normal_path)
            elif command == "setuser":
                users = Getter.get_user_list(self.config_reader.normal_path)
                users.remove("default")
                if len(users) == 0:
                    print("There is no user to set to! Use the createuser command to create a user.")
                    continue
                if len(users) == 1:
                    print("There is only one user, so we set your user to that.")
                    user = User(users[0], self.config_reader)
                    continue
                print(users)
                print("Pick a user you want to be.")
                while True:
                    user_choice = input("User (q to quit): ")
                    if user_choice == "q":
                        print("Exited the picking of a user on request.")
                        break
                    if user_choice not in users:
                        print("This is not one of the users that exists. Please try again, or type q to exit and create the user with the createuser command.")
                        continue
                    user = User(user_choice, self.config_reader)
            elif command == "logout":
                if user.name != "default":
                    con = True
                    while True:
                        sure = input("Are you sure you want to logout (y or n)? ")
                        if sure == "n":
                            con = False
                            break
                        elif sure == "y":
                            con = True
                            break
                    if con:
                        user = User("default", self.config_reader)
                        print("Logged out. Use setuser to login.")
                    else:
                        print("Canceled logout.")
                else:
                    print("You are not logged in. Login with the setuser command.")
                    continue
            elif command == "createdragon":
                name = ""
                element = ""
                while True:
                    name = input("Dragon Name: ")
                    check_drag = Dragon(name, element, self.config_reader)
                    for dragon in user.dragons:
                        if dragon.equals(check_drag):
                            print("Dragon with this name already exists. Please choose a different one.")
                            continue
                    break

                while True:
                    element = input("Element: ")
                    if element in self.config_reader.elements:
                        break

                drag = Dragon(name, element, self.config_reader)
                user.add_dragon(drag)
                print(f"Created a dragon named {drag.name} under the user profile {user.name}!")
            elif command == "deletedragon":
                if len(user.dragons) == 0:
                    print("You do not have any dragons to delete. Create a dragon by using the command createdragon")
                    continue
                name = ""
                fail = False
                con = True
                while con:
                    name = input("Dragon Name (q to quit): ")
                    if name == "q":
                        fail = True
                        break
                    for dragon in user.dragons:
                        if dragon.string_equals(name):
                            fail = False
                            con = False
                    if con is False:
                        break
                    print("There is no dragon with this name under your user. Are you under the correct user? Try again.")
                cancel = False
                if not fail:
                    while True:
                        sure = input(f"Are you sure you want to delete the dragon {name} (y or n)? ")
                        if sure == "y":
                            cancel = False
                            break
                        elif sure == "n":
                            cancel = True
                            break
                    if not cancel:
                        user.delete_dragon(user.get_dragon(name))
                        print("We deleted the dragon!")
                    else:
                        print("You canceled the deletion of this dragon. If you want to delete another dragon, rerun the command.")
                        continue
            elif command == "createuser":
                while True:
                    name = input("Name (q to quit): ")
                    if name == "q":
                        break
                    users = Getter.get_user_list(self.config_reader.normal_path)
                    if name in users:
                        print("A user with this name already exists. Please choose another one.")
                        continue
                    break
                if name == "q":
                    continue
                us = User(name, self.config_reader)
                us.create()
                user = us
                print("We have created this user, and logged you in as it!")
            elif command == "deleteuser":
                u_l = Getter.get_user_list(self.config_reader.normal_path)
                u_l.remove("default")
                if len(u_l) == 0:
                    print("You do not have any users you can delete.")
                    continue
                while True:
                    name = input("Name: (q to quit): ")
                    if name == "q":
                        break
                    users = Getter.get_user_list(self.config_reader.normal_path)
                    users.remove('default')
                    if name not in users:
                        print("There is no user with this name that exists. Please give another name.")
                        continue
                    break
                if name == "q":
                    continue
                while True:
                    sure = input("Are you sure you want to delete this user (y or n) This also deletes all of their data and dragons and after deleting it, it is NOT retrievable.? ")
                    if sure == "y" or sure == "n":
                        break
                    print("Invalid input has been given. Only reply with y or n")

                if sure == "n":
                    print("You have aborted the deletion of this user.")
                    continue
                if user.name == name:
                    user = User("default", self.config_reader)
                    print("Since you are logged in as this user, we have logged you out of them.")
                Getter.delete_user(name, self.config_reader.normal_path)
                print("We deleted this user!")
            elif command == "renameuser":
                u_l = Getter.get_user_list(self.config_reader.normal_path)
                u_l.remove("default")
                if len(u_l) == 0:
                    print("You do not have any users to rename")
                    continue
                while True:
                    name = input("User to rename (q to quit): ")
                    if name == "q":
                        break
                    users = Getter.get_user_list(self.config_reader.normal_path)
                    users.remove("default")
                    if name not in users:
                        print("This name is not in the users list. Please try again.")
                        continue
                    break
                if name == "q":
                    continue
                while True:
                    new_name = input("New Name (q to quit): ")
                    if new_name == "q":
                        break
                    users = Getter.get_user_list(self.config_reader.normal_path)
                    if new_name in users:
                        print("A user with this name already exists. Please choose a different one.")
                        continue
                    break
                if new_name == "q":
                    continue
                Getter.user_rename(name, new_name, self.config_reader)
                print("Renamed the user!")
            elif command == "userinfo":
                u_l = Getter.get_user_list(self.config_reader.normal_path)
                u_l.remove("default")
                if len(u_l) == 0:
                    print("There is no users to get the info of.")
                    continue
                while True:
                    name = input("User (q to quit): ")
                    if name == "q":
                        break
                    users = Getter.get_user_list(self.config_reader.normal_path)
                    users.remove("default")
                    if name not in users:
                        print("This is not a real user. Please try again.")
                        continue
                    break

                if name == "q":
                    continue

                usr = User(name, self.config_reader)
                usr.get_dragons()
                usr.get_achievements()
                print(f"Name: {usr.name}")
                print(f"Achievements Completed: {len(usr.achievements)}")
                print("Dragons: ")
                if len(usr.dragons) == 0:
                    print("User has no dragons.")
                    continue
                for dragon in usr.dragons:
                    print(f"{dragon.name} (Element: {dragon.element}) - Level {dragon.level}")
            elif command == "achievements":
                if len(self.config_reader.achievements) == 0:
                    print("There is no achievements.")
                    continue
                for y in range(1, len(self.config_reader.achievements)+1):
                    achievement = Getter.get_achievement(y, self.config_reader)
                    print(f"{achievement.number}# - {achievement.message}")
                    print("Requirements")
                    for x in range(0, len(achievement.actions)):
                        action = achievement.actions[x]
                        print(f"{action}", end="")
                        if action in self.config_reader.achievement_action_numbers:
                            print(f"- {achievement.numbers[x]}", end="")
                        print("")
            elif command == "dragonprestige":
                if len(user.dragons) == 0:
                    print("You do not have any dragons you can prestige.")
                    continue
                while True:
                    name = input("Dragon to Prestige (q to quit): ")
                    if name == "q":
                        break
                    drag = user.get_dragon(name)
                    if drag is None:
                        print("This is not a dragon the user has. Please try again.")
                        continue
                    break
                if name == "q":
                    continue
                err = drag.prestige_up()
                if err == -1:
                    print("This dragon is already the max prestige it can be.")
                    continue
                if err == -2:
                    print("This dragon is not high enough level to prestige. Your dragon must be level 3000.")
                    continue
                user.modify_dragon(drag)
                print("Success! Prestiged your dragon!")
            elif command == "dragons":
                if len(user.dragons) == 0:
                    print("You do not have any dragons.")
                    continue
                for drag in user.dragons:
                    print(f"{drag.name} - {drag.element}")
                print("Use dragoninfo command to get information about a specific dragon.")
            elif command == "dragoninfo":
                if len(user.dragons) == 0:
                    print("You do not have any dragons to check the info for.")
                    continue
                while True:
                    name = input("Dragon Name (q to quit): ")
                    if name == "q":
                        break
                    drag = user.get_dragon(name)
                    if drag is None:
                        print("This dragon does not exist in the current user you are logged into. Try again")
                        continue
                    break
                if name == "q":
                    continue
                print(f"{drag.name}")
                print(f"Element: {drag.element}")
                print(f"Level: {drag.level}")
                print(f"Exp: {drag.exp}")
                print(f"Prestige: {drag.prestige}")
                print(f"Boss Number: {drag.boss_number}")
                print(f"Boss3 Number: {drag.boss3_number}")
                print(f"Story Number: {drag.story_number}")

            elif command == "dragonreset":
                if len(user.dragons) == 0:
                    print("You do not have any dragons to reset.")
                    continue
                while True:
                    name = input("Dragon Name: (q to quit): ")
                    if name == "q":
                        break
                    drag = user.get_dragon(name)
                    if drag is None:
                        print("This dragon does not exist in the current user you are logged into. Try again")
                        continue
                    break
                if name == "q":
                    continue
                while True:
                    sure = input("Are you sure you want to reset your dragon? There is no way to undo this. (y or n): ")
                    if sure == "y":
                        break
                    if sure == "n":
                        break
                if sure == "n":
                    print("Resetting of dragon aborted.")
                    continue
                if sure == "y":
                    for drg in user.dragons:
                        if drg.name == drag.name:
                            drg.reset()
                            user.modify_dragon(drg)
                            break
                    print("Reset the dragon to default stats.")
            elif command == "deletedragons":
                if len(user.dragons) == 0:
                    print("You do not have any dragons to delete.")
                    continue
                while True:
                    sure = input(f"You are about to delete all of your dragons in the user {user.name}. Are you sure you want to proceed? There is no retrieving this data after you do this. (y or n): ")
                    if sure == "y":
                        break
                    if sure == "n":
                        break
                if sure == "n":
                    print("Aborted deletion of all user dragons.")
                    continue
                if sure == "y":
                    while True:
                        supersure = input(f"This is your last chance. Are you sure you want to delete {user.name}'s dragons? You will not be able to retrieve this! (y or n): ")
                        if supersure == "y":
                            break
                        if supersure == "n":
                            break
                    if supersure == "n":
                        print("Aborted deletion of all user dragons.")
                        continue
                    if supersure == "y":
                        user.delete_dragons()
                        print(f"Deleted {user.name}'s dragons.")
            elif command == "dragonrename":
                if len(user.dragons) == 0:
                    print("You cannot rename a dragon because you do not have any.")
                while True:
                    name = input("Dragon Name (q to quit): ")
                    if name == "q":
                        break
                    drag = user.get_dragon(name)
                    if drag is None:
                        print(f"This is not a dragon that exists for the user {user.name}. Please try again.")
                        continue
                    break
                if name == "q":
                    continue
                while True:
                    new_name = input("New Name (q to quit): ")
                    if new_name == "q":
                        break
                    dr = user.get_dragon(new_name)
                    if dr is not None:
                        print(f"A dragon with the name {new_name} already exists under {user.name}'s profile. Please choose another name.")
                        continue
                    break
                if new_name == "q":
                    continue
                while True:
                    sure = input(f"Are you sure you want to rename the dragon {name} to {new_name} under the profile {user.name} (y or n): ")
                    if sure == "y":
                        break
                    if sure == "n":
                        break
                if sure == "n":
                    print("Aborted rename.")
                    continue
                if sure == "y":
                    Getter.dragon_rename(name, new_name, user)
                    user.rename_dragon(name, new_name)
                    print("Renamed the dragon!")
            elif command == "dragonmove":
                if len(user.dragons) == 0:
                    print("You do not have any dragons you can move.")
                    continue
                u_l = Getter.get_user_list(self.config_reader.normal_path)
                u_l.remove(user.name)
                if len(u_l) == 0:
                    print("There is not any other users you can move this dragon to.")
                    continue
                while True:
                    usr_name = input("User to Move to (q to quit): ")
                    if usr_name == "q":
                        break
                    usr_list = Getter.get_user_list(self.config_reader.normal_path)
                    usr_list.remove(user.name)
                    if usr_name not in usr_list:
                        print(f"The user {usr_name} is not a user that exists. Please try again.")
                        continue
                    break
                if usr_name == "q":
                    continue
                while True:
                    drag_name = input("Dragon to Move (q to quit): ")
                    if drag_name == "q":
                        break
                    drag = user.get_dragon(drag_name)
                    if drag is None:
                        print(f"There is no dragon that exists under the name {drag_name} in the user {user.name}. Please try again.")
                        continue
                    other_usr = User(usr_name, self.config_reader)
                    if other_usr.get_dragon(drag_name) is not None:
                        print(f"The other user, {other_usr.name}, has a dragon with the name {drag_name}. Please try again.")
                        continue
                    break
                if drag_name == "q":
                    continue
                while True:
                    sure = input(f"Are you sure you want to move your ({user.name}) dragon {drag_name} to the user {other_usr.name} (y or n): ")
                    if sure == "y":
                        break
                    if sure == "n":
                        break
                if sure == "n":
                    print("Aborted moving this dragon.")
                    continue
                if sure == "y":
                    Getter.dragon_move(user, drag, other_usr)
                    print("Moved the dragon!")
            elif command == "movedragons":
                if len(user.dragons) == 0:
                    print(f"The user {user.name} does not have any dragons.")
                    continue
                u_l = Getter.get_user_list(self.config_reader.normal_path)
                u_l.remove(user.name)
                if len(u_l) == 0:
                    print("There are no users to move the dragons to.")
                    continue
                while True:
                    usr_name = input("User to Move to (q to quit): ")
                    if usr_name == "q":
                        break
                    usr_list = Getter.get_user_list(self.config_reader.normal_path)
                    usr_list.remove(user.name)
                    if usr_name not in usr_list:
                        print(f"The user {usr_name} is not a user that exists. Please try again.")
                        continue
                    break
                if usr_name == "q":
                    continue
                other_usr = User(usr_name, self.config_reader)
                while True:
                    sure = input(f"Are you sure you want to move your ({user.name}) dragons to the user {other_usr.name} (y or n): ")
                    if sure == "y":
                        break
                    if sure == "n":
                        break
                if sure == "n":
                    print("Aborted moving this dragon.")
                    continue
                if sure == "y":
                    for drag in user.dragons:
                        Getter.dragon_move(user, drag, other_usr)
                    print("Moved the dragon!")
            elif command == "userreset":
                if user.name == "default":
                    print("You cannot reset default since it is not a normal user. Please use a different user with setuser. If you want to remove defaults dragons, use the deletedragons command.")
                    continue
                while True:
                    sure = input(f"Are you sure you want to reset the user {user.name} (must use setuser to change what user we reset) (y or n): ")
                    if sure == "n":
                        break
                    if sure == "y":
                        break
                if sure == "n":
                    print("Aborted user reset.")
                    continue
                if sure == "y":
                    while True:
                        supersure = input(f"Are you sure you want to reset the current user you are on ({user.name}). This resets all achievements, deletes all dragons, and is not retrievable after you do this. (y or n): ")
                        if supersure == "y":
                            break
                        if supersure == "n":
                            break
                    if supersure == "n":
                        print("Aborted user reset.")
                        continue
                    if supersure == "y":
                        user.reset_all()
                        print("Reset your user!")
            elif command == "achievementreset":
                if user.name == "default":
                    print("You cannot reset default's achievements since it is not a normal user. Please use a different user with setuser. If you want to remove defaults dragons, use the deletedragons command.")
                    continue
                while True:
                    sure = input(f"Are you sure you want to reset the achievements of the user {user.name} (must use setuser to change what user we reset the achievements of) (y or n): ")
                    if sure == "n":
                        break
                    if sure == "y":
                        break
                if sure == "n":
                    print("Aborted user achievement reset.")
                    continue
                if sure == "y":
                    while True:
                        supersure = input(f"Are you sure you want to reset the achievements of the current user you are on ({user.name}). This resets all achievements and is not retrievable after you do this. (y or n): ")
                        if supersure == "y":
                            break
                        if supersure == "n":
                            break
                    if supersure == "n":
                        print("Aborted user achievement reset.")
                        continue
                    if supersure == "y":
                        user.reset_achievements()
                        print("Reset achievements your user!")
            elif command == "properties":
                print(f"Version: {self.config_reader.version}")
                print(f"Max Prestige: {self.config_reader.max_prestige}")
                print(f"Health Multiplier: {self.config_reader.health_multi}")
                print(f"Exp Multiplier: {self.config_reader.exp_multi}")
                print(f"Font Size (not implemented): {self.config_reader.font_size}")
            elif command == "elements":
                print("Elements:")
                if len(self.config_reader.elements) == 0:
                    print("None")
                    continue
                for element in self.config_reader.elements:
                    print(element)
            elif command == "moves":
                print("Moves:")
                if len(self.config_reader.moves) == 0:
                    print("None")
                    continue
                for move in self.config_reader.moves:
                    print(f"{move.name} - {move.element}")
            elif command == "bosses":
                print("Bosses:")
                if len(self.config_reader.bosses) == 0:
                    print("None")
                    continue
                for x in range(1, len(self.config_reader.bosses)+1):
                    for boss in self.config_reader.bosses:
                        if boss.boss_number == x:
                            print(f"#{boss.boss_number} - {boss.name}")
            elif command == "bosses3":
                print("Bosses3:")
                if len(self.config_reader.bosses3) == 0:
                    print("None")
                    continue
                for x in range(1, len(self.config_reader.bosses3)+1):
                    for boss3 in self.config_reader.bosses3:
                        if boss3.boss_number == x:
                            print(f"#{boss3.boss_number} - {boss3.name}")
            elif command == "quests":
                print(f"Number of Story Quests: {len(self.config_reader.stories)}")
                print(f"Number of Dragon Fights: {len(self.config_reader.story_dragons)}")
                print(f"Number of Boss Fights: {len(self.config_reader.story_bosses)}")
                print(f"Number of Dragon Moves: {len(self.config_reader.story_dragon_moves)}")
                print(f"Number of Boss Moves: {len(self.config_reader.story_boss_moves)}")
            elif command == "moveinfo":
                if len(self.config_reader.moves) == 0:
                    print("There is no moves so we cannot give you information about them.")
                    continue
                while True:
                    move = input("Move Name (q to quit): ")
                    if move == "q":
                        break
                    isMove = False
                    m_obj = None
                    for m in self.config_reader.moves:
                        if move == m.name:
                            isMove = True
                            m_obj = m
                            break
                    if not isMove:
                        print(f"The move with the name {move} does not exist. Please try again.")
                        continue
                    break
                if move == "q":
                    continue
                print(f"{m_obj.name} Info:")
                print(f"Element: {m_obj.element}")
                print(f"Damage: {m_obj.damage}")
                print(f"Accuracy: {m_obj.accuracy}")
                print(f"Level Needed: {m_obj.level_needed}")
                print(f"Boss Number Required: ", end="")
                if m_obj.unlock == 0:
                    print("None")
                else:
                    print(f"{m_obj.unlock}")
            elif command == "bossinfo":
                if len(self.config_reader.bosses) == 0:
                    print("There is no bosses so we cannot give you information about them.")
                    continue
                while True:
                    boss = input("Boss Name or Number (q to quit): ")
                    if boss == "q":
                        break
                    isBoss = False
                    b_obj = None
                    for b in self.config_reader.bosses:
                        if boss == b.name:
                            isBoss = True
                            b_obj = b
                            break
                        if boss.isnumeric():
                            if int(boss) == b.boss_number:
                                isBoss = True
                                b_obj = b
                                break
                    if not isBoss:
                        print(f"The boss with the name {boss} does not exist. Please try again.")
                        continue
                    break
                if boss == "q":
                    continue
                print(f"{b_obj.name} Info:")
                print(f"Boss Number: {b_obj.boss_number}")
                print(f"Level: {b_obj.level}")
                print(f"Move: {b_obj.move.name}")
                print(f"Move Damage: {b_obj.move.damage}")
                print(f"Move Accuracy: {b_obj.move.accuracy}")
            elif command == "boss3info":
                if len(self.config_reader.bosses3) == 0:
                    print("There is no boss3's so you cannot get any information on them.")
                    continue
                while True:
                    boss3 = input("Boss3 Name or Number (q to quit): ")
                    if boss3 == "q":
                        break
                    isBoss3 = False
                    b3_obj = None
                    for b3 in self.config_reader.bosses3:
                        if boss3 == b3.name:
                            isBoss3 = True
                            b3_obj = b3
                            break
                        if boss3.isnumeric():
                            if int(boss3) == b3.boss_number:
                                isBoss3 = True
                                b3_obj = b3
                                break
                    if not isBoss3:
                        print(f"The boss with the name {boss3} does not exist. Please try again.")
                        continue
                    break
                if boss3 == "q":
                    continue
                print(f"{b3_obj.name} Info:")
                print(f"Boss Number: {b3_obj.boss_number}")
                print(f"Level: {b3_obj.level}")
                print(f"Move: {b3_obj.move.name}")
                print(f"Move Damage: {b3_obj.move.damage}")
                print(f"Move Accuracy: {b3_obj.move.accuracy}")
            elif command == "storyinfo":
                if len(self.config_reader.stories) == 0:
                    print("There is no stories so you cannot get information about one.")
                    continue
                print("Please note, this will contain spoilers for messages and everything about the stories.")
                while True:
                    num = input("Number for Story (q to quit): ")
                    if num == "q":
                        break
                    if not num.isnumeric():
                        print(f"The number you gave is not a number, please give on in the range of 1-{len(self.config_reader.stories)}.")
                        continue
                    n = int(num)
                    if n < 1 or n > len(self.config_reader.stories):
                        print(f"The number must be in the range 1-{len(self.config_reader.stores)}, please try again.")
                        continue
                    break
                if num == "q":
                    break
                for story in self.config_reader.stories:
                    if story.name == num:
                        print(f"Name: {story.name}")
                        print(f"Dialogue: {story.dialogue.message}")
                        if story.dragon is not None:
                            print(f"Dragon: {story.dragon.name}")
                            print(f"Level: {story.dragon.level}")
                            print(f"Prestige: {story.dragon.prestige}")
                            print(f"Element: {story.dragon.element}")
                        else:
                            print(f"Dragon: None")
                        if story.boss is not None:
                            print(f"Boss: {story.boss.name}")
                            print(f"Level: {story.boss.level}")
                            print(f"Move: {story.boss.move.name}")
                            print(f"Move Damage: {story.boss.move.damage}")
                            print(f"Move Accuracy: {story.boss.move.accuracy}")
                        else:
                            print(f"Boss: None")
            elif command == "checkachievements":
                if user.name == "default":
                    print("You cannot check achievements because you are not logged into a user.")
                    continue
                user.check_achievements()
            elif command == "tutorial":
                print("Tutorial")
                print("-----------")
                print("Type help to list all of the commands and what they do.")
                print("Type createdragon to start the creation of a dragon.")
                print("Type fight to start a fight with a dragon to grind exp.")
                print("Type boss to start a fight with a boss dragon.")
                print("Type boss3 to start a fight with 3 of your dragons, against one powerful boss.")
                print("Type story to start the story with a specific dragon.")
            elif command == "fight":
                if len(user.dragons) == 0:
                    print(f"You cannot start a fight until you have a dragon. Use the command createdragon to create a dragon.")
                    continue
                while True:
                    drag_name = input("Dragon (q to quit): ")
                    if drag_name == "q":
                        break
                    drag = user.get_dragon(drag_name)
                    if drag is None:
                        print(f"The dragon with the name {drag_name} does not exist under the user profile {user.name}. Please try again.")
                        continue
                    break
                if drag_name == "q":
                    continue
                while True:
                    drag_form = input("Form (q to quit 0 for no form): ")
                    if drag_form == "q":
                        break
                    if not drag_form.isnumeric():
                        print("The form must be a number, and what you provided was not a number, please try again.")
                        continue
                    if int(drag_form) == 0:
                        form = None
                        break
                    form = drag.get_form(int(drag_form))
                    if form is None:
                        print(f"The form with the number {drag_form} does not exist under this dragon or this dragon cannot use this form. Please try again.")
                        continue
                    break
                if drag_form == "q":
                    continue
                while True:
                    drag_move = input("Move (q to quit): ")
                    if drag_move == "q":
                        break
                    move = drag.get_move(drag_move)
                    if move is None:
                        print(f"The move with the name {drag_move} does not exist under this dragon or this dragon cannot use this move. Please try again.")
                        continue
                    break
                if drag_move == "q":
                    continue
                cpu = gen_rand(drag.level, drag.prestige, self.config_reader)
                drag_s = drag
                move_s = move
                form_s = form
                last_cmd_special = True
                start_fight(drag, move, form, cpu, cpu.get_random_move(), cpu.get_random_form(), False, user)
            elif command == "boss":
                if len(user.dragons) == 0:
                    print(f"You cannot start a boss fight until you have a dragon. Use the command createdragon to create a dragon.")
                    continue
                while True:
                    drag_name = input("Dragon (q to quit): ")
                    if drag_name == "q":
                        break
                    drag = user.get_dragon(drag_name)
                    if drag is None:
                        print(f"The dragon with the name {drag_name} does not exist under the user profile {user.name}. Please try again.")
                        continue
                    break
                if drag_name == "q":
                    continue
                while True:
                    drag_form = input("Form (q to quit 0 for no form): ")
                    if drag_form == "q":
                        break
                    if not drag_form.isnumeric():
                        print("The form must be a number, and what you provided was not a number, please try again.")
                        continue
                    if int(drag_form) == 0:
                        form = None
                        break
                    form = drag.get_form(int(drag_form))
                    if form is None:
                        print(f"The form with the number {drag_form} does not exist under this dragon or this dragon cannot use this form. Please try again.")
                        continue
                    break
                if drag_form == "q":
                    continue
                while True:
                    drag_move = input("Move (q to quit): ")
                    if drag_move == "q":
                        break
                    move = drag.get_move(drag_move)
                    if move is None:
                        print(f"The move with the name {drag_move} does not exist under this dragon or this dragon cannot use this move. Please try again.")
                        continue
                    break
                if drag_move == "q":
                    continue
                move_s = move
                drag_s = drag
                form_s = form
                last_cmd_special = True
                boss = self.config_reader.get_boss(drag.boss_number)
                start_fight(drag, move, form, boss, boss.move, None, False, user)
            elif command == "story":
                if len(user.dragons) == 0:
                    print(f"You cannot start the story until you have a dragon. Use the command createdragon to create a dragon.")
                    continue
                while True:
                    drag_name = input("Dragon (q to quit): ")
                    if drag_name == "q":
                        break
                    drag = user.get_dragon(drag_name)
                    if drag is None:
                        print(f"The dragon with the name {drag_name} does not exist under the user profile {user.name}. Please try again.")
                        continue
                    break
                if drag_name == "q":
                    continue
                while True:
                    drag_form = input("Form (q to quit 0 for no form): ")
                    if drag_form == "q":
                        break
                    if not drag_form.isnumeric():
                        print("The form must be a number, and what you provided was not a number, please try again.")
                        continue
                    if int(drag_form) == 0:
                        form = None
                        break
                    form = drag.get_form(int(drag_form))
                    if form is None:
                        print(f"The form with the number {drag_form} does not exist under this dragon or this dragon cannot use this form. Please try again.")
                        continue
                    break
                if drag_form == "q":
                    continue
                while True:
                    drag_move = input("Move (q to quit): ")
                    if drag_move == "q":
                        break
                    move = drag.get_move(drag_move)
                    if move is None:
                        print(f"The move with the name {drag_move} does not exist under this dragon or this dragon cannot use this move. Please try again.")
                        continue
                    break
                if drag_move == "q":
                    continue
                move_s = move
                drag_s = drag
                form_s = form
                self.config_reader.get_story(drag.story_number).start(drag, move, form, user)
            elif command == "boss3":
                if len(user.dragons) < 3:
                    print(f"You cannot start the boss3 fight until you have 3 dragons. Use the command createdragon to create a dragon.")
                    continue
                while True:
                    drag_name1 = input("Dragon1 (q to quit): ")
                    if drag_name1 == "q":
                        break
                    drag1 = user.get_dragon(drag_name1)
                    if drag1 is None:
                        print(f"The dragon with the name {drag_name1} does not exist under the user profile {user.name}. Please try again.")
                        continue
                    break
                if drag_name1 == "q":
                    continue
                while True:
                    drag_form1 = input("Form1 (q to quit 0 for no form): ")
                    if drag_form1 == "q":
                        break
                    if not drag_form1.isnumeric():
                        print("The form must be a number, and what you provided was not a number, please try again.")
                        continue
                    if int(drag_form1) == 0:
                        form1 = None
                        break
                    form1 = drag1.get_form(int(drag_form1))
                    if form1 is None:
                        print(f"The form with the number {drag_form1} does not exist under this dragon or this dragon cannot use this form. Please try again.")
                        continue
                    break
                if drag_form1 == "q":
                    continue
                while True:
                    drag_move1 = input("Move1 (q to quit): ")
                    if drag_move1 == "q":
                        break
                    move1 = drag1.get_move(drag_move1)
                    if move1 is None:
                        print(f"The move with the name {drag_move1} does not exist under this dragon or this dragon cannot use this move. Please try again.")
                        continue
                    break
                if drag_move1 == "q":
                    continue
                while True:
                    drag_name2 = input("Dragon2 (q to quit): ")
                    if drag_name2 == "q":
                        break
                    drag2 = user.get_dragon(drag_name2)
                    if drag1 == drag2:
                        print(f"You are already using this dragon in this fight. Please pick a different one.")
                        continue
                    if drag2 is None:
                        print(f"The dragon with the name {drag_name2} does not exist under the user profile {user.name}. Please try again.")
                        continue
                    break
                if drag_name2 == "q":
                    continue
                while True:
                    drag_form2 = input("Form2 (q to quit 0 for no form): ")
                    if drag_form2 == "q":
                        break
                    if not drag_form2.isnumeric():
                        print("The form must be a number, and what you provided was not a number, please try again.")
                        continue
                    if int(drag_form2) == 0:
                        form2 = None
                        break
                    form2 = drag2.get_form(int(drag_form2))
                    if form2 is None:
                        print(f"The form with the number {drag_form2} does not exist under this dragon or this dragon cannot use this form. Please try again.")
                        continue
                    break
                if drag_form2 == "q":
                    continue
                while True:
                    drag_move2 = input("Move2 (q to quit): ")
                    if drag_move2 == "q":
                        break
                    move2 = drag2.get_move(drag_move2)
                    if move2 is None:
                        print(f"The move with the name {drag_move2} does not exist under this dragon or this dragon cannot use this move. Please try again.")
                        continue
                    break
                if drag_move2 == "q":
                    continue
                while True:
                    drag_name3 = input("Dragon3 (q to quit): ")
                    if drag_name3 == "q":
                        break
                    drag3 = user.get_dragon(drag_name3)
                    if drag3 == drag1 or drag3 == drag2:
                        print(f"You are already using this dragon in this fight. Please pick a different one.")
                    if drag3 is None:
                        print(f"The dragon with the name {drag_name3} does not exist under the user profile {user.name}. Please try again.")
                        continue
                    break
                if drag_name3 == "q":
                    continue
                while True:
                    drag_form3 = input("Form3 (q to quit 0 for no form): ")
                    if drag_form3 == "q":
                        break
                    if not drag_form3.isnumeric():
                        print("The form must be a number, and what you provided was not a number, please try again.")
                        continue
                    if int(drag_form3) == 0:
                        form3 = None
                        break
                    form3 = drag3.get_form(int(drag_form1))
                    if form3 is None:
                        print(f"The form with the number {drag_form3} does not exist under this dragon or this dragon cannot use this form. Please try again.")
                        continue
                    break
                if drag_form3 == "q":
                    continue
                while True:
                    drag_move3 = input("Move3 (q to quit): ")
                    if drag_move3 == "q":
                        break
                    move3 = drag3.get_move(drag_move3)
                    if move3 is None:
                        print(f"The move with the name {drag_move3} does not exist under this dragon or this dragon cannot use this move. Please try again.")
                        continue
                    break
                if drag_move3 == "q":
                    continue
                drages = [drag1, drag2, drag3]
                formes = [form1, form2, form3]
                movees = [move1, move2, move3]
                last_cmd_special = True
                boss_num = drag1.boss3_number
                if drag2.boss3_number > boss_num:
                    boss_num = drag2.boss3_number
                if drag3.boss3_number > boss_num:
                    boss_num = drag3.boss3_number
                if drag1.boss3_number >= boss_num and drag2.boss3_number >= boss_num and drag3.boss3_number >= boss_num:
                    boss3 = self.config_reader.get_boss3(int(drag1.boss3_number))
                    boss3_start(drag1, move1, form1, drag2, move2, form2, drag3, move3, form3, boss3, user)
                else:
                    print("One or more of these dragons have a boss3 number that is too small.")
                    drages = []
                    formes = []
                    movees = []
                    last_cmd_special = False
                    continue
            elif command == "":
                if last_cmd_special:
                    if old_cmd == "fight":
                        n_drag = user.get_dragon(drag_s.name)
                        cpu = gen_rand(n_drag.level, n_drag.prestige, self.config_reader)
                        start_fight(n_drag, move_s, form_s, cpu, cpu.get_random_move(), cpu.get_random_form(), False, user)
                    elif old_cmd == "boss":
                        n_drag = user.get_dragon(drag_s.name)
                        boss = self.config_reader.get_boss(n_drag.boss_number)
                        start_fight(n_drag, move_s, form_s, boss, boss.move, None, False, user)
                    elif old_cmd == "boss3":
                        n_drag1 = user.get_dragon(drages[0].name)
                        n_drag2 = user.get_dragon(drages[1].name)
                        n_drag3 = user.get_dragon(drages[2].name)
                        boss_num = drag1.boss3_number
                        if drag2.boss3_number > boss_num:
                            boss_num = drag2.boss3_number
                        if drag3.boss3_number > boss_num:
                            boss_num = drag3.boss3_number
                        if drag1.boss3_number >= boss_num and drag2.boss3_number >= boss_num and drag3.boss3_number >= boss_num:
                            boss3 = self.config_reader.get_boss(boss_num)
                            boss3_start(n_drag1, movees[0], formes[0], n_drag2, movees[1], formes[1], n_drag3, movees[2], formes[2], boss3, user)
                        else:
                            print("Invalid command. Please type help to list all of the commands and what they do.")
                else:
                    print("Invalid command. Please type help to list all of the commands and what they do.")
            else:
                print("Invalid command. Please type help to list all of the commands and what they do.")
            if command != "":
                old_cmd = command


"""Commands to add:
creator PROGRAM
"""

if __name__ == "__main__":
    config_loc_lines = FileActions.get_lines("config_loc.txt")
    if config_loc_lines[0] == "inthisfolder":
        g = GUI(os.getcwd().replace("\\", "/") + "/Config")
    else:
        g = GUI(config_loc_lines[0])
    g.start()
else:
    raise RunMustBeByMainError
