"""The main program for Hunt The Wumpus"""
from cave import Cave #Imports the cave class from the cave.py file
from character import Enemy #Imports the enemy class from the character.py file
from character import Character #Imports the character class from the character.py file
from character import Salesman #Imports the salesman class from the character.py file
from inventory import Inventory #Imports the inventory class from the inventory.py file
import random #Imports the ability to add randomness
import os #Imports the operating system

def clear_console():
    """Clear the console function that clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

"""Object creation"""
wump_coins = Inventory("coin", "wump coin")
wump_coins.set_obj_quantity("0")
wump_coins.set_obj_price("0")

pendant = Inventory("pendant", "test pendant")
pendant.set_obj_quantity("0")
pendant.set_obj_price("10")
pendant_price = int(pendant.get_object_price())

library_key = Inventory("library_key", "library_Key")
library_key.set_obj_quantity("0")
library_key.set_obj_price("30")
library_key_price = int(library_key.get_object_price())

wind_charm = Inventory("wind_charm", "highland wind charm")
wind_charm.set_obj_quantity("0")
wind_charm.set_obj_price("50")
wind_charm_price = int(wind_charm.get_object_price())

librarians_stick = Inventory("librarians_stick", "stick from the librarian")
librarians_stick.set_obj_quantity("0")
librarians_stick.set_obj_price("40")
librarians_stick_price = int(librarians_stick.get_object_price())

gladiators_boots = Inventory("gladiators_boots", "gladiator boots")
gladiators_boots.set_obj_quantity("0")
gladiators_boots.set_obj_price("20")
gladiators_boots_price = int(gladiators_boots.get_object_price())

ancient_charm = Inventory("ancient_charm", "ancient charms")
ancient_charm.set_obj_quantity("0")
ancient_charm.set_obj_price("60")
ancient_charm_price = int(ancient_charm.get_object_price())

dungeon_key = Inventory("dungeon_key", "dungeon key")
dungeon_key.set_obj_quantity("0")
dungeon_key.set_obj_price("30")
dungeon_key_price = int(dungeon_key.get_object_price())

player_inventory = [wump_coins, pendant, library_key, dungeon_key, ancient_charm, gladiators_boots, librarians_stick, wind_charm] #List for what objects the player can have


"""Cave creation"""
cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
dungeon.set_entry_requirement({'item': 'dungeon_key', 'quantity': 1})
dungeon.lock_cave(False)
mineshaft = Cave("Mineshaft Entrance")
mineshaft.set_description("The entrance into the ancient Wumpus caves")
fork = Cave("Fork In The Road")
fork.set_description("A fork in the caves pathway")
grand = Cave("Grand Marsh")
grand.set_description("A swampy wetland covered in moss")
library = Cave("Sunken Library")
library.set_description("A withered library trapped in the moss")
library.set_entry_requirement({'item': 'library_key', 'quantity': 1})
library.lock_cave(False)
thicket = Cave("Deadly Thicket")
thicket.set_description("A forest with many withered trees")
thicket.set_entry_requirement({'item': 'librarians_stick', 'quantity': 1})
thicket.lock_cave(False)
dump = Cave("Wet Dump")
dump.set_description("A wet pile of moss that appears to be smoking")
shopkeeper = Cave("Shopkeeper's Abode")
shopkeeper.set_description("A cabin hidden in the moss where the shopkeeper resides")
hole = Cave("Giant Hole")
hole.set_description("A giant hole that seems hard to get out of")
hole.set_entry_requirement({'item': 'gladiators_boots', 'quantity': 1})
hole.lock_cave(False)
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
insides.set_entry_requirement({'item': 'ancient_charm', 'quantity': 1})
insides.lock_cave(False)
highland = Cave("Highland Glades")
highland.set_description("A windswept grassland")
highland.set_entry_requirement({'item': 'wind_charm', 'quantity': 1})
highland.lock_cave(False)
city = Cave("Sky City")
city.set_description("A city in the clouds filled with the surviving people")
temple = Cave("Sky Temple")
temple.set_description("The temple to the last sky lord from ancient times")
arena = Cave("Sky Arena")
arena.set_description("The skyland's colossuem")
swamp = Cave("Gladiator's Swamp")
swamp.set_description("A swamp filled with moss and wumpus to fight")

"""Cave linking"""
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


"""Character creation"""
guide = Character("Guide", "A guide to begin your quest")
guide.set_conversation("Hello traveler be careful exploring the caves. Some caves require certain items to open and other caves have evils lurking within. I HIGHLY recommend only purchasing one of each item as multiple are NEVER neccessary. I've heard that guard dogs are weak to a bone. Try talking to as many people as you can")

shopkeep = Salesman("Shopman", "A salesman to help you on your journey")
shopkeep.set_conversation("Hello traveler I have some items to sell you for your Wump coins\nYou have: " + str(wump_coins) + " Wump coins to trade")
shopkeep.set_good(library_key)
shopkeep.set_price(library_key_price)
shopkeeper.set_character2(shopkeep)

guard_puppy = Enemy("Guard puppy", "A puppy wumpus that is holding the shopkeeper captive")
guard_puppy.set_health(10)
guard_puppy.set_weakness("bone")
shopkeeper.set_character1(guard_puppy)

librarian = Salesman("Librarian", "An old man who protects the library")
librarian.set_conversation("Traveler there are many mentions of an evil wumpus lurking in the sky. I've also heard that goblins are weak to a stick, you can buy mine if you want")
librarian.set_good(librarians_stick)
librarian.set_price(librarians_stick)
library.set_character1(librarian)

goblin = Enemy("Goblin", "A greedy goblin attacking a barbarian?")
goblin.set_health(10)
goblin.set_weakness("stick")
swamp.set_character1(goblin)

barbarian = Salesman("Barbarian", "A battle hardened warrior")
barbarian.set_conversation("Thank you for saving me. You can buy my boots to allow you to go down giant holes.")
barbarian.set_good(gladiators_boots)
barbarian.set_price(gladiators_boots_price)
swamp.set_character2(barbarian)

royal_guard = Salesman("Royal Guard", "A skeleton from a fallen army")
royal_guard.set_conversation("The temple is further this way but to enter the citadel you need a pendant you can buy from me")
royal_guard.set_good(pendant)
royal_guard.set_price(pendant)
stairway.set_character1(royal_guard)

stone_tablet = Salesman("Stone Tablet", "A stone tablet hung upon the walls of the ancient shrine")
stone_tablet.set_conversation("The insides of the ancient temple can only be accessed with an ancient charm. Bought from me of course")
stone_tablet.set_good(ancient_charm)
stone_tablet.set_price(ancient_charm_price)
shrine.set_character1(stone_tablet)

skeleton = Salesman("Skeleton", "A skeleton withered by the confines of the insides of the temple")
skeleton.set_conversation("You can buy a key from me that allows you to access the dungeon near the citadel.")
skeleton.set_good(dungeon_key)
skeleton.set_price(dungeon_key_price)
insides.set_character1(skeleton)

chained_prisoner = Salesman("Chained Prisoner", "A prisoner chained in the dungeon")
chained_prisoner.set_conversation("I have been locked in here since the wumpus overlords went into hiding. They are weak to a berserker. Take this wind charm to access the highland glades near the mineshaft entrance you came from")
chained_prisoner.set_good(wind_charm)
chained_prisoner.set_price(wind_charm)
dungeon.set_character1(chained_prisoner)

sky_citizen = Character("Sky Citizen", "A citizen of the sky land")
sky_citizen.set_conversation("The evil wumpus overlord is in the sky temple. Please save the world from his terror")
city.set_character1(sky_citizen)

overlord = Enemy("Wumpus Overlord", "The ancient evil wumpus overlord")
overlord.set_health(10)
overlord.set_weakness("berserker")
temple.set_character1(overlord)


"""Main gameplay loop"""
current_cave = mineshaft
dead = False
while dead is False:
    if temple.get_character1() is not None:
        wump_coins_quantity = int(wump_coins.get_object_quantity())
        library_key_quantity = int(library_key.get_object_quantity())
        librarians_stick_quantity = int(librarians_stick.get_object_quantity())
        gladiator_boots_quantity = int(gladiators_boots.get_object_quantity())
        pendant_quantity = int(pendant.get_object_quantity())
        ancient_charm_quantity = int(ancient_charm.get_object_quantity())
        dungeon_key_quantity = int(dungeon_key.get_object_quantity())
        wind_charm_quantity = int(wind_charm.get_object_quantity())
        print("\n")
        current_cave.get_details()
        inhabited = current_cave.character1
        print("\n---------")
        if wump_coins_quantity != 0:
            print("you have " + str(wump_coins.get_object_quantity()) + " Wump coins")
        if library_key_quantity != 0:
            print("you have " + str(library_key.get_object_quantity()) + " Library keys")
        if librarians_stick_quantity != 0:
            print("you have " + str(librarians_stick.get_object_quantity()) + " Librarians sticks")
        if gladiator_boots_quantity != 0:
            print("you have " + str(gladiators_boots.get_object_quantity()) + " Gladiator boots")
        if pendant_quantity != 0:
            print("you have " + str(pendant.get_object_quantity()) + " Pendants")
        if ancient_charm_quantity != 0:
            print("you have " + str(ancient_charm.get_object_quantity()) + " Ancient Charms")
        if dungeon_key_quantity != 0:
            print("you have " + str(dungeon_key.get_object_quantity()) + " Dungeon Keys")
        if wind_charm_quantity != 0:
            print("you have " + str(wind_charm.get_object_quantity()) + " Wind Charms")
        if inhabited is not None:
            inhabited.describe()
            if inhabited is not None and isinstance(inhabited, Enemy):
                print("You can fight this character")
                print("You can talk to this character")
            elif inhabited is not Enemy:
                print("You can talk to this character")
        print("\nWhat would you like to do?: ")
        command = input("> ").lower()
        if command in ["north", "south", "west", "east"]:
            can_move_cave = True
            newer_cave = current_cave.linked_caves.get(command)
            if newer_cave:
                newer_cave.open_cave(player_inventory)
                if newer_cave.unlocked:
                    current_cave = newer_cave
                else:
                    print("The cave is still locked.")
            else:
                print("You cannot move here yet")
                input("\nPress enter to continue...")
        elif command == "talk":
            if inhabited is not None:
                clear_console()
                inhabited.talk()
                input("\nPress enter to continue...")
        elif command == "fight": #Fights with the enemy
            if inhabited is not None and isinstance(inhabited, Enemy):
                fight_with = input("What do you want to fight with?: ")
                if inhabited.fight(fight_with) is True:
                    print("\nBravo, you win the battle.")
                    money_dropped = random.randint(60, 120)
                    wump_coins.change_quantity(-money_dropped)
                    print(f"You have obtained {money_dropped} wump coins from defeating {current_cave.character1}")
                    current_cave.character1 = current_cave.character2
                    current_cave.character2 = None
                    input("\nPress enter to continue...")
                    clear_console()
                else:
                    print("You have been defeated. GAME OVER")
                    dead = True
        elif command == "shop":
            if inhabited is not None and isinstance(inhabited, Salesman):
                clear_console()
                inhabited.get_shop_details()
                want_to_buy = input("Would you like to purchase the item?: ")
                if want_to_buy == "yes":
                    if inhabited.shop == (library_key):
                        if int(wump_coins.quantity) >= library_key_price:
                            library_key.change_quantity(-1)
                            wump_coins.change_quantity(30)
                            print("You have purchased the Library Key for 30 Wump Coins")
                            input("\nPress enter to continue...")
                        else:
                                print("You are too poor to buy the library key. Come back after you fight some enemies with their wump coins")
                                input("\nPress enter to continue...")
                    if inhabited.shop == (pendant):
                        if int(wump_coins.quantity) >= pendant_price:
                            pendant.change_quantity(-1)
                            wump_coins.change_quantity(10)
                            print("You have purchased a Pendant for 10 Wump Coins")
                            input("\nPress enter to continue...")
                        else:
                                print("You are too poor to buy a pendant. Come back after you fight some enemies with their wump coins")
                                input("\nPress enter to continue...")
                    if inhabited.shop == (librarians_stick):
                        if int(wump_coins.quantity) >= librarians_stick_price:
                            librarians_stick.change_quantity(-1)
                            wump_coins.change_quantity(40)
                            print("You have purchased a librarians stick for 40 Wump Coins")
                            input("\nPress enter to continue...")
                        else:
                                print("You are too poor to buy a librarians stick. Come back after you fight some enemies with their wump coins")
                                input("\nPress enter to continue...")
                    if inhabited.shop == (gladiators_boots):
                        if int(wump_coins.quantity) >= gladiators_boots_price:
                            gladiators_boots.change_quantity(-1)
                            wump_coins.change_quantity(20)
                            print("You have purchased gladiators bootsfor 20 Wump Coins")
                            input("\nPress enter to continue...")
                        else:
                                print("You are too poor to buy gladiators boots. Come back after you fight some enemies with their wump coins")
                                input("\nPress enter to continue...")
                    if inhabited.shop == (ancient_charm):
                        if int(wump_coins.quantity) >= ancient_charm_price:
                            ancient_charm.change_quantity(-1)
                            wump_coins.change_quantity(30)
                            print("You have purchased a ancient_charm for 60 Wump Coins")
                            input("\nPress enter to continue...")
                        else:
                                print("You are too poor to buy a ancient charm. Come back after you fight some enemies with their wump coins")
                                input("\nPress enter to continue...")
                    if inhabited.shop == (dungeon_key):
                        if int(wump_coins.quantity) >= dungeon_key_price:
                            dungeon_key.change_quantity(-1)
                            wump_coins.change_quantity(30)
                            print("You have purchased a dungeon_key for 30 Wump Coins")
                            input("\nPress enter to continue...")
                        else:
                                print("You are too poor to buy a dungeon key. Come back after you fight some enemies with their wump coins")
                                input("\nPress enter to continue...")
                    if inhabited.shop == (wind_charm):
                        if int(wump_coins.quantity) >= wind_charm_price:
                            wind_charm.change_quantity(-1)
                            wump_coins.change_quantity(50)
                            print("You have purchased a wind charm for 50 Wump Coins")
                            input("\nPress enter to continue...")
                        else:
                                print("You are too poor to buy a wind charm. Come back after you fight some enemies with their wump coins")
                                input("\nPress enter to continue...")
                if want_to_buy == "no":
                    print("Okay come again.")
                    input("\nPress enter to continue...")
        else:
            clear_console()
    else:
        print("You have saved the wumpus world. Thank you for playing")
        input("Press enter to exit the game...")
        exit()
#End-of-file (EOF)
