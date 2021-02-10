import os
from Dragon import Dragon
import json
from FileActions import create_file


while True:
    sure = input("Are you sure that you want to change file syntax to the new format? You will have to manually revert this if you want to go back. (You also could backup the files somewhere else). (Also want to point out the format file and read me for info files are not changed. Get it from the new program.) ALSO MAKE SURE YOU GOT THE CORRECT PATH TO YOUR CONFIG. YOU CANNOT USE inthisfolder FOR THIS. (y or n): ")
    if sure == "y":
        break
    if sure == "n":
        break
if sure == "n":
    print("Aborted.")
    exit(0)
if sure == "y":
    print("Starting conversion...")
    with open("config_loc.txt", "r") as f:
        path = f.readline()
    dur = os.listdir(f"{path}/Dragons/")
    for file in dur:
        if "." in file:
            print(f"Converting '{path}Dragons/{file}' to '{path}Dragons/{file[0:file.index('.')]}.json'")
            with open(f'{path}Dragons/{file}', "r") as f:
                lines = f.readlines()
                name = lines[0][lines[0].index(":")+2:lines[0].index("#")]
                element = lines[1][lines[1].index(":")+2:lines[1].index("!")]
                exp = int(lines[2][lines[2].index(":")+2:lines[2].index("$")])
                level = int(lines[3][lines[3].index(":")+2:lines[3].index("%")])
                # skip line 5 (index 4) because we no longer store haslasereyes.
                boss_num = int(lines[5][lines[5].index(":")+2:lines[5].index("&")])
                prestige = int(lines[6][lines[6].index(":")+2:lines[6].index("@")])
                boss3_num = int(lines[7][lines[7].index(":")+2:lines[7].index("*")])
                story_num = int(lines[8][lines[8].index(":")+2:lines[8].index("(")])
                drg = Dragon(name, element, None, level, prestige, boss_num, boss3_num, story_num, exp)
            with open(f"{path}Dragons/{file[0:file.index('.')]}.json", "w+") as j:
                json.dump(drg.get_dragon_dictionary(), j)
            os.remove(f"{path}Dragons/{file}")
        else:
            us_dur = os.listdir(f"{path}Dragons/{file}/")
            for other_file in us_dur:
                if "." in other_file:
                    print(f"Converting '{path}Dragons/{file}/{other_file}' to '{path}Dragons/{file}/{other_file[0:other_file.index('.')]}.json'")
                    with open(f'{path}Dragons/{file}/{other_file}', "r") as f:
                        lines = f.readlines()
                        name = lines[0][lines[0].index(":")+2:lines[0].index("#")]
                        element = lines[1][lines[1].index(":")+2:lines[1].index("!")]
                        exp = int(lines[2][lines[2].index(":")+2:lines[2].index("$")])
                        level = int(lines[3][lines[3].index(":")+2:lines[3].index("%")])
                        # skip line 5 (index 4) because we no longer store haslasereyes.
                        boss_num = int(lines[5][lines[5].index(":")+2:lines[5].index("&")])
                        prestige = int(lines[6][lines[6].index(":")+2:lines[6].index("@")])
                        boss3_num = int(lines[7][lines[7].index(":")+2:lines[7].index("*")])
                        story_num = int(lines[8][lines[8].index(":")+2:lines[8].index("(")])
                        drg = Dragon(name, element, None, level, prestige, boss_num, boss3_num, story_num, exp)
                    with open(f"{path}Dragons/{file}/{other_file[0:other_file.index('.')]}.json", "w+") as j:
                        json.dump(drg.get_dragon_dictionary(), j)
                    os.remove(f"{path}Dragons/{file}/{other_file}")
                else:
                    print(f"Converting '{path}Dragons/{file}/{other_file}/data.txt' to '{path}Dragons/{file}/{other_file}/data.json'")
                    with open(f"{path}Dragons/{file}/{other_file}/data.txt", "r") as k:
                        d_lines = k.readline()
                        lst = [int(x) for x in d_lines.split("|")]
                    new_lst = []
                    for obj in lst:
                        if obj != 0:
                            new_lst.append(obj)
                    with open(f"{path}Dragons/{file}/{other_file}/data.json", "w+") as l:
                        json.dump(new_lst, l)
                    os.remove(f"{path}Dragons/{file}/{other_file}/data.txt")
    config_dur = os.listdir(f"{path}Config/")
    for folder in config_dur:
        if "." in folder:
            continue
        elif folder == "Achievements":
            ach_files = os.listdir(f"{path}Config/Achievements/")
            for ach_file in ach_files:
                if "." not in ach_file:
                    continue
                print(f"Converting {path}Config/Achievements/{ach_file} to the new format.")
                with open(f"{path}Config/Achievements/{ach_file}", "r") as ach_f:
                    ach_lines = ach_f.readlines()
                    actions = ach_lines[0][ach_lines[0].index(":")+2:ach_lines[0].index("!")]
                    numbers = ach_lines[1][ach_lines[1].index(":")+2:ach_lines[1].index("@")]
                    message = ach_lines[2][ach_lines[2].index(":")+2:ach_lines[2].index("#")]
                with open(f"{path}Config/Achievements/{ach_file}", "w+") as ach_f2:
                    f2_lines = [f"{actions}\n", f"{numbers}\n", f"{message}"]
                    ach_f2.writelines(f2_lines)
        elif folder == "DragonBosses":
            db_files = os.listdir(f"{path}Config/DragonBosses/")
            for db_file in db_files:
                if db_file == "Moves":
                    move_files = os.listdir(f"{path}Config/DragonBosses/Moves/")
                    for move_file in move_files:
                        print(f"Converting {path}Config/DragonBosses/Moves/{move_file} to the new format.")
                        with open(f"{path}Config/DragonBosses/Moves/{move_file}", "r") as mf:
                            mf_lines = mf.readlines()
                            name = mf_lines[0][mf_lines[0].index(":")+2:mf_lines[0].index("#")]
                            damage = mf_lines[1][mf_lines[1].index(":")+2:mf_lines[1].index("$")]
                            accuracy = mf_lines[2][mf_lines[2].index(":")+2:mf_lines[2].index("%")]
                        with open(f"{path}Config/DragonBosses/Moves/{move_file}", "w+") as mf2:
                            m2_lines = [f"{name}\n", f"{damage}\n", f"{accuracy}"]
                            mf2.writelines(m2_lines)
                    continue
                elif "." not in db_file:
                    continue
                print(f"Converting {path}Config/DragonBosses/{db_file} to the new format.")
                with open(f"{path}Config/DragonBosses/{db_file}", "r") as db_f:
                    db_lines = db_f.readlines()
                    name = db_lines[0][db_lines[0].index(":")+2:db_lines[0].index("#")]
                    level = db_lines[1][db_lines[1].index(":")+2:db_lines[1].index("$")]
                    move = db_lines[2][db_lines[2].index(":")+2:db_lines[2].index("*")]
                    boss_number = db_lines[3][db_lines[3].index(":")+2:db_lines[3].index("^")]
                with open(f"{path}Config/DragonBosses/{db_file}", "w+") as db_f2:
                    d2_lines = [f"{name}\n", f"{level}\n", f"{move}\n", f"{boss_number}"]
                    db_f2.writelines(d2_lines)
        elif folder == "DragonBosses3":
            db3_files = os.listdir(f"{path}Config/DragonBosses3/")
            for db3_file in db3_files:
                if db3_file == "Moves":
                    move3_files = os.listdir(f"{path}Config/DragonBosses3/Moves/")
                    for move3_file in move3_files:
                        print(f"Converting {path}Config/DragonBosses3/Moves/{move3_file} to the new format.")
                        with open(f"{path}Config/DragonBosses3/Moves/{move3_file}", "r") as mf3:
                            mf3_lines = mf3.readlines()
                            name = mf3_lines[0][mf3_lines[0].index(":")+2:mf3_lines[0].index("#")]
                            damage = mf3_lines[1][mf3_lines[1].index(":")+2:mf3_lines[1].index("$")]
                            accuracy = mf3_lines[2][mf3_lines[2].index(":")+2:mf3_lines[2].index("%")]
                        with open(f"{path}Config/DragonBosses3/Moves/{move3_file}", "w+") as mf23:
                            m23_lines = [f"{name}\n", f"{damage}\n", f"{accuracy}"]
                            mf23.writelines(m23_lines)
                    continue
                elif "." not in db3_file:
                    continue
                print(f"Converting {path}Config/DragonBosses3/{db3_file} to the new format.")
                with open(f"{path}Config/DragonBosses3/{db3_file}", "r") as db3_f:
                    db3_lines = db3_f.readlines()
                    name = db3_lines[0][db3_lines[0].index(":")+2:db3_lines[0].index("#")]
                    level = db3_lines[1][db3_lines[1].index(":")+2:db3_lines[1].index("$")]
                    move = db3_lines[2][db3_lines[2].index(":")+2:db3_lines[2].index("*")]
                    boss_number = db3_lines[3][db3_lines[3].index(":")+2:db3_lines[3].index("^")]
                with open(f"{path}Config/DragonBosses3/{db3_file}", "w+") as db_f23:
                    d23_lines = [f"{name}\n", f"{level}\n", f"{move}\n", f"{boss_number}"]
                    db_f23.writelines(d23_lines)
        elif folder == "Elements":
            print("No need to convert elements, they work the same!")
        elif folder == "Forms":
            form_folders = os.listdir(f"{path}Config/Forms/")
            for form_folder in form_folders:
                form_files = os.listdir(f"{path}Config/Forms/{form_folder}/")
                for form_file in form_files:
                    print(f"Converting {path}Config/Forms/{form_folder}/{form_file} to the new format.")
                    with open(f"{path}Config/Forms/{form_folder}/{form_file}", "r") as fr_f:
                        fr_lines = fr_f.readlines()
                        multi = fr_lines[0][fr_lines[0].index(":")+2:fr_lines[0].index("x")]
                        level = fr_lines[1][fr_lines[1].index(":")+2:fr_lines[1].index("#")]
                    with open(f"{path}Config/Forms/{form_folder}/{form_file}", "w+") as fr_f2:
                        f2_lines = [f"{multi}\n", f"{level}"]
                        fr_f2.writelines(f2_lines)
        elif folder == "Moves":
            move_files = os.listdir(f"{path}Config/Moves/")
            for move_file in move_files:
                print(f"Converting {path}Config/Moves/{move_file} to the new format.")
                with open(f"{path}Config/Moves/{move_file}", "r") as mv_f:
                    mv_lines = mv_f.readlines()
                    name = mv_lines[0][mv_lines[0].index(":")+2:mv_lines[0].index("#")]
                    element = mv_lines[1][mv_lines[1].index(":")+2:mv_lines[1].index("!")]
                    damage = mv_lines[2][mv_lines[2].index(":")+2:mv_lines[2].index("$")]
                    accuracy = mv_lines[3][mv_lines[3].index(":")+2:mv_lines[3].index("%")]
                    level_req = mv_lines[4][mv_lines[4].index(":")+2:mv_lines[4].index("&")]
                    unlock = mv_lines[5][mv_lines[5].index(":")+2:mv_lines[5].index(")")]
                with open(f"{path}Config/Moves/{move_file}", "w+") as mv_f2:
                    mv2_lines = [f"{name}\n", f"{element}\n", f"{damage}\n", f"{accuracy}\n", f"{level_req}\n", f"{unlock}"]
                    mv_f2.writelines(mv2_lines)
        elif folder == "Other":
            other_files = os.listdir(f"{path}Config/Other/")
            for other_file in other_files:
                if other_file == "expcalcmultiplier.txt":
                    continue
                if other_file == "ver.txt":
                    continue
                print(f"Converting {path}Config/Other/{other_file} to the new format.")
                if other_file == "fontsize.txt":
                    with open(f"{path}Config/Other/{other_file}", "r") as font_f:
                        font_lines = font_f.readlines()
                        size = font_lines[0][font_lines[0].index(":")+2:font_lines[0].index(")")]
                    with open(f"{path}Config/Other/{other_file}", "w+") as font_f2:
                        font_f2.writelines([f"{size}"])
                if other_file == "healthmultiplier.txt":
                    with open(f"{path}Config/Other/{other_file}", "r") as health_f:
                        health_lines = health_f.readlines()
                        health_mult = health_lines[0][health_lines[0].index(":")+2:health_lines[0].index("*")]
                    with open(f"{path}Config/Other/{other_file}", "w+") as health_f2:
                        health_f2.writelines([f"{health_mult}"])
                if other_file == "maxprestige.txt":
                    with open(f"{path}Config/Other/{other_file}", "r") as pres_f:
                        pres_lines = pres_f.readlines()
                        max_pres = pres_lines[0][pres_lines[0].index(":")+2:pres_lines[0].index("(")]
                    with open(f"{path}Config/Other/{other_file}", "w+") as pres_f2:
                        pres_f2.writelines([f"{max_pres}"])
            print(f"Creating new boss health multiplier file: {path}Config/Other/bosshealthmultiplier.txt and setting it to 200.")
            create_file(f"{path}Config/Other/bosshealthmultiplier.txt", "200")
        elif folder == "Story":
            story_folders = os.listdir(f"{path}Config/Story/")
            for story_folder in story_folders:
                if story_folder == "Dialogue":
                    continue
                elif story_folder == "Bosses":
                    boss_files = os.listdir(f"{path}Config/Story/Bosses/")
                    for boss_file in boss_files:
                        if boss_file == "Moves":
                            bossm_files = os.listdir(f"{path}Config/Story/Bosses/Moves/")
                            for bossm_file in bossm_files:
                                print(f"Converting {path}Config/Story/Bosses/Moves/{bossm_file} to the new format.")
                                with open(f"{path}Config/Story/Bosses/Moves/{bossm_file}", "r") as bm_f:
                                    bm_lines = bm_f.readlines()
                                    damage = bm_lines[0][bm_lines[0].index(":")+2:bm_lines[0].index("!")]
                                    accuracy = bm_lines[1][bm_lines[1].index(":")+2:bm_lines[1].index("@")]
                                with open(f"{path}Config/Story/Bosses/Moves/{bossm_file}", "w+") as bm_f2:
                                    bm2_lines = [f"{damage}\n", f"{accuracy}"]
                                    bm_f2.writelines(bm2_lines)
                            continue
                        print(f"Converting {path}Config/Story/Bosses/{boss_file} to the new format.")
                        with open(f"{path}Config/Story/Bosses/{boss_file}", "r") as sb_f:
                            sb_lines = sb_f.readlines()
                            level = sb_lines[0][sb_lines[0].index(":")+2:sb_lines[0].index("!")]
                            move = sb_lines[1][sb_lines[1].index(":")+2:sb_lines[1].index("@")]
                        with open(f"{path}Config/Story/Bosses/{boss_file}", "w+") as sb_f2:
                            sb2_lines = [f"{level}\n", f"{move}"]
                            sb_f2.writelines(sb2_lines)
                elif story_folder == "Dragons":
                    dragon_files = os.listdir(f"{path}Config/Story/Dragons/")
                    for dragon_file in dragon_files:
                        if dragon_file == "Moves":
                            move_files = os.listdir(f"{path}Config/Story/Dragons/Moves/")
                            for move_file in move_files:
                                print(f"Converting {path}Config/Story/Dragons/Moves/{move_file} to the new format.")
                                with open(f"{path}Config/Story/Dragons/Moves/{move_file}", "r") as dm_f:
                                    dm_lines = dm_f.readlines()
                                    damage = dm_lines[0][dm_lines[0].index(":")+2:dm_lines[0].index("!")]
                                    accuracy = dm_lines[1][dm_lines[1].index(":")+2:dm_lines[1].index("@")]
                                    element = dm_lines[2][dm_lines[2].index(":")+2:dm_lines[2].index("#")]
                                with open(f"{path}Config/Story/Dragons/Moves/{move_file}", "w+") as dm_f2:
                                    dm2_lines = [f"{damage}\n", f"{accuracy}\n", f"{element}"]
                                    dm_f2.writelines(dm2_lines)
                            continue
                        print(f"Converting {path}Config/Story/Dragons/{dragon_file} to the new format.")
                        with open(f"{path}Config/Story/Dragons/{dragon_file}", "r") as sd_f:
                            sd_lines = sd_f.readlines()
                            move = sd_lines[0][sd_lines[0].index(":")+2:sd_lines[0].index("!")]
                            element = sd_lines[1][sd_lines[1].index(":")+2:sd_lines[1].index("@")]
                            level = sd_lines[2][sd_lines[2].index(":")+2:sd_lines[2].index("#")]
                            prestige = sd_lines[3][sd_lines[3].index(":")+2:sd_lines[3].index("$")]
                        with open(f"{path}Config/Story/Dragons/{dragon_file}", "w+") as sd_f2:
                            sd2_lines = [f"{move}\n", f"{element}\n", f"{level}\n", f"{prestige}"]
                            sd_f2.writelines(sd2_lines)
                elif story_folder == "Order":
                    order_files = os.listdir(f"{path}Config/Story/Order/")
                    for order_file in order_files:
                        print(f"Converting {path}Config/Story/Order/{order_file} to the new format.")
                        with open(f"{path}Config/Story/Order/{order_file}", "r") as o_f:
                            o_lines = o_f.readlines()
                            dialogue = o_lines[0][o_lines[0].index(":")+2:o_lines[0].index("!")]
                            fight = o_lines[1][o_lines[1].index(":")+2:o_lines[1].index("@")]
                            dragon = o_lines[2][o_lines[2].index(":")+2:o_lines[2].index("#")]
                            boss = o_lines[3][o_lines[3].index(":")+2:o_lines[3].index("$")]
                        with open(f"{path}Config/Story/Order/{order_file}", "w+") as o_f2:
                            o2_lines = [f"{dialogue}\n", f"{fight}\n", f"{dragon}\n", f"{boss}"]
                            o_f2.writelines(o2_lines)
    print("Finished Conversion!")
