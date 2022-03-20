from .promotion import Promotion

class Checkout:
    """Checkout encapsulation. This represents a client order checkout""" 

    def __init__(self, database, promotion = None):
        self.items = []
        self.promotion = promotion
        self.database = database

    def scan(self, item):
        """This method adds any item to a list of items to be checkd out afterwards"""

        self.items.append(self.database[item])

    def total(self):
        """This method compute the actual total taking into accout the possible
        promotions to be applied"""

        total = 0
        if self.promotion is not None:
            total, self.items = self.promotion.check_promotion(self.items)

        for item in self.items:
            total += item['price']

        return total

    def get_scanned_items(self):
        return self.items
