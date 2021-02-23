from random import choice, randint
from Dragon import Dragon


def start_fight(dragon1, dragon1_move, dragon1_form, dragon2, dragon2_move, dragon2_form, story, user):
    """Starts a fight between the two dragons. Dragon2 is a cpu."""
    fighting = True
    turn = None  # if turn is 1, dragon1 goes first. if turn is 2 dragon2 goes first.
    # Hp is: level * healthmult * prestige
    dragon1_hp = dragon1.level * dragon1.config_reader.health_multi * dragon1.prestige
    dragon2_hp = dragon2.level * dragon1.config_reader.health_multi * dragon2.prestige
    if dragon2.boss:
        dragon2_hp = dragon2.level * dragon1.config_reader.bosshealth_multiplier * dragon2.prestige
    attacks_made = 0  # Gets the number of attacks made to calculate exp gained.
    if not dragon2.boss:
        print(f"Fight: \nDragon: {dragon1.name} Element: {dragon1.element} Level: {dragon1.level} Prestige {dragon1.prestige}\nvs.\nDragon: {dragon2.name} Element: {dragon2.element} Level: {dragon2.level} Prestige: {dragon2.prestige}. Start!")
    else:
        print(f"Fight: \nDragon: {dragon1.name} Element: {dragon1.element} Level: {dragon1.level} Prestige {dragon1.prestige}\nvs.\nBoss: {dragon2.name} Level: {dragon2.level}\nStart!")
    while fighting:
        if turn is None:
            turn = randint(1, 2)
        elif turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1
        hit_chance = randint(1, 100)  # Getting random number 1 - 100 for accuracy check.
        if turn == 1:
            damage = dragon1_move.damage * dragon1.level * dragon1.prestige
            accuracy = dragon1_move.accuracy

            if dragon1_form != None:
                accuracy = dragon1_move.accuracy/dragon1_form.multiplier
                damage = damage / 4*dragon1_form.multiplier

            if hit_chance > accuracy:  # This is a miss.
                print(f"{dragon1.name}'s attack {dragon1_move.name} missed! {dragon2.name}'s turn!")
                continue
            else:
                attacks_made += 1
                dragon2_hp -= damage
                if dragon2_hp <= 0:
                    print(f"{dragon1.name}'s attack {dragon1_move.name} hit and did {damage} and killed {dragon2.name}. Fight over.")
                    fighting = False
                    break
                print(f"{dragon1.name}'s attack {dragon1_move.name} hit and did {damage} to the other dragon leaving them at {dragon2_hp} HP! {dragon2.name}'s turn!")
        if turn == 2:
            damage = dragon2_move.damage * dragon2.level * dragon2.prestige
            accuracy = dragon2_move.accuracy
            if dragon2.boss and not story:
                damage = dragon2_move.damage * dragon2.level * dragon2.prestige / 4
            if dragon2_form is not None:
                accuracy = dragon2_move.accuracy/dragon2_form.multiplier
                damage = damage / 4*dragon2_form.multiplier

            if hit_chance > accuracy:  # This is a miss.
                print(f"{dragon2.name}'s attack {dragon2_move.name} missed! {dragon1.name}'s turn!")
            else:
                dragon1_hp -= damage
                if dragon1_hp <= 0:
                    print(f"{dragon2.name}'s attack {dragon2_move.name} hit and did {damage} and killed {dragon1.name}. Fight over.")
                    fighting = False
                    break
                print(f"{dragon2.name}'s attack {dragon2_move.name} hit and did {damage} to the other dragon leaving them at {dragon1_hp} HP! {dragon1.name}'s turn!")
    exp_gain = (int(dragon1.config_reader.exp_multi) * attacks_made)/2
    won = "Lost"
    if dragon2_hp <= 0:
        won = "Won"
        exp_gain = exp_gain * 2
        if dragon2.boss and len(dragon1.config_reader.bosses) > dragon1.boss_number and not story:
            dragon1.boss_number = dragon1.boss_number + 1
            print("You can now go to the next boss fight!")
        elif dragon2.boss and not story:
            print("You have beaten all of the bosses. Congrats!")
    elif dragon2.boss and not story:
        print("You will need to beat this boss before continuing to the next one.")
    err = None
    if dragon2.boss and not story:
        if won == "Won":
            err = dragon1.gain_exp(exp_gain)
        else:
            exp_gain = 0.0
    else:
        err = dragon1.gain_exp(exp_gain)
    if err != -1:
        user.modify_dragon(dragon1)
    if dragon1.level == 3000:
        print(f"You {won}! {dragon1.name} didn't gain any exp.")
    else:
        print(f"You {won}! {dragon1.name} gained {exp_gain} exp.")
    if won == "Lost":
        return False
    if won == "Won":
        if dragon2.boss and len(dragon1.config_reader.bosses) > dragon1.boss_number and not story and err == -1:
            user.modify_dragon(dragon1)
        return True


def boss3_start(dragon1, dragon1_move, dragon1_form, dragon2, dragon2_move, dragon2_form, dragon3, dragon3_move, dragon3_form, boss, user):
    """Start a boss3 fight."""
    fighting = True
    turn = None  # if turn is 1, dragon1-3 goes first. if turn is 2 boss goes first.
    # Hp is: level * healthmult * prestige
    dragon1_hp = dragon1.level * dragon1.config_reader.health_multi * dragon1.prestige
    dragon2_hp = dragon2.level * dragon1.config_reader.health_multi * dragon2.prestige
    dragon3_hp = dragon3.level * dragon1.config_reader.health_multi * dragon3.prestige
    boss_hp = boss.level * dragon1.config_reader.bosshealth_multiplier * boss.prestige
    dragon1_dead = False
    dragon2_dead = False
    dragon3_dead = False
    attacks_made = 0  # Gets the number of attacks made to calculate exp gained.
    print(f"Fight: \nDragon: {dragon1.name} Element: {dragon1.element} Level: {dragon1.level} Prestige {dragon1.prestige}\nDragon: {dragon2.name} Element: {dragon2.element} Level: {dragon2.level} Prestige {dragon2.prestige}\nDragon: {dragon3.name} Element: {dragon3.element} Level: {dragon3.level} Prestige {dragon3.prestige}\nvs.\nBoss: {dragon2.name} Level: {dragon2.level}\nStart!")
    while fighting:
        if turn is None:
            turn = randint(1, 2)
        elif turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1
        hit_chance = randint(1, 100)  # Getting random number 1 - 100 for accuracy check.
        if turn == 1:
            damage1 = dragon1_move.damage * dragon1.level * dragon1.prestige
            accuracy1 = dragon1_move.accuracy
            damage2 = dragon2_move.damage * dragon2.level * dragon2.prestige
            accuracy2 = dragon2_move.accuracy
            damage3 = dragon3_move.damage * dragon3.level * dragon3.prestige
            accuracy3 = dragon3_move.accuracy

            if dragon1_form != None:
                accuracy1 = dragon1_move.accuracy/dragon1_form.multiplier
                damage1 = damage1 / 4*dragon1_form.multiplier
            if dragon2_form != None:
                accuracy2 = dragon2_move.accuracy/dragon2_form.multiplier
                damage2 = damage2 / 4*dragon2_form.multiplier
            if dragon3_form != None:
                accuracy3 = dragon3_move.accuracy/dragon3_form.multiplier
                damage3 = damage3 / 4*dragon3_form.multiplier
            damages = [damage1, damage2, damage3]
            accuracys = [accuracy1, accuracy2, accuracy3]
            dragons = [dragon1, dragon2, dragon3]
            dragon_moves = [dragon1_move, dragon2_move, dragon3_move]
            for index in range(0, len(damages)):
                if index == 0 and dragon1_dead:
                    continue
                if index == 1 and dragon2_dead:
                    continue
                if index == 2 and dragon3_dead:
                    continue
                accuracy = accuracys[index]
                damage = damages[index]
                drag = dragons[index]
                drag_move = dragon_moves[index]
                hit_chance = randint(1, 100)
                if hit_chance > accuracy:  # This is a miss.
                    print(f"{drag.name}'s attack {drag_move.name} missed! Next Dragons turn!")
                    continue
                else:
                    attacks_made += 1
                    boss_hp -= damage
                    if boss_hp <= 0:
                        print(f"{drag.name}'s attack {drag.name} hit and did {damage} and killed {boss.name}. Fight over.")
                        fighting = False
                        break
                    print(f"{drag.name}'s attack {drag_move.name} hit and did {damage} to the other dragon leaving them at {boss_hp} HP! Next Dragons turn!")
            print(f"It is now {boss.name}'s turn!")
        if turn == 2:
            accuracy = boss.move.accuracy
            damage = boss.move.damage * boss.level * boss.prestige / 4
            if hit_chance > accuracy:  # This is a miss.
                print(f"{boss.name}'s attack {boss.move.name} missed! Other Dragon's turns!")
            else:
                dragon1_hp -= damage
                dragon2_hp -= damage
                dragon3_hp -= damage
                if dragon1_hp <= 0:
                    print(f"{boss.name}'s attack {boss.move.name} hit and did {damage} and killed {dragon1.name}.")
                    dragon1_dead = True
                if dragon2_hp <= 0:
                    print(f"{boss.name}'s attack {boss.move.name} hit and did {damage} and killed {dragon2.name}.")
                    dragon2_dead = True
                if dragon3_hp <= 0:
                    print(f"{boss.name}'s attack {boss.move.name} hit and did {damage} and killed {dragon3.name}.")
                    dragon3_dead = True
                if dragon1_dead and dragon2_dead and dragon3_dead:
                    print(f"Boss killed all of your dragons, fight over.")
                    fighting = False
                    break
                print(f"{boss.name}'s attack {boss.move.name} hit and did {damage} to the other dragons leaving them at {dragon1_hp} HP, {dragon2_hp} HP, and {dragon3_hp} HP! Other Dragon's turns!")
    exp_gain = (int(dragon1.config_reader.exp_multi) * attacks_made)/2
    won = "Lost"
    if boss_hp <= 0:
        won = "Won"
        exp_gain = exp_gain * 2
        if len(dragon1.config_reader.bosses3) > dragon1.boss3_number:
            dragon1.boss3_number += 1
            dragon2.boss3_number += 1
            dragon3.boss3_number += 1
            print("You finished the boss3 and now you can go to the next one!")
        else:
            print("You have finished all of the boss3 bosses available to you at the moment.")
    else:
        exp_gain = 0.0
        print("Since you lost, you will need to defeat this dragon boss3 before going to the next one.")
    err1 = dragon1.gain_exp(exp_gain)
    err2 = dragon2.gain_exp(exp_gain)
    err3 = dragon3.gain_exp(exp_gain)
    if err1 != -1:
        user.modify_dragon(dragon1)
    if err2 != -1:
        user.modify_dragon(dragon2)
    if err3 != -1:
        user.modify_dragon(dragon3)
    print(f"You {won}! All of your dragons gained {exp_gain} exp unless they were already max level.")
    if won == "Lost":
        return False
    if won == "Won":
        if len(dragon1.config_reader.bosses3) > dragon1.boss_number3 and err1 == -1:
            user.modify_dragon(dragon1)
        if len(dragon1.config_reader.bosses3) > dragon2.boss_number3 and err2 == -1:
            user.modify_dragon(dragon2)
        if len(dragon1.config_reader.bosses3) > dragon3.boss_number3 and err3 == -1:
            user.modify_dragon(dragon3)
        return True


def gen_rand(level, prestige, config_reader):
    """Generates a random dragon with the given level and prestige."""
    element = choice(config_reader.elements)
    name = "CPU"
    level = level
    prestige = prestige
    boss_number = 0
    boss_number3 = 0
    story_number = 0
    exp = 0
    cpu_drag = Dragon(name, element, config_reader, level, prestige, boss_number, boss_number3, story_number, exp)
    return cpu_drag


