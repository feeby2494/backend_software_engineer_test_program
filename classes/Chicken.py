from classes.Ability import Ability
from classes.Enemy import Enemy


class Chicken(Enemy):
    # https://www.youtube.com/watch?v=miomuSGoPzI
    name = "Chicken"
    strength = 5
    defense = 0.1
    max_mana = 10
    max_health = 50
    boss = False

    def __init__(self, action_log):
        super(Chicken, self).__init__(action_log, self.name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Chicken Attack", 10, 3),
            Ability(self.action_log, "Eat Bug", 0, 1)
        ]
