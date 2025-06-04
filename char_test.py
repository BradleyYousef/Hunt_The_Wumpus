"""Testing the character"""
from character import Enemy

harry = Enemy("Harry", "A dirty, smelly Wumpus")
harry.describe()
harry.set_conversation("Come closer. I cannot see you.")
harry.talk()
print(harry)
harry.set_weakness("vegemite")

fight_with = input("What do you want to fight with? ")
harry.fight(fight_with)
