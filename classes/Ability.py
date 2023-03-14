class Ability:
    def __init__(self, action_log, name, damage, mana_cost):
        self.action_log = action_log
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    def cast(self, attacking_character, defending_character):
        # The attacking_character should reduce their mana to use the attack
        attacking_character.current_mana = attacking_character.current_mana - self.mana_cost
        # The defending_character should reduce their health
        defending_character.take_damage(self.damage)
        # A message should be displayed for the ability use
        print(f"{attacking_character.name} used it's special ability: {self.name}")
        self.action_log.add_action_list(f"{attacking_character.name} used it's special ability: {self.name}")

    def __str__(self):
        return self.name
