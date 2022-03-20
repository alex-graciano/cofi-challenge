from abc import ABC, abstractmethod

class Promotion(ABC):
    """Base class that encapsulates a promotion behavior""" 

    def __init__(self, next_promotion):
        self.next_promotion = next_promotion
        self.total = 0

    @abstractmethod
    def check_promotion(items):
        """Abstract public method in which any concrete object should
        implement the behavior"""
        pass

    def _next_promotion(self, remaining_items):
        """Handler of the promotion pipeline"""
        next_total = 0
        if self.next_promotion is not None:
            next_total, remaining_items = self.next_promotion.check_promotion(remaining_items)
        
        return self.total + next_total, remaining_items


class BulkPromotion(Promotion):
    """The main idea of this implementation is to count in linear order the number
    of each target item and in case this count exceeds the bulk does not pass any
    of these items to the next promotion"""

    def __init__(self, item_promotion, new_item_price, bulk_amount, next_promotion = None):
        super().__init__(next_promotion=next_promotion)
        self.item_promotion = item_promotion
        self.new_item_price = new_item_price
        self.bulk_amount = bulk_amount

    def check_promotion(self, items):
        remaining_items = []
        promotion_items = []
        item_counter = 0
        for item in items:
            item_code = item["code"]
            if item_code == self.item_promotion:
                item_counter += 1
                if item_counter < self.bulk_amount:
                    promotion_items.append(item)
            else:
                remaining_items.append(item)

        if item_counter >= self.bulk_amount:
            self.total = item_counter * self.new_item_price
        else:
            remaining_items += promotion_items
        
        return super()._next_promotion(remaining_items)


class TwoForOnePromotion(Promotion):
    """The main idea of this implementation is to save one of a target item
    until a new one os found, in that case none of them are added to the
    remaining items, otherwise the saved should be added."""

    def __init__(self, item_promotion, item_price, next_promotion = None):
        super().__init__(next_promotion=next_promotion)
        self.item_promotion = item_promotion
        self.item_price = item_price

    def check_promotion(self, items):
        remaining_items = []
        item_found = None
        item_counter = 0
        for item in items:
            item_code = item['code']
            if item_code == self.item_promotion:
                if item_found is not None:
                    item_counter += 1
                    item_found = None
                else:
                    item_found = item
            else:
                remaining_items.append(item)

        if item_found is not None:
            remaining_items.append(item_found)

        self.total = item_counter * self.item_price

        return super()._next_promotion(remaining_items)


class SwagPromotion(Promotion):
    """In a first pass to the items we discard those that are
    not included in the swag and count the ocurrences of the swag items. 
    The minimum value is the number of swags to be added to the total.
    Then, we should complete the list of leftovers with those not
    included in that minimum value"""

    swag_count = {}

    def __init__(self, swag_items, price, next_promotion = None):
        super().__init__(next_promotion=next_promotion)
        self.swag_items = swag_items
        self.swag_price = price
        for item in self.swag_items:
            self.swag_count[item] = 0


    def check_promotion(self, items):
        remaining_items = []

        for item in items:
            item_code = item['code']
            if item_code in self.swag_items:
                self.swag_count[item_code] += 1
            else:
                remaining_items.append(item)

        min_repetition = min(self.swag_count, key=self.swag_count.get)
        n_swags = self.swag_count[min_repetition]

        if n_swags > 0:
            self.total = n_swags * self.swag_price
            for item in items:
                item_code = item['code']
                if self.swag_count[item_code] - n_swags > 0:
                    remaining_items.append(item)
                    self.swag_count[item_code] -= 1
        else:
            remaining_items = items

        return super()._next_promotion(remaining_items)
        

#prom = SwagPromotion(['VOUCHER', 'MUG', 'TSHIRT'], 25.0)
#prom = TwoForOnePromotion('VOUCHER', 5.0)
#prom = BulkPromotion('TSHIRT', 4.0, 3)
items = [
    {
        "code": "VOUCHER",
        "name": "Cofi Voucher",
        "price": 5.0
    },
    {
        "code": "TSHIRT",
        "name": "Cofi Voucher",
        "price": 5.0
    },
    {
        "code": "TSHIRT",
        "name": "Cofi Voucher",
        "price": 5.0
    },
    {
        "code": "TSHIRT",
        "name": "Cofi Voucher",
        "price": 5.0
    },
    {
        "code": "TSHIRT",
        "name": "Cofi Voucher",
        "price": 5.0
    },
    {
        "code": "MUG",
        "name": "Cofi Voucher",
        "price": 5.0
    },
    {
        "code": "VOUCHER",
        "name": "Cofi Voucher",
        "price": 5.0
    },
    {
        "code": "VOUCHER",
        "name": "Cofi Voucher",
        "price": 5.0
    }
]
#total, remaining = prom.check_promotion(items)
#print(total)
#print(remaining)
