"""The main program for Hunt The Wumpus"""
from cave import Cave #Imports the cave class from the cave.py file
from character import Enemy #Imports the enemy class from the character.py file

cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")

harry = Enemy("Harry", "A dirty, smelly Wumpus")
harry.set_conversation("Come closer. I cannot see you.")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

current_cave = cavern
dead = False
while dead is False:
    print("\n")
    current_cave.get_details()
    inhabited = current_cave.get_character()
    if inhabited is not None:
        inhabited.describe()
    command = input("> ")
    if command in ["North", "South", "West", "East"]:
        current_cave = current_cave.move(command)
    elif command == "Talk":
        if inhabited is True:
            inhabited.talk()
    elif command == "Fight":
        if inhabited is not None and isinstance(inhabited, Enemy):
            fight_with = input("What do you want to fight with?: ")
            if inhabited.fight(fight_with) is True:
                print("Bravo, you win the battle.")
                current_cave.set_character(None)
            else:
                print("You have been defeated. GAME OVER")
                dead = True
            #Fights with the enemy
#End-of-file (EOF)
