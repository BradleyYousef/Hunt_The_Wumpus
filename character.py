"""Class for the characters in Hunt The Wumpus"""
class Character:
    """Class for creating characters"""
    def __init__(self, char_name, char_description):
        """Constructs the character"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Method to display the attributes of the character"""
        print("\n" + self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Method to set what the character can say"""
        self.conversation = conversation

    def talk(self):
        """Method to allow the character to talk"""
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you.")

    def fight(self):
        """Method for fighting characters"""
        print(self.name + " doesn't want to fight you")
        return True

class Enemy(Character):
    """Used for making the baddies in Hunt The Wumpus"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        """Sets the weakness for the enemy"""
        self.weakness = item_weakness

    def get_weakness(self):
        """Gets the weakness for the enemy"""
        return self.weakness

    def fight(self, combat_item):
        """Method to fight the Wumpus's"""
        if combat_item == self.weakness:
            print("You fend off " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " swallows you whole! You died.")
            return False
