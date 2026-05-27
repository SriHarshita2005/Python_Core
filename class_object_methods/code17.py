#  Build an Inventory class that:
# Tracks the total number of items across all inventories.
# Each instance maintains its own stock dictionary ({"item": quantity}).
# Provides a method to add or remove stock.
# Allows updating a minimum stock threshold globally.
# Offers a static checker to verify if a stock level is below threshold.
# Demonstrate:
# 1.Managing multiple inventories.
# 2.Adjusting stock threshold.
# 3.Using static validation inside the instance logic.


class Inventroy:
    total_items = 0
    threshold = 25
    def __init__(self):
        self.items = {}
    def add(self,item,quantity):
        self.items[item] = quantity
        Inventroy.total_items+=1
    def remove(self,item):
        if item in self.items.keys():
            self.items.pop(item)
            print("removed successfully")
            Inventroy.total_items-=1
        else:
            pass

    @staticmethod
    def valid(q):
        return q>=Inventroy.threshold
