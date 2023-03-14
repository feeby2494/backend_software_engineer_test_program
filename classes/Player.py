from classes.Ability import Ability
from classes.Potion import Potion
from classes.Character import Character


class Player(Character):
    AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT = 1
    AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT = 0.05
    AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT = 1
    AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT = 10

    strength = 10
    defense = 0.25
    max_mana = 10
    max_health = 100

    def __init__(self, action_log, name):
        super(Player, self).__init__(action_log, name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Smash", 50, 5)
        ]

        self.potions = [
            Potion(self.action_log, "Health Potion", 0, 40, self.health_potions, "health"),
            Potion(self.action_log, "Mana Potion", 4, 0, self.mana_potions, "mana")
        ]

    def rest(self):
        self.current_mana += 3
        self.current_health += 30

        if self.current_mana > self.max_mana:
            self.current_mana = self.max_mana

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def level_up(self):

        def upgrade(choice):
            if choice == 's':
                self.strength += self.AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT
                self.action_log.add_action_list(f"Player choose to upgrade their strength to: {self.strength}")
            elif choice == 'd':
                self.defense += self.AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT
                self.action_log.add_action_list(f"Player choose to upgrade their defense to: {self.defense}")
            elif choice == 'm':
                self.max_mana += self.AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT
                self.action_log.add_action_list(f"Player choose to upgrade their max mana to: {self.max_mana}")
            elif choice == 'h':
                self.max_health += self.AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT
                self.action_log.add_action_list(f"Player choose to upgrade their max health to: {self.max_health}")
                
        # Finish the remainder of this function including validation and appropriate assignment

        print("You have 3 actions you can take:")
        print("    s = Increase strength by", self.AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT)
        print("    d = Increase defense by", self.AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT)
        print("    m = Increase max mana by", self.AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT)
        print("    h = Increase max health by", self.AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT)

        choices_are_valid = False

        while not choices_are_valid:
            # Example 1: s s d
            # Example 2: d h m
            # Example 3: m s d
            choices = input("Enter your 3 choices separated by spaces: ")
            choices = choices.split(' ')
            # Validate the choices
            if len(choices) == 3:
                if set(choices).issubset({'s', 'd', 'm', 'h'}):
                    choices_are_valid = True

                    #Do upgrades; Wanted to use map, but need side effects
                    for choice in choices:
                        upgrade(choice)                  
    
        print()

    def take_turn(self, enemy):
        is_invalid_input = True

        while is_invalid_input:
            is_invalid_input = False

            # Getting possible attacks first
            player_ablities = self.abilities

            # Getting potions
            player_potions = self.potions

            # IMPLEMENT: If the player doesn't have enough mana, they can't cast the ability
            def check_ability_mana_cost(ability):
                return ability.mana_cost <= self.current_mana
               
            player_ablities = [ability for ability in filter(check_ability_mana_cost, player_ablities)]
            
            print("r = Regular Attack")
            print("k = Attack with Sword")
            print("s = Smash")
            print("h = Drink Health Potion")
            print("m = Drink Mana Potion")

            action = input("Choose an action: ")

            print()

            if action == "r":
                self.use_regular_attack(enemy)
            elif action == "k":
                self.use_sword_attack(enemy)
            elif action == "s":
                if self.current_mana >= self.abilities[0].mana_cost:
                    self.use_ability(self.abilities[0], enemy)
                else:
                    print("You don't have enough mana to cast this ability.")
                    is_invalid_input = True
            elif action == "h":
                if self.health_potions >= 1:
                    print(self)
                    self.use_potion(self.potions[0], "health")
                else:
                    print("You don't have anymore potions left.")
                    is_invalid_input = True
            elif action == "m":
                if self.mana_potions >= 1:
                    self.use_potion(self.potions[1], "mana")
                else:
                    print("You don't have anymore potions left.")
                    is_invalid_input = True
            else:
                is_invalid_input = True
