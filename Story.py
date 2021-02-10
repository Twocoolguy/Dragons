from fight import start_fight


class Story:
    def __init__(self, name, boss, dragon, dialogue):
        self.name = name
        self.boss = boss
        self.dragon = dragon
        self.dialogue = dialogue

    def equals(self, story):
        """Checks if another instance of this type of object is equal to this."""
        return story.name == self.name

    def start(self, dragon, dragon_move, dragon_form, user):
        """Starts the story mode."""
        # Start with fighting dragon
        # Second fight is the boss.
        # Third is the dialogue
        # Lastly modify dragon.
        won = False
        won2 = False
        if self.dragon is not None:
            won = start_fight(dragon, dragon_move, dragon_form, self.dragon, self.dragon.get_random_move(), self.dragon.get_random_form(), True, user)
        else:
            won = True
        if self.boss is not None and won:
            new_drag = user.get_dragon(dragon.name)
            won2 = start_fight(new_drag, dragon_move, dragon_form, self.boss, self.boss.move, None, True, user)
        else:
            won2 = True

        if won and won2:
            new_new_drag = user.get_dragon(dragon.name)
            if len(new_new_drag.config_reader.stories) > new_new_drag.story_number:
                new_new_drag.story_number += 1
            user.modify_dragon(new_new_drag)
            print(self.dialogue.message)
        else:
            print("You lost. You will need to retry and win to continue forward.")

    def get_file_lines(self):
        """Gets a list of each line of this story."""
        if self.dragon is not None:
            dragon_lines = self.dragon.get_file_lines()
            dragon_name = dragon_lines["name"][0:dragon_lines["name"].index(".")]
        else:
            dragon_lines = None
            dragon_name = "none"
        if self.boss is not None:
            boss_lines = self.boss.get_file_lines()
            boss_name = boss_lines["name"][0:boss_lines["name"].index(".")]
        else:
            boss_lines = None
            boss_name = "none"
        fight = "none"
        if self.boss is not None or self.dragon is not None:
            fight = "true"
        dialogue_name = self.dialogue.name
        dialogue_lines = {"name": f"{self.name}", "lines":[f"{self.message}"]}
        lines = [
            f"{dialogue_name}\n",
            f"{fight}\n",
            f"{dragon_name}\n",
            f"{boss_name}"
        ]
        return [{"name": f"{self.name}", "lines": lines}, dragon_lines, boss_lines, dialogue_lines]
