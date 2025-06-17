"""The main program for Hunt The Wumpus"""
from cave import Cave #Imports the cave class from the cave.py file
from character import Enemy #Imports the enemy class from the character.py file
from character import Character #Imports the character class from the character.py file

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
harry.set_conversation("At this fork in the road there is a giant hole to steep to go down normally and a large grotto that I will eat you in.")
harry.set_weakness("vegemite")
harry.set_health(10)
fork.set_character1(harry)

larry = Enemy("Larry", "An asian Wumpus")
larry.set_conversation("You killed harry. I am Larry and I'm gonna eat your dog")
larry.set_weakness("engrish")
larry.set_health(10)
cavern.set_character2(larry)


shopkeep = Character("Shopman", "A salesman to help you on your journey")
shopkeep.set_conversation("Hello traveler I have some items to sell you for your Wump coins")
shopkeeper.set_character1(shopkeep)

cavern.link_caves(mineshaft, "north")
cavern.link_caves(fork, "south")
grotto.link_caves(fork, "east")
grotto.link_caves(grand, "west")
dungeon.link_caves(citadel, "north")
mineshaft.link_caves(highland, "north")
mineshaft.link_caves(cavern, "south")
fork.link_caves(cavern, "north")
fork.link_caves(grotto, "west")
fork.link_caves(hole, "east")
grand.link_caves(grotto, "east")
grand.link_caves(library, "north")
grand.link_caves(thicket, "west")
grand.link_caves(dump, "south")
library.link_caves(grand, "south")
thicket.link_caves(grand, "east")
thicket.link_caves(swamp, "west")
dump.link_caves(grand, "north")
dump.link_caves(shopkeeper, "south")
shopkeeper.link_caves(dump, "north")
hole.link_caves(fork, "west")
hole.link_caves(stairway, "east")
stairway.link_caves(hole, "west")
stairway.link_caves(citadel, "east")
citadel.link_caves(stairway, "west")
citadel.link_caves(path, "east")
citadel.link_caves(dungeon, "south")
path.link_caves(citadel, "west")
path.link_caves(shrine, "east")
shrine.link_caves(path, "west")
shrine.link_caves(insides, "north")
insides.link_caves(shrine, "south")
highland.link_caves(mineshaft, "south")
highland.link_caves(city, "north")
city.link_caves(highland, "south")
city.link_caves(arena, "west")
city.link_caves(temple, "east")
temple.link_caves(city, "west")
arena.link_caves(city, "east")
swamp.link_caves(thicket, "east")

pendant_quantity = 0

current_cave = mineshaft
dead = False
while dead is False:
    print("\n")
    current_cave.get_details()
    inhabited = current_cave.character1
#    if current_cave.character1 is None:
#        current_cave.set_character2
    if inhabited is not None:
        inhabited.describe()
        if inhabited is not None and isinstance(inhabited, Enemy):
            print("You can fight this character")
        elif inhabited is not Enemy:
            print("You can talk to this character")
    print("\nYou have options for what to do")
    print(current_cave.get_character1) #try working here nxt
    command = input("> ").lower()
    if command in ["north", "south", "west", "east"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabited is not None:
            inhabited.talk()
    elif command == "fight":
        if inhabited is not None and isinstance(inhabited, Enemy):
            fight_with = input("What do you want to fight with?: ")
            if inhabited.fight(fight_with) is True:
                print("Bravo, you win the battle.")
                current_cave.set_character1(None)
                inhabited = current_cave.set_character2
            else:
                print("You have been defeated. GAME OVER")
                dead = True
            #Fights with the enemy
#End-of-file (EOF)
