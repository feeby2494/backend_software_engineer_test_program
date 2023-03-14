class Potion:
    class NoPotionsLeft(Exception):
        pass

    def __init__(self, action_log, name, mana_replenish, health_replenish, inventory, potion_type):
        self.action_log = action_log
        self.name = name
        self.mana_replenish = mana_replenish
        self.health_replenish = health_replenish
        self.inventory = inventory
        self.potion_type = potion_type

    def drink(self, drinking_character, potion_type):
        # The drinking character uses no mana for this
        # need to check if drinking_character has enough of these potions
        try:
            if self.inventory <= 0:
                raise self.NoPotionsLeft("No more potions left")
            
            # The defending_character should either get more health or mana
            if potion_type == "health":
                drinking_character.replenish_health(self.health_replenish)
                drinking_character.health_potions -= 1
            elif potion_type == "mana":
                drinking_character.replenish_mana(self.mana_replenish)
                drinking_character.mana_potions -= 1

        except self.NoPotionsLeft:
            return "No more potions left"
        
        # A message should be displayed for the potion used
        print(f"{drinking_character.name} drank: {self.name}")
        self.action_log.add_action_list(f"{drinking_character.name} drank: {self.name}")
