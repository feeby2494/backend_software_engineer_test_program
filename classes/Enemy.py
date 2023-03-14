from classes.Ability import Ability
from random import choice
from classes.Character import Character


class Enemy(Character):
    # If you add any new messages here, they need to have n_or_no_n and enemy_name
    ENEMY_ENCOUNTER_MESSAGES = [
        "You see a{n_or_no_n} {enemy_name}!", "A{n_or_no_n} {enemy_name} has crossed your path!"
    ]

    def get_action(self):
        enemy_abilities = self.abilities
        # If you don't have enough mana to use a specific abiilty, the ability should not be selectable
        def check_ability_mana_cost(ability):
            return ability.mana_cost <= self.current_mana
        
        enemy_abilities = [ability for ability in filter(check_ability_mana_cost, enemy_abilities)]   
        # Randomly choose between all abilities and a regular attack
        # Regular attack should be returned as "Regular Attack"
        if "Regular Attack" not in enemy_abilities:
            enemy_abilities.append("Regular Attack")  
        enemy_action = choice(enemy_abilities)

        return enemy_action

    def display_enemy_encounter_message(self):
        enemy_encounter_message = choice(Enemy.ENEMY_ENCOUNTER_MESSAGES)
        n_or_no_n = ""

        if self.name[0].lower() in ["a", "e", "i", "o", "u"]:
            n_or_no_n = "n"

        print(enemy_encounter_message.format(n_or_no_n=n_or_no_n, enemy_name=self.name))
        self.action_log.add_action_list(f"\nFight {self.action_log.fight_number}\n")
        self.action_log.fight_number += 1
        self.action_log.add_action_list(enemy_encounter_message.format(n_or_no_n=n_or_no_n, enemy_name=self.name))
        print()

    def take_turn(self, player):
        action = self.get_action()

        if isinstance(action, Ability):
            self.use_ability(action, player)
        elif action == "Regular Attack":
            self.use_regular_attack(player)
        else:
            print(self, "did nothing.")
            self.action_log.add_action_list(f"{self} did nothing.")

        print()
