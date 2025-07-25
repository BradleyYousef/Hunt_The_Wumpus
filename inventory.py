class Inventory:
    def __init__(self, obj_name_init):
        self.name = obj_name_init
        self.quantity = 0
        self.price = 0

        def set_obj_quantity(self, obj_amount):
            """Creates an objects amount"""
            self.quantity = obj_amount

        def set_obj_price(self, obj_price):
            """Creates an objects price"""
            self.price = obj_price
        
        def get_object_quantity(self):
            """Returns the objects quantity"""
            return self.quantity
        
        def get_object_price(self):
            """Returns the objects price"""
            return self.price