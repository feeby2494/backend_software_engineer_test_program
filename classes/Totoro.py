from classes.Ability import Ability
from classes.Enemy import Enemy


class Totoro(Enemy):
    # https://www.youtube.com/watch?v=oETPccnOnDA
    name = "Totoro"
    strength = 10
    defense = 0.1
    max_mana = 20
    max_health = 200
    boss = True

    def __init__(self, action_log):
        super(Totoro, self).__init__(action_log, self.name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Spin Attack", 23, 5),
            Ability(self.action_log, "Power Yawn", 35, 7),
            Ability(self.action_log, "Grow Giant Tree", 0, 1),
            Ability(self.action_log, "Flying with Children", 0, 3)
        ]
