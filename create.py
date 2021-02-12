import os
from ConfigReader import ConfigReader
import FileActions

config_loc_lines = FileActions.get_lines("config_loc.txt")
if config_loc_lines[0] == "inthisfolder":
    cof = os.getcwd().replace("\\", "/") + "/Config"
else:
    cof = (config_loc_lines[0].replace("\\", "/"))
config = ConfigReader(cof)


def reload_config():
    """Reloads the config so it is updated."""
    config = ConfigReader(cof)


def print_change_list():
    """Prints the list of changeable/addable things."""
    print("List of things you can create:")
    print("achievement")
    print("boss")
    print("bossmove")
    print("boss3")
    print("boss3move")
    print("element")
    print("form")
    print("move")
    print("story")
    print("List of things you can edit:")
    print("bosshealthmult")
    print("expcalcmult")
    #print("fontsize")
    print("healthmult")
    print("maxprestige")


print_change_list()

while True:
    action = input("What would you like to create/edit (q to cancel)? ")
    action = action.lower()
    if action == "q":
        exit()
    if action == "achievement":
        valid_actions = ["level", "created", "createu", "prestige", "exp", "boss", "boss3", "story"]
        actions = []
        numbers = []
        while True:
            new_action = input("Achievement Action: (q to quit/finish adding actions): ")
            if new_action == "q":
                break
            if new_action not in valid_actions:
                print("The action that you provided is not a valid action. Valid actions are: ")
                for act in valid_actions:
                    print(act)
                print("Please try again.")
                continue
            if new_action in actions:
                print("You have already added this action. You can only add one action with one number at a time.")
                continue
            if new_action == "created" or new_action == "createu":
                actions.append(new_action)
                numbers.append(0)
                print("Created a new action! Type q to stop adding more!")
                continue
            else:
                max = 1
                if new_action == "level":
                    max = 3000
                elif new_action == "prestige":
                    max = config.max_prestige
                elif new_action == "exp":
                    max = 900000000
                elif new_action == "boss":
                    max = len(config.bosses)
                elif new_action == "boss3":
                    max = len(config.bosses3)
                elif new_action == "story":
                    max = len(config.stories)

                while True:
                    new_number = input(f"Please input a number for the action {new_action} (must be a number between 1-{max}) (q to cancel): ")
                    if new_number == "q":
                        break
                    try:
                        number = int(new_number)
                        if number < 1 or number > max:
                            print(f"The value that you gave was either higher than 1 or higher than the max value of {max}. Please try again.")
                            continue
                        break
                    except ValueError:
                        print("The value that you gave was an invalid number. Please try again.")
                if new_number == "q":
                    print("Canceled adding this action.")
                    continue
                numbers.append(number)
                actions.append(new_action)

        if new_action == "q" and len(actions) == 0:
            print("Canceled making new achievement.")
        else:
            while True:
                ach_message = input("Achievement Message (q to quit): ")
                break
            if ach_message == "q":
                print("Canceled making new achievement.")
            else:
                config.create_achievement(actions, numbers, ach_message)
                reload_config()
    elif action == "boss":
        while True:
            boss_name = input("Dragon Boss Name (q to quit): ")
            if boss_name == "q":
                break
            if len(boss_name) == 0:
                print("Please put a name.")
                continue
            break
        if boss_name == "q":
            print("Canceled making a new boss.")
        else:
            while True:
                boss_chlevel = input("Dragon Boss Level (Must be 1 or over and a number) (q to quit): ")
                if boss_chlevel == "q":
                    break
                try:
                    boss_level = int(boss_chlevel)
                    if boss_level <= 0:
                        print("Please give us a number 1 or over.")
                        continue
                    break
                except ValueError:
                    print("Please give us a valid number.")
            if boss_chlevel == "q":
                print("Canceled making a new boss.")
            else:
                while True:
                    boss_move = input("Boss Move Name (q to quit): ")
                    if boss_move == "q":
                        break
                    if not config.isBossMove(boss_move):
                        print("The move you provided was not a valid boss move. All valid boss moves are: ")
                        for mv in config.boss_moves:
                            print(mv.name)
                        print("Please try again.")
                        continue
                    break
                if boss_move == "q":
                    print("Canceled making a new boss.")
                else:
                    config.create_boss(boss_name, boss_level, boss_move, config.get_new_boss_number())
                    reload_config()
    elif action == "bossmove":
        while True:
            move_name = input("Boss Move Name (q to quit): ")
            if move_name == "q":
                break
            if config.isBossMove(move_name):
                print("The move name you provided is already a move. Please pick a different move name.")
                continue
            break
        if move_name == "q":
            print("Canceled making new boss move.")
        else:
            while True:
                move_chdamage = input("Boss Move Damage (q to quit) (Must be a number and above 1): ")
                if move_chdamage == "q":
                    break
                try:
                    move_damage = int(move_chdamage)
                    if move_damage <= 0:
                        print("The value you provided was less than or equal to zero. Please make sure it is above zero.")
                        continue
                    break
                except ValueError:
                    print("The value you provided was an invalid number. Please try again.")
            if move_chdamage == "q":
                print("Canceled making new boss move.")
            else:
                while True:
                    move_chaccuracy = input("Boss Move Accuracy (q to quit) (Must be a number and between 1-100): ")
                    if move_chaccuracy == "q":
                        break
                    try:
                        move_accuracy = int(move_chaccuracy)
                        if move_accuracy > 100 or move_accuracy < 1:
                            print("The value you provided was either less than 1 or greater than 100. This cannot be possible. Please try again with a value between 1-100.")
                            continue
                        break
                    except ValueError:
                        print("The valid you provided was an invalid number. Please try again.")
                if move_chaccuracy == "q":
                    print("Canceled making new boss move.")
                else:
                    config.create_boss_move(move_name, move_damage, move_accuracy)
                    reload_config()
    elif action == "boss3":
        while True:
            boss_name = input("Dragon Boss3 Name (q to quit): ")
            if boss_name == "q":
                break
            if len(boss_name) == 0:
                print("Please put a name.")
                continue
            break
        if boss_name == "q":
            print("Canceled making a new boss3.")
        else:
            while True:
                boss_chlevel = input("Dragon Boss3 Level (Must be 1 or over and a number) (q to quit): ")
                if boss_chlevel == "q":
                    break
                try:
                    boss_level = int(boss_chlevel)
                    if boss_level <= 0:
                        print("Please give us a number 1 or over.")
                        continue
                    break
                except ValueError:
                    print("Please give us a valid number.")
            if boss_chlevel == "q":
                print("Canceled making a new boss3.")
            else:
                while True:
                    boss_move = input("Boss3 Move Name (q to quit): ")
                    if boss_move == "q":
                        break
                    if not config.isBossMove3(boss_move):
                        print("The move you provided was not a valid boss3 move. All valid boss3 moves are: ")
                        for mv in config.boss_moves3:
                            print(mv.name)
                        print("Please try again.")
                        continue
                    break
                if boss_move == "q":
                    print("Canceled making a new boss3.")
                else:
                    config.create_boss3(boss_name, boss_level, boss_move, config.get_new_boss3_number())
                    reload_config()
    elif action == "boss3move":
        while True:
            move_name = input("Boss3 Move Name (q to quit): ")
            if move_name == "q":
                break
            if config.isBossMove3(move_name):
                print("The move name you provided is already a move. Please pick a different move name.")
                continue
            break
        if move_name == "q":
            print("Canceled making new boss3 move.")
        else:
            while True:
                move_chdamage = input("Boss3 Move Damage (q to quit) (Must be a number and above 1): ")
                if move_chdamage == "q":
                    break
                try:
                    move_damage = int(move_chdamage)
                    if move_damage <= 0:
                        print("The value you provided was less than or equal to zero. Please make sure it is above zero.")
                        continue
                    break
                except ValueError:
                    print("The value you provided was an invalid number. Please try again.")
            if move_chdamage == "q":
                print("Canceled making new boss3 move.")
            else:
                while True:
                    move_chaccuracy = input("Boss3 Move Accuracy (q to quit) (Must be a number and between 1-100): ")
                    if move_chaccuracy == "q":
                        break
                    try:
                        move_accuracy = int(move_chaccuracy)
                        if move_accuracy > 100 or move_accuracy < 1:
                            print("The value you provided was either less than 1 or greater than 100. This cannot be possible. Please try again with a value between 1-100.")
                            continue
                        break
                    except ValueError:
                        print("The valid you provided was an invalid number. Please try again.")
                if move_chaccuracy == "q":
                    print("Canceled making new boss3 move.")
                else:
                    config.create_boss3_move(move_name, move_damage, move_accuracy)
                    reload_config()
    elif action == "element":
        while True:
            change = input("Element Name (q to quit): ")
            if change == "q":
                break
            if config.isElement(change):
                print("This is already a name of another element. Please try again.")
                continue
            break
        if change == "q":
            print("Canceled making new element")
        else:
            FileActions.create_file(f"{cof}/Elements/{change}.txt")
            reload_config()
            print(f"Created a new element named {change}!")
    elif action == "form":
        while True:
            change = input("Form Element (q to quit): ")
            if change == "q":
                break
            if not config.isElement(change):
                print("This is not an element! Please try again.")
                continue
            break
        if change == "q":
            print("Canceled creating a new form.")
        else:
            while True:
                changef = input("Form Name (q to quit): ")
                if changef == "q":
                    break
                if config.isForm(change, changef):
                    print("This form already exists. Please choose a different one.")
                    continue
                break
            if changef == "q":
                print("Canceled making a new form.")
            else:
                while True:
                    changefm = input("Form Multiplier (Number) (q to quit): ")
                    if changefm == "q":
                        break
                    try:
                        fm = int(changefm)
                        if fm <= 0:
                            print("Form multipliers must be greater than zero. Please try again.")
                            continue
                        break
                    except ValueError:
                        print("Given number is an invalid number. Please try again.")
                if changefm == "q":
                    print("Canceled making new form.")
                else:
                    while True:
                        changelr = input("Form Level Requirement (Number) (q to quit): ")
                        if changelr == "q":
                            break
                        try:
                            lr = int(changelr)
                            if lr <= 0:
                                print("Form Level Requirement must be greater than zero. Please try again.")
                                continue
                            if lr > 3000:
                                print("Form Level Requirement cannot be greater than 3000. Please try again.")
                                continue
                            break
                        except ValueError:
                            print("Invalid number. Please try again.")
                    if changelr == "q":
                        print("Canceled making new form.")
                    else:
                        config.create_form(change, changef, fm, lr)
                        reload_config()
    elif action == "move":
        mv_name = ""
        mv_element = ""
        mv_damage = 0
        mv_accuracy = 0
        mv_levelreq = 0
        mv_unlock = 0
        while True:
            mv_name = input("Move name (q to quit): ")
            if mv_name == "q":
                break
            mv_element = input("Move Element: ")
            if not config.isElement(mv_element):
                print("The element you gave was not an element. Please try again.")
                continue
            if config.isMove(mv_element, mv_name):
                print("A move with this name and element already exists. Please choose a different name.")
                continue
            else:
                break
        if mv_name == "q":
            print("Canceled the creation of a new move.")
        else:
            while True:
                dmg = input("Move Damage (number) (q to quit): ")
                if dmg == "q":
                    break
                try:
                    mv_damage = int(dmg)
                    if mv_damage <= 0:
                        print("The move damage must be less than or equal to zero. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid number. Please make sure that the value is a number.")
            if dmg == "q":
                print("Canceled making new move.")
            else:
                while True:
                    acc = input("Move Accuracy (number 1-100) (q to quit): ")
                    if acc == "q":
                        break
                    try:
                        mv_accuracy = int(acc)
                        if mv_accuracy <= 0:
                            print("Accuracy must be greater than zero and less than 101. Please try again.")
                            continue
                        if mv_accuracy >= 101:
                            print("Accuracy must be greater than zero and less than 101. Please try again.")
                            continue
                        break
                    except ValueError:
                        print("Invalid number. Please make sure that the value is a number.")
                if acc == "q":
                    print("Canceled making new move.")
                else:
                    while True:
                        lr = input("Move Level Requirement (1-3000) (q to quit): ")
                        if lr == "q":
                            break
                        try:
                            mv_levelreq = int(lr)
                            if mv_levelreq < 1 or mv_levelreq > 3000:
                                print("Minimum level is 1 and Maximum level is 3000. Please try again.")
                                continue
                            break
                        except ValueError:
                            print("The number given was not a valid number. Please try again.")
                    if lr == "q":
                        print("Canceled making new move.")
                    else:
                        if len(config.bosses) <= 0:
                            print("Since there are no bosses we made no unlock requirement.")
                        else:
                            while True:
                                un = input("Move Unlock (0 for no boss requirement (boss number)) (q to quit): ")
                                if un == "q":
                                    break
                                try:
                                    u = int(un)
                                    if u == 0:
                                        break
                                    bos = config.get_boss(u)
                                    if bos is None:
                                        print("There is no boss with this number that exists. Please try again.")
                                        continue
                                    break
                                except ValueError:
                                    print("Invalid number. Please try again.")
                        if un == "q":
                            print("Canceled making new move.")
                        else:
                            config.create_move(mv_name, mv_element, mv_damage, mv_accuracy, mv_levelreq, mv_unlock)
                            reload_config()
    elif action == "story":
        print("Due to complexities with story mode we have not yet created the creation tool for it. I apologize.")
    elif action == "bosshealthmult":
        print(f"Current boss health multiplier is {config.bosshealth_multiplier}.")
        while True:
            change = input("What would you like to change it to (q to cancel)? ")
            if change == "q":
                break
            try:
                ch = int(change)
                if ch <= 0:
                    print("Boss health multiplier cannot be less than or equal to zero. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid number. Please put a valid number.")
        if change != "q":
            config.set_boss_health_mult(ch)
            reload_config()
        else:
            print("Canceled changing value.")
    elif action == "expcalcmult":
        print(f"Current exp calculation multiplier is {config.exp_multi}.")
        while True:
            change = input("What would you like to change it to (q to cancel)? ")
            if change == "q":
                break
            try:
                ch = int(change)
                if ch <= 0:
                    print("Exp calc multiplier cannot be less than or equal to zero. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid number. Please put a valid number.")
        if change != "q":
            config.set_exp_calc_mult(ch)
            reload_config()
        else:
            print("Canceled changing value.")
    elif action == "healthmult":
        print(f"Current health multiplier is {config.health_multi}.")
        while True:
            change = input("What would you like to change it to (q to cancel)? ")
            if change == "q":
                break
            try:
                ch = int(change)
                if ch <= 0:
                    print("Health multiplier cannot be less than or equal to zero. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid number. Please put a valid number.")
        if change != "q":
            config.set_health_multi(ch)
            reload_config()
        else:
            print("Canceled changing value.")
    elif action == "maxprestige":
        print(f"Current max Prestige is {config.max_prestige}.")
        while True:
            change = input("What would you like to change it to (q to cancel)? ")
            if change == "q":
                break
            try:
                ch = int(change)
                if ch <= 0:
                    print("The prestige cannot be less than or equal to 0. If you want to disable prestige put 1.")
                    continue
                if ch == config.max_prestige:
                    print("This is already the current max prestige. Please choose a different number.")
                    continue
                break
            except ValueError:
                print("Invalid number. Please put a valid number.")
        if change != "q":
            config.set_max_prestige(ch)
            reload_config()
        else:
            print("Canceled changing value.")
    else:
        print("Invalid choice here are your choices:")
        print_change_list()
        print("Please try again.")
