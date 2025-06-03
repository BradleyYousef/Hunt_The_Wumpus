"""Class for the characters in Hunt The Wumpus"""
class Character:
    """Class for creating characters"""
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Method to display the attributes of the character"""
        print(self.name + " is here!")
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
