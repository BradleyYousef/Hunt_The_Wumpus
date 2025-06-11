"""The main program for Hunt The Wumpus"""
from cave import Cave #Imports the cave class from the cave.py file
from character import Enemy #Imports the enemy class from the character.py file

cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
mineshaft = Cave("Mineshaft Entrance")
mineshaft.set_description("The entrance into the ancient Wumpus caves")
fork = Cave("Fork In The Road")
fork.set_description("A fork in the caves pathway")
grand = Cave("Grand Marsh")
grand.set_description("A swampy wetland covered in moss")
library = Cave("Sunken Library")
library.set_description("A withered library trapped in the moss")
thicket = Cave("Deadly Thicket")
thicket.set_description("A forest with many withered trees")
dump = Cave("Wet Dump")
dump.set_description("A wet pile of moss that appears to be smoking")
shopkeeper = Cave("Shopkeeper's Abode")
shopkeeper.set_description("A cabin hidden in the moss where the shopkeeper resides")
hole = Cave("Giant Hole")
hole.set_description("A giant hole that seems hard to get out of")
stairway = Cave("Royal Stairway")
stairway.set_description("A royal stairway with many armour stands lining the path")
citadel = Cave("Citadel")
citadel.set_description("The former sanctuary for civilisation")
path = Cave("Ruined Pathway")
path.set_description("A pathway eroded by time")
shrine = Cave("Ancient Shrine")
shrine.set_description("A shrine to the ancient sky lords")
insides = Cave("Ancient Shrine Insides")
insides.set_description("A secret area hidden behind the ancient shrine")
highland = Cave("Highland Glades")
highland.set_description("A windswept grassland")
city = Cave("Sky City")
city.set_description("A city in the clouds filled with the surviving people")
temple = Cave("Sky Temple")
temple.set_description("The temple to the last sky lord from ancient times")
arena = Cave("Sky Arena")
arena.set_description("The skyland's colossuem")
swamp = Cave("Gladiator's Swamp")
swamp.set_description("A swamp filled with moss and wumpus to fight")


harry = Enemy("Harry", "A dirty, smelly Wumpus")
harry.set_conversation("Come closer. I cannot see you.")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

cavern.link_caves(mineshaft, "North")
cavern.link_caves(fork, "South")
grotto.link_caves(fork, "East")
grotto.link_caves(grand, "West")

current_cave = mineshaft
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
