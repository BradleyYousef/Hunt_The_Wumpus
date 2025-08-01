"""Some templates for creating objects, characters and caves"""


"""Shopkeeper template"""
test_shopkeep = Salesman("Test Shop", "A tester shopkeeper")
test_shopkeep.set_conversation("Hiya wanna buy smth gangster")
test_shopkeep.set_good(pendant)
test_shopkeep.set_price(pendant_price)
cavern.set_character1(test_shopkeep)


"""Character template"""
harry = Enemy("Harry", "A dirty, smelly Wumpus")
harry.set_conversation("At this fork in the road there is a giant hole to steep to go down normally and a large grotto that I will eat you in.")
harry.set_weakness("vegemite")
harry.set_health(10)
fork.set_character1(harry)


"""Item template"""
pendant = Inventory("pendant", "test pendant")
pendant.set_obj_quantity("0")
pendant.set_obj_price("30")
pendant_price = int(pendant.get_object_price())



"""Cave template"""
hole = Cave("Giant Hole")
hole.set_description("A giant hole that seems hard to get out of")
hole.set_entry_requirement({'item': 'pendant', 'quantity': 1})
hole.lock_cave(False)

hole.link_caves(fork, "west")
hole.link_caves(stairway, "east")


"""Old code might reuse"""
test_shopkeep = Salesman("Test Shop", "A tester shopkeeper")
test_shopkeep.set_conversation("Hiya wanna buy smth gangster")
test_shopkeep.set_good(pendant)
test_shopkeep.set_price(pendant_price)
cavern.set_character1(test_shopkeep)



larry = Enemy("Larry", "An asian Wumpus")
larry.set_conversation("You killed harry. I am Larry and I'm gonna eat your dog")
larry.set_weakness("engrish")
larry.set_health(10)
fork.set_character2(larry)


harry = Enemy("Harry", "A dirty, smelly Wumpus")
harry.set_conversation("At this fork in the road there is a giant hole to steep to go down normally and a large grotto that I will eat you in.")
harry.set_weakness("vegemite")
harry.set_health(10)
fork.set_character1(harry)