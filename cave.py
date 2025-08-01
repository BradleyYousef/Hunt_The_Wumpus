from inventory import Inventory #Imports the inventory class from the inventory.py file
"""Cave class for Hunt The Wumpus"""
class Cave:
    """Class for creating the caves"""
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character1 = None
        self.character2 = None
        self.unlocked = True
        self.entry_requirement = None

    def set_name(self, cave_name):
        """Sets the name of the cave"""
        self.name = cave_name

    def get_name(self):
        """Gets the name of the cave """
        return self.name

    def set_description(self, cave_description):
        """Sets the description of the cave"""
        self.description = cave_description

    def get_description(self):
        """Gets the description of the cave"""
        return self.description

    def describe(self):
        """Describes the current cave"""
        print(self.description)

    def link_caves(self, cave_to_link, direction):
        """Defines which caves are linked together and what direction"""
        self.linked_caves[direction] = cave_to_link
        #print(self.name + "linked caves" + repr(self.linked_caves))

    def get_details(self):
        """Gets the details of the cave the player is currently in"""
        print(self.name)
        print("----------")
        print(self.description)
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        """Allows the player to move between caves"""
        new_cave = self.linked_caves[direction]
        if direction in self.linked_caves and new_cave.unlocked == True:
            return self.linked_caves[direction]
        elif direction in self.linked_caves and new_cave.unlocked == False:
            print("This cave is locked")
        else:
            print("You can't go that way")
            return self

    def get_character1(self):
        """Gets the current character in the cave"""
        return self.character1

    def set_character1(self, new_character):
        """Sets the current character in the cave"""
        self.character1 = new_character

    def get_character2(self):
        """Gets the current character in the cave"""
        return self.character2

    def set_character2(self, new_character):
        """Sets the current character in the cave"""
        self.character2 = new_character
    
    def lock_cave(self, is_locked):
        """Allows the caves to have entry requirements"""
        self.unlocked = is_locked
    
    def set_entry_requirement(self, open_item):
        """Sets the item and quantity required to unlock the cave"""
        self.entry_requirement = open_item
        self.unlocked = False  # Lock the cave until requirement is met

    def open_cave(self, player_inventory):
        """
        Attempts to unlock the cave if the player has the required item and quantity.
        player_inventory: a dictionary or list of Inventory objects
        """
        if not self.entry_requirement:
            print("No entry requirement set for this cave.")
            return

        required_item_name = self.entry_requirement['item']
        required_quantity = self.entry_requirement['quantity']

        for item in player_inventory:
            if item.name == required_item_name and item.get_object_quantity() >= required_quantity:
                self.unlocked = True
                print(f"The cave '{self.name}' is now unlocked!")
                return

        print(f"You need at least {required_quantity} of '{required_item_name}")
            

#End-of-file (EOF)