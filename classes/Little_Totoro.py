from classes.Ability import Ability
from classes.Enemy import Enemy


class Little_Totoro(Enemy):
    # https://www.youtube.com/watch?v=YJtoJ6t4qpA
    name = "Little Totoro"
    strength = 3
    defense = 0.1
    max_mana = 10
    max_health = 40
    boss = False

    def __init__(self, action_log):
        super(Little_Totoro, self).__init__(action_log, self.name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Throw an acorn", 10, 5),
            Ability(self.action_log, "Try to turn invisable and run away", 0, 3),
        ]