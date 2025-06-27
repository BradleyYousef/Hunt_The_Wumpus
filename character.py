"""Class for the characters in Hunt The Wumpus"""
class Character:
    """Class for creating characters"""
    def __init__(self, char_name, char_description):
        """Constructs the character"""
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.health = None

    def describe(self):
        """Method to display the attributes of the character"""
        print("\n" + self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Method to set what the character can say"""
        self.conversation = str(conversation)

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
    
    def set_health(self, health_points):
        """Sets the characters health points"""
        self.health = health_points

    def death(self):
        """Kills the character after their health is too low"""
        if self.health <= 0:
            return True

class Salesman(Character):
    """Creates the characters that interact with the player to give or buy items"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.shop = None
        self.good_price = 0

    def set_good(self, sold_good):
        """Sets the good that a specific npc will sell"""
        self.shop = sold_good
    
    def get_good(self):
        """Returns the good that an npc is selling"""
        return self.shop
    
    def set_price(self, good_value):
        """Sets the value of a specific salesman's good"""
        self.good_price = good_value
    
    def get_price(self):
        """Gets the price that a salesman sells things for"""
        return self.good_price
    
    def get_shop_details(self):
        """Prints the shop for an npc"""
        print("Testing shop\nItem being sold")
        print("\n--------")
        print(str(self.get_good()) + " is being sold for " + str(self.get_price()) + " wump coins")
    
    def good_sold(self):
        """Used to define what variable the sold good impacts"""
        


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
            self.health - 10
            print("You fend off " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " swallows you whole! You died.")
            return False
    
#    def set_drop(self, loot_item):
#        """Sets the loot item for an enemy"""
#        self.drop == loot_item

#    def loot(self):
  #      """Gives the loot item to the player"""
  #      if isinstance.__closure__  

#class Ally(Character):
 #   """Class for ally characters"""
  ##     super().__init__(char_name, char_description)
