from classes.Ability import Ability
from classes.Enemy import Enemy


class Kappa(Enemy):
    # https://www.youtube.com/watch?v=pVkqUJBLy-o
    name = "Kappa"
    strength = 15
    defense = 0.2
    max_mana = 10
    max_health = 70
    boss = False

    def __init__(self, action_log):
        super(Kappa, self).__init__(action_log, self.name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Turtle Shell Throw", 15, 4),
            Ability(self.action_log, "Bite", 6, 2),
        ]
