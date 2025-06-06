"""Cave class for Hunt The Wumpus"""
class Cave:
    """Class for creating the caves"""
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

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
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self

    def get_character(self):
        """Gets the current character in the cave"""
        return self.character

    def set_character(self, new_character):
        """Sets the current character in the cave"""
        self.character = new_character

#End-of-file (EOF)
