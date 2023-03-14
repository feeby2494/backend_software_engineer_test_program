# Backend Software Engineer Test Program

## Game Information

The project presented here is a simple text-based turn-based RPG. In the game,
you will battle different enemies (one has been provided and the others are to
be implemented). Characters possess values relating to health, strength,
defense, and more. Every time you defeat an enemy, you will level up.

## Game Attributes

- strength: This value represents the amount of base damage your regular attack
  inflicts
- defense: This is a decimal value that represents what percent of damage will be
  blocked
    - If the attack is 10 damage and your defense is 0.1, then you will take 9
      damage
    - If the attack is 10 and your defense is 0.25, then you will take 8 damage,
      as it will round up. This defense protects against regular attacks as well
      as abilities
- max_mana: Your max mana. This can be affected by stat changes
- max_health: Your max health. This can be affected by stat changes

## Items for You to Implement

- Finish the Player.level_up() function
- Finish the Enemy.choose_action() function
- Finish the Ability.cast() function
- Add a new type of enemy. Follow the same setup as Chicken

## Bonus Items for You to Implement

- Finish the ActionLog.write_action_log_to_file() function
- Add all the necessary code to add actions to the ActionLog class
- Write the ActionLog to a file at the end of the game

Feel free to take liberties and make any changes to the project wherever you see
fit. The changes can be minor in detail or can be more creative in nature, such as changing how the game functions. This is meant to be a base and can be expanded
upon, changed, or improved in whatever way you desire. This is your project.
Show me your style and creativity. If you change the way the game functions,
please document it in a separate `.md` file.
