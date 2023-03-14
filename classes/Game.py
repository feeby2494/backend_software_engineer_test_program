from random import choice

from black_magic import get_player_and_enemy_info_box_lines
from classes.ActionLog import ActionLog
from classes.Chicken import Chicken
from classes.Kappa import Kappa
from classes.Totoro import Totoro
from classes.Little_Totoro import Little_Totoro
from classes.Bowser import Bowser
from classes.Player import Player


class Game:
    class PlayerDiedException(Exception):
        pass

    def __init__(self, number_of_enemies_to_kill=5):
        self.number_of_enemies_to_kill = number_of_enemies_to_kill

        self.action_log = ActionLog()

        player_name = input("Player Name: ").strip()
        self.player = Player(self.action_log, player_name)

        # Add additional enemies here
        self.enemies = [
            Chicken,
            Kappa,
            Totoro,
            Little_Totoro,
            Bowser,
        ]

        self.current_enemy = None

    def run(self):
        try:
            for i in range(self.number_of_enemies_to_kill):
                self.fight()

            # last turn fight a boss
            print("***************************************")
            print("Boss Level!")
            print("***************************************")
            self.action_log.add_action_list("***************************************\nBoss Level!\n***************************************")
            boss = True
            self.fight(boss)
            print("You have completed your journey, then died from natural causes")
            self.action_log.add_action_list("You have completed your journey, then died from natural causes")

        except self.PlayerDiedException:
            print("You died!")
            print(f"{self.current_enemy} killed {self.player}")
            print()
            print("Wasted!")
            print()
            self.action_log.add_action_list(f"You died!\n{self.current_enemy} killed {self.player}\nWasted!\n")
            pass
        
        self.action_log.write_action_log_to_file()

    def fight(self, boss=False):
        if boss:
            EnemyClass = self.get_final_boss()
        else:
            EnemyClass = self.get_random_enemy()
        self.current_enemy = EnemyClass(self.action_log)

        self.current_enemy.display_enemy_encounter_message()

        self.display_player_and_enemy_info()

        while self.current_enemy.current_health > 0 and self.player.current_health > 0:
            self.player.take_turn(self.current_enemy)
            self.current_enemy.take_turn(self.player)

            self.display_player_and_enemy_info()

        if self.player.current_health <= 0:
            raise self.PlayerDiedException("You died!")

        self.player.level_up()
        self.player.rest()

    def get_random_enemy(self):
        regular_enemies = list(filter(lambda enemy: enemy.boss == False, self.enemies))

        return choice(regular_enemies)
    
    def get_final_boss(self):
        boss_enemies = list(filter(lambda enemy: enemy.boss == True, self.enemies))

        return choice(boss_enemies)

    def display_player_and_enemy_info(self):
        for line in get_player_and_enemy_info_box_lines(self.player, self.current_enemy):
            print(line)

        print()
