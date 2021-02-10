import os

errs = []
print("Checking for Syntax Errors...")
with open("config_loc.txt", "r") as f:
    path = f.readline()
config = ""
if path == "inthisfolder":
    config = os.getcwd().replace("\\", "/") + "/Config/"
else:
    config = path.replace("\\", "/")
    if config[-1] is not "/":
        config += "/"
config_files = os.listdir(config)
for config_file in config_files:
    if "." in config_file:
        continue
    if config_file == "DragonBosses":
        boss_files = os.listdir(f"{config}DragonBosses/")
        if len(boss_files) <= 1:
            continue
        for boss_file in boss_files:
            if boss_file == "Moves":
                bmove_files = os.listdir(f"{config}DragonBosses/Moves/")
                if len(bmove_files) == 0:
                    continue
                for bmove_file in bmove_files:
                    with open(f"{config}DragonBosses/Moves/{bmove_file}", "r") as bmf:
                        bm_lines = bmf.readlines()
                    if len(bm_lines) == 0:
                        errs.append(f"Major Error ({config}DragonBosses/Moves/{bmove_file}) This boss move does not have any content. Cannot check other issues due to this error.")
                    elif len(bm_lines) != 3:
                        errs.append(f"Major Error ({config}DragonBosses/Moves/{bmove_file}) This boss move does not contain the correct amount of lines. Should be 3. Cannot check other issues due to this error.")
                    else:
                        name = bm_lines[0][0:bm_lines[0].index("\n")]
                        damage = bm_lines[1][0:bm_lines[1].index("\n")]
                        accuracy = bm_lines[2]
                        if name == "":
                            errs.append(f"Minor Error ({config}DragonBosses/Moves/{bmove_file}) This move does not contain a name in the file.")
                        if bmove_file[0:bmove_file.index(".")] != name:
                            errs.append(f"Minor Error ({config}DragonBosses/Moves/{bmove_file}) This moves filename and move name do not match.")
                        if not damage.isnumeric():
                            errs.append(f"Major Error ({config}DragonBosses/Moves/{bmove_file}) This moves damage is not a valid number (not a number).")
                        if not accuracy.isnumeric():
                            errs.append(f"Major Error ({config}DragonBosses/Moves/{bmove_file}) This moves accuracy is not a valid number (not a number).")
                        else:
                            if int(accuracy) <= 0:
                                errs.append(f"Major Error ({config}DragonBosses/Moves/{bmove_file}) This moves accuracy is less than or equal to zero.")
                            if int(accuracy) > 100:
                                errs.append(f"Major Error ({config}DragonBosses/Moves/{bmove_file}) This moves accuracy is over 100.")
                continue
            if "." not in boss_file:
                continue
            with open(f"{config}DragonBosses/{boss_file}", "r") as bf:
                b_lines = bf.readlines()
            if len(b_lines) == 0:
                errs.append(f"Major Error ({config}DragonBosses/{boss_file}) This boss file contains no content. Cannot check other issues due to this error.")
            elif len(b_lines) != 4:
                errs.append(f"Major Error ({config}DragonBosses/{boss_file}) The boss file does not contain the correct amount of lines. Should be 4. Cannot check other issues due to this error.")
            else:
                if b_lines[0][0:b_lines[0].index("\n")] == "":
                    errs.append(f"Minor Error ({config}DragonBosses/{boss_file}) The boss file does not contain a name.")
                if b_lines[1][0:b_lines[1].index("\n")] == "":
                    errs.append(f"Major Error (({config}DragonBosses/{boss_file}) The boss file does not contain a level.")
                else:
                    if not b_lines[1][0:b_lines[1].index("\n")].isnumeric():
                        errs.append(f"Major Error ({config}DragonBosses/{boss_file}) The boss file has an invalid number value for its level.")
                if b_lines[2] == "":
                    errs.append(f"Major Error ({config}DragonBosses/{boss_file}) The boss file does not contain a move.")
                if b_lines[3] == "":
                    errs.append(f"Major Error ({config}DragonBosses/{boss_file}) The boss file does not contain a boss number.")
                else:
                    if not b_lines[3].isnumeric():
                        errs.append(f"Major Error ({config}DragonBosses/{boss_file}) This boss does not contain a valid boss number (Not a number).")
                    else:
                        num_bosses = len(boss_files)-1
                        boss_num = int(b_lines[3])
                        if boss_num < 1:
                            errs.append(f"Major Error ({config}DragonBosses/{boss_file}) The boss number this boss has is lower than possible (lower than 1).")
                        if boss_num > num_bosses:
                            errs.append(f"Major Error ({config}DragonBosses/{boss_file}) The boss number this boss has is higher than possible (higher than the total number of bosses, {num_bosses}).")
    elif config_file == "DragonBosses3":
        boss_files = os.listdir(f"{config}DragonBosses3/")
        if len(boss_files) <= 1:
            continue
        for boss_file in boss_files:
            if boss_file == "Moves":
                bmove_files = os.listdir(f"{config}DragonBosses3/Moves/")
                if len(bmove_files) == 0:
                    continue
                for bmove_file in bmove_files:
                    with open(f"{config}DragonBosses3/Moves/{bmove_file}", "r") as bmf:
                        bm_lines = bmf.readlines()
                    if len(bm_lines) == 0:
                        errs.append(f"Major Error ({config}DragonBosses3/Moves/{bmove_file}) This boss move does not have any content. Cannot check other issues due to this error.")
                    elif len(bm_lines) != 3:
                        errs.append(f"Major Error ({config}DragonBosses3/Moves/{bmove_file}) This boss move does not contain the correct amount of lines. Should be 3. Cannot check other issues due to this error.")
                    else:
                        name = bm_lines[0][0:bm_lines[0].index("\n")]
                        damage = bm_lines[1][0:bm_lines[1].index("\n")]
                        accuracy = bm_lines[2]
                        if name == "":
                            errs.append(f"Minor Error ({config}DragonBosses3/Moves/{bmove_file}) This move does not contain a name in the file.")
                        if bmove_file[0:bmove_file.index(".")] != name:
                            errs.append(f"Minor Error ({config}DragonBosses3/Moves/{bmove_file}) This moves filename and move name do not match.")
                        if not damage.isnumeric():
                            errs.append(f"Major Error ({config}DragonBosses3/Moves/{bmove_file}) This moves damage is not a valid number (not a number).")
                        if not accuracy.isnumeric():
                            errs.append(f"Major Error ({config}DragonBosses3/Moves/{bmove_file}) This moves accuracy is not a valid number (not a number).")
                        else:
                            if int(accuracy) <= 0:
                                errs.append(f"Major Error ({config}DragonBosses3/Moves/{bmove_file}) This moves accuracy is less than or equal to zero.")
                            if int(accuracy) > 100:
                                errs.append(f"Major Error ({config}DragonBosses3/Moves/{bmove_file}) This moves accuracy is over 100.")
                continue
            if "." not in boss_file:
                continue
            with open(f"{config}DragonBosses3/{boss_file}", "r") as bf:
                b_lines = bf.readlines()
            if len(b_lines) == 0:
                errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) This boss file contains no content. Cannot check other issues due to this error.")
            elif len(b_lines) != 4:
                errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) The boss file does not contain the correct amount of lines. Should be 4. Cannot check other issues due to this error.")
            else:
                if b_lines[0][0:b_lines[0].index("\n")] == "":
                    errs.append(f"Minor Error ({config}DragonBosses3/{boss_file}) The boss file does not contain a name.")
                if b_lines[1][0:b_lines[1].index("\n")] == "":
                    errs.append(f"Major Error (({config}DragonBosses3/{boss_file}) The boss file does not contain a level.")
                else:
                    if not b_lines[1][0:b_lines[1].index("\n")].isnumeric():
                        errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) The boss file has an invalid number value for its level.")
                if b_lines[2] == "":
                    errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) The boss file does not contain a move.")
                if b_lines[3] == "":
                    errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) The boss file does not contain a boss number.")
                else:
                    if not b_lines[3].isnumeric():
                        errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) This boss does not contain a valid boss number (Not a number).")
                    else:
                        num_bosses = len(boss_files)-1
                        boss_num = int(b_lines[3])
                        if boss_num < 1:
                            errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) The boss number this boss has is lower than possible (lower than 1).")
                        if boss_num > num_bosses:
                            errs.append(f"Major Error ({config}DragonBosses3/{boss_file}) The boss number this boss has is higher than possible (higher than the total number of bosses, {num_bosses}).")
    elif config_file == "Elements":
        elements = os.listdir(f"{config}Elements/")
        if len(elements) == 0:
            errs.append(f"Major Error ({config}Elements/) This config does not contain any elements.")
    elif config_file == "Forms":
        form_folders = os.listdir(f"{config}Forms/")
        for form_folder in form_folders:
            form_files = os.listdir(f"{config}Forms/{form_folder}/")
            for form_file in form_files:
                with open(f"{config}Forms/{form_folder}/{form_file}", "r") as ff:
                    form_lines = ff.readlines()
                if not form_file[0:form_file.index(".")].isnumeric():
                    errs.append(f"Major Error ({config}Forms/{form_folder}/{form_file}) This forms file name is not a number.")
                if len(form_lines) == 0:
                    errs.append(f"Major Error ({config}Forms/{form_folder}/{form_file}) This forms file does not contain any data. This prevents us from checking other issues.")
                elif len(form_lines) != 2:
                    errs.append(f"Major Error ({config}Forms/{form_folder}/{form_file}) This forms file does not contain the correct number of lines. This prevents us from checking other issues.")
                else:
                    multiplier = form_lines[0][0:form_lines[0].index("\n")]
                    level_req = form_lines[1]
                    if not multiplier.isnumeric():
                        errs.append(f"Major Error ({config}Forms/{form_folder}/{form_file}) This forms multiplier is not a valid number (not a number).")
                    else:
                        if int(multiplier) <= 1:
                            errs.append(f"Major Error ({config}Forms/{form_folder}/{form_file}) This forms multiplier is less than or equal to 1.")
                    if not level_req.isnumeric():
                        errs.append(f"Major Error ({config}Forms/{form_folder}/{form_file}) This forms required level is not a valid number (not a number).")
                    else:
                        if int(level_req) <= 0:
                            errs.append(f"Minor Error ({config}Forms/{form_folder}/{form_file}) This forms required level is less than or equal to 0.")
                        if int(level_req) > 3000:
                            errs.append(f"Major Error ({config}Forms/{form_folder}/{form_file}) This forms required level is over the max level of 3000.")
    elif config_file == "Other":
        other_files = os.listdir(f"{config}Other/")
        if "expcalcmultiplier.txt" not in other_files:
            errs.append(f"Major Error ({config}Other/) The other folder does not contain an important file: expcalcmultiplier.txt")
        if "fontsize.txt" not in other_files:
            errs.append(f"Major Error ({config}Other/) The other folder does not contain an important file: fontsize.txt")
        if "healthmultiplier.txt" not in other_files:
            errs.append(f"Major Error ({config}Other/) The other folder does not contain an important file: healthmultiplier.txt")
        if "maxprestige.txt" not in other_files:
            errs.append(f"Major Error ({config}Other/) The other folder does not contain an important file: maxprestige.txt")
        if "ver.txt" not in other_files:
            errs.append(f"Major Error ({config}Other/) The other folder does not contain an important file: ver.txt")
        if "bosshealthmultiplier.txt" not in other_files:
            errs.append(f"Major Error ({config}Other/) The other folder does not contain an important file: bosshealthmultiplier.txt")
        for other_file in other_files:
            with open(f"{config}Other/{other_file}", "r") as exp_f:
                exp_lines = exp_f.readlines()
            if len(exp_lines) == 0:
                errs.append(f"Major Error ({config}Other/{other_file}) The important file {other_file} does not contain any data.")
            elif len(exp_lines) != 1:
                errs.append(f"Major Error ({config}Other/{other_file}) The important file {other_file} does not contain the correct number of lines (1).")
            elif other_file != "ver.txt":
                mult = exp_lines[0]
                if not mult.isnumeric():
                    errs.append(f"Major Error ({config}Other/{other_file}) The important file {other_file} has content is not a valid number (not a number).")
                else:
                    if int(mult) < 1:
                        errs.append(f"Major Error ({config}Other/{other_file}) The important file {other_file} has content that has a number less than 1.")
    elif config_file == "Moves":
        move_files = os.listdir(f"{config}Moves/")
        if len(move_files) == 0:
            errs.append(f"Major Error ({config}Moves/) The moves folder does not contain any moves. Big issue.")
        for move_file in move_files:
            with open(f"{config}Moves/{move_file}", "r") as m_f:
                m_lines = m_f.readlines()
            if len(m_lines) == 0:
                errs.append(f"Major Error ({config}Moves/{move_file}) This move does not have any data.")
            elif len(m_lines) != 6:
                errs.append(f"Major Error ({config}Moves/{move_file}) This move does not contain the correct number of lines (6).")
            else:
                name = m_lines[0][0:m_lines[0].index("\n")]
                element = m_lines[1][0:m_lines[1].index("\n")]
                damage = m_lines[2][0:m_lines[2].index("\n")]
                accuracy = m_lines[3][0:m_lines[3].index("\n")]
                level_needed = m_lines[4][0:m_lines[4].index("\n")]
                unlock = m_lines[5]
                if name != move_file[0:move_file.index(".")]:
                    errs.append(f"Major Error ({config}Moves/{move_file}) This move's file name is not the same as the name content on the first line (name).")
                if name == "":
                    errs.append(f"Minor Error ({config}Moves/{move_file}) This move does not contain a name in the file.")
                if not damage.isnumeric():
                    errs.append(f"Major Error ({config}Moves/{move_file}) This move's damage is not a valid number (not a number).")
                else:
                    if int(damage) < 1:
                        errs.append(f"Minor Error ({config}Moves/{move_file}) This move's damage is less than one.")
                if not accuracy.isnumeric():
                    errs.append(f"Major Error ({config}Moves/{move_file}) This move's accuracy is not a valid number (not a number).")
                else:
                    if int(accuracy) < 1:
                        errs.append(f"Major Error ({config}Moves/{move_file}) This move's accuracy is less than 1.")
                    if int(accuracy) > 100:
                        errs.append(f"Major Error ({config}Moves/{move_file}) This move's accuracy is greater than 100.")
                if not level_needed.isnumeric():
                    errs.append(f"Major Error ({config}Moves/{move_file}) This move's level needed is not a valid number (not a number).")
                else:
                    if int(level_needed) < 1:
                        errs.append(f"Minor Error ({config}Moves/{move_file}) This move's level needed is less than one.")
                    if int(level_needed) > 3000:
                        errs.append(f"Major Error ({config}Moves/{move_file}) This move's level needed is higher than the max level possible.")
                if not unlock.isnumeric():
                    errs.append(f"Major Error ({config}Moves/{move_file}) This move's unlock number is not a valid number (not a number).")
                else:
                    if int(unlock) < 0:
                        errs.append(f"Major Error ({config}Moves/{move_file}) This move's unlock is less than 0.")
    elif config_file == "Achievements":
        ach_files = os.listdir(f"{config}Achievements/")
        for ach_file in ach_files:
            with open(f"{config}Achievements/{ach_file}", "r") as a_f:
                a_lines = a_f.readlines()
            if len(a_lines) == 0:
                errs.append(f"Major Error ({config}Achievements/{ach_file}) This achievement does not contain any data.")
            elif len(a_lines) != 3:
                errs.append(f"Major Error ({config}Achievements/{ach_file}) This achievement does not contain the correct number of lines.")
            else:
                actions = []
                if "," in a_lines[0]:
                    acts = a_lines[0].split(",")
                    for act in acts:
                        if "\n" in act:
                            actions.append(act[0:act.index("\n")])
                        else:
                            actions.append(act)
                else:
                    actions.append(a_lines[0][0:a_lines[0].index("\n")])

                numbers = []
                if "," in a_lines[1]:
                    nums = a_lines[1].split(",")
                    for num in nums:
                        if "\n" in num:
                            numbers.append(num[0:num.index("\n")])
                        else:
                            numbers.append(num)
                else:
                    numbers.append(a_lines[1][0:a_lines[1].index("\n")])
                message = a_lines[2]
                if message == "":
                    print(f"Minor Error ({config}Achievements/{ach_file}) There is no message for this achievement.")
                if len(actions) != len(numbers):
                    print(f"Major Error ({config}Achievements/{ach_file}) The number of actions ({len(actions)}) versus the number of numbers ({len(numbers)}) for this achievement are not the same.")
                for action in actions:
                    if action == "":
                        print(f"Major Error ({config}Achievements/{ach_file}) An action is nothing, which cannot be possible.")
                for number in numbers:
                    if number == "":
                        print(f"Major Error ({config}Achievements/{ach_file}) A number is nothing, which cannot be possible.")
                    if not number.isnumeric():
                        print(f"Major Error ({config}Achievements/{ach_file}) A number is not a valid number (not a number).")
                    else:
                        if int(number) < 0:
                            print(f"Minor Error ({config}Achievements/{ach_file}) The requirement number for an action is less than 0.")
    elif config_file == "Story":
        story_folders = os.listdir(f"{config}Story/")
        for story_folder in story_folders:
            if story_folder == "Dialogue":
                dia_files = os.listdir(f"{config}Story/Dialogue/")
                for dia_file in dia_files:
                    with open(f"{config}Story/Dialogue/{dia_file}", "r") as d_f:
                        d_lines = d_f.readlines()
                    if len(d_lines) == 0:
                        print(f"Major Error ({config}Story/Dialogue/{dia_file}) This dialogue does not contain any data.")
                    elif len(d_lines) != 1:
                        print(f"Major Error ({config}Story/Dialogue/{dia_file}) This dialogue does not have the correct amount of lines (1).")
                    else:
                        if d_lines[0] == "":
                            print(f"Minor Error ({config}Story/Dialogue/{dia_file}) This dialogue does not have any text.")
            elif story_folder == "Order":
                order_files = os.listdir(f"{config}Story/Order/")
                for order_file in order_files:
                    with open(f"{config}Story/Order/{order_file}", "r") as o_f:
                        o_lines = o_f.readlines()
                    if len(o_lines) == 0:
                        print(f"Major Error ({config}Story/Order/{order_file}) This order file does not contain any data.")
                    elif len(o_lines) != 4:
                        print(f"Major Error ({config}Story/Order/{order_file}) This order file does not have the correct amount of lines (4).")
                    else:
                        fight = o_lines[1][0:o_lines[1].index("\n")]
                        if fight != "true" and fight != "none":
                            print(f"Minor Error ({config}Story/Order/{order_file}) This order file fight data does not contain a valid object. Must be 'true' or 'none' not {fight}.")
            elif story_folder == "Dragons":
                dragon_files = os.listdir(f"{config}Story/Dragons/")
                for dragon_file in dragon_files:
                    if dragon_file == "Moves":
                        dragon_move_files = os.listdir(f"{config}Story/Dragons/Moves/")
                        for dragon_move_file in dragon_move_files:
                            with open(f"{config}Story/Dragons/Moves/{dragon_move_file}", "r") as dm_f:
                                dm_lines = dm_f.readlines()
                            if len(dm_lines) == 0:
                                print(f"Major Error ({config}Story/Dragons/Moves/{dragon_move_file}) This dragon move does not contain any data.")
                            elif len(dm_lines) != 3:
                                print(f"Major Error ({config}Story/Dragons/Moves/{dragon_move_file}) This dragon move does not have the correct number of lines (3).")
                            else:
                                damage = dm_lines[0][0:dm_lines[0].index("\n")]
                                accuracy = dm_lines[1][0:dm_lines[1].index("\n")]
                                element = dm_lines[2]
                                if element == "":
                                    print(f"Major Error ({config}Story/Dragons/Moves/{dragon_move_file}) The element of this dragon move is none.")
                                if not damage.isnumeric():
                                    print(f"Major Error ({config}Story/Dragons/Moves/{dragon_move_file}) The damage of this dragon move is not a valid number (not a number).")
                                else:
                                    if int(damage) < 1:
                                        print(f"Minor Error ({config}Story/Dragons/Moves/{dragon_move_file}) The damage of this dragon move is less than 1.")
                                if not accuracy.isnumeric():
                                    print(f"Major Error ({config}Story/Dragons/Moves/{dragon_move_file}) The accuracy of this dragon move is not a valid number (not a number).")
                                else:
                                    if int(accuracy) < 1:
                                        print(f"Major Error ({config}Story/Dragons/Moves/{dragon_move_file}) The accuracy of this dragon move is less than 1.")
                                    if int(accuracy) > 100:
                                        print(f"Major Error ({config}Story/Dragons/Moves/{dragon_move_file}) The accuracy of this dragon move is over 100.")
                        continue
                    if "." not in dragon_file:
                        continue
                    with open(f"{config}Story/Dragons/{dragon_file}", "r") as d_f:
                        d_lines = d_f.readlines()
                    if len(d_lines) == 0:
                        print(f"Major Error ({config}Story/Dragons/{dragon_file}) This dragon file does not contain any data.")
                    elif len(d_lines) != 4:
                        print(f"Major Error ({config}Story/Dragons/{dragon_file}) This dragon file does not have the correct amount of lines (4).")
                    else:
                        move = d_lines[0][0:d_lines[0].index("\n")]
                        element = d_lines[1][0:d_lines[1].index("\n")]
                        level = d_lines[2][0:d_lines[2].index("\n")]
                        prestige = d_lines[3]
                        if move == "":
                            print(f"Major Error ({config}Story/Dragons/{dragon_file}) The move for this dragon is none.")
                        if element == "":
                            print(f"Major Error ({config}Story/Dragons/{dragon_file}) The element for this dragon is none.")
                        if not level.isnumeric():
                            print(f"Major Error ({config}Story/Dragons/{dragon_file}) The level for this dragon is not a valid number (not a number).")
                        else:
                            if int(level) < 1:
                                print(f"Major Error ({config}Story/Dragons/{dragon_file}) The level for this dragon is less than 1.")
                            if int(level) > 3000:
                                print(f"Major Error ({config}Story/Dragons/{dragon_file}) The level for this dragon is over the max possible level (3000).")
                        if not prestige.isnumeric():
                            print(f"Major Error ({config}Story/Dragons/{dragon_file}) The prestige for this dragon is not a valid number (not a number).")
                        else:
                            if int(prestige) < 1:
                                print(f"Major Error ({config}Story/Dragons/{dragon_file}) The prestige for this dragon is less than 1.")
            elif story_folder == "Bosses":
                boss_files = os.listdir(f"{config}Story/Bosses/")
                for boss_file in boss_files:
                    if boss_file == "Moves":
                        bmove_files = os.listdir(f"{config}/Story/Bosses/Moves/")
                        for bmove_file in bmove_files:
                            with open(f"{config}/Story/Bosses/Moves/{bmove_file}", "r") as bm_f:
                                bm_lines = bm_f.readlines()
                            if len(bm_lines) == 0:
                                print(f"Major Error ({config}/Story/Bosses/Moves/{bmove_file}) This story boss dragon move does not contain any data.")
                            elif len(bm_lines) != 2:
                                print(f"Major Error ({config}/Story/Bosses/Moves/{bmove_file}) This story boss dragon move does not have the correct number of lines (2).")
                            else:
                                damage = bm_lines[0][0:bm_lines[0].index("\n")]
                                accuracy = bm_lines[1]
                                if not damage.isnumeric():
                                    print(f"Major Error ({config}/Story/Bosses/Moves/{bmove_file}) This story boss dragon move's damage is not a valid number (not a number).")
                                else:
                                    if int(damage) < 1:
                                        print(f"Minor Error ({config}/Story/Bosses/Moves/{bmove_file}) This story boss dragon move's damage is less than 1.")
                                if not accuracy.isnumeric():
                                    print(f"Major Error ({config}/Story/Bosses/Moves/{bmove_file}) This story boss dragon move's accuracy is not a valid number (not a number).")
                                else:
                                    if int(accuracy) < 1:
                                        print(f"Major Error ({config}/Story/Bosses/Moves/{bmove_file}) This story boss dragon move's accuracy is less than 1.")
                                    if int(accuracy) > 100:
                                        print(f"Major Error ({config}/Story/Bosses/Moves/{bmove_file}) This story boss dragon move's accuracy is greater than 100.")
                        continue
                    if "." not in boss_file:
                        continue
                    with open(f"{config}Story/Bosses/{boss_file}", "r") as b_f:
                        b_lines = b_f.readlines()
                    if len(b_lines) == 0:
                        print(f"Major Error ({config}Story/Bosses/{boss_file}) This story boss dragon does not contain any data.")
                    elif len(b_lines) != 2:
                        print(f"Major Error ({config}Story/Bosses/{boss_file}) This story boss dragon does not have the correct number of lines (2).")
                    else:
                        level = b_lines[0][0:b_lines[0].index("\n")]
                        move = b_lines[1]
                        if move == "":
                            print(f"Major Error ({config}Story/Bosses/{boss_file}) This story boss dragon does not have a move.")
                        if not level.isnumeric():
                            print(f"Major Error ({config}Story/Bosses/{boss_file}) This story boss dragon's level is not a valid number (not a number).")
                        else:
                            if int(level) < 1:
                                print(f"Major Error ({config}Story/Bosses/{boss_file}) This story boss dragon's level is less than 1.")

for err in errs:
    print(err)
if len(errs) > 0:
    print("Please note if you have not converted to the correct format there will be many errors. Use the oldfix program to convert to the correct format.")
print(f"Total Errors Found: {len(errs)}")
