from classes.Ability import Ability
from classes.Enemy import Enemy


class Bowser(Enemy):
    # https://www.youtube.com/watch?v=sFVYamNtgKQ
    name = "Bowser"
    strength = 20
    defense = 0.5
    max_mana = 20
    max_health = 170
    boss = True

    def __init__(self, action_log):
        super(Bowser, self).__init__(action_log, self.name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Claw Attack", 15, 3),
            Ability(self.action_log, "Fire Breath", 50, 7),
        ]