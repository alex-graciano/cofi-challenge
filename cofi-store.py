import json
from lib.checkout import Checkout
from lib.promotion import (
    TwoForOnePromotion, 
    BulkPromotion,
    SwagPromotion
)

def set_promotion_pipeline(database):
    prom_3 = BulkPromotion('TSHIRT', 19.0, 3)
    prom_2 = TwoForOnePromotion('VOUCHER', database['VOUCHER']['price'], prom_3)
    prom_1 = SwagPromotion(['VOUCHER', 'MUG', 'TSHIRT'], 25.0, prom_2)
    return Checkout(database, prom_1)    

database = {}
with open('./fixtures/database.json') as json_file:
    database= json.load(json_file)

checkout = set_promotion_pipeline(database)
checkout.scan('VOUCHER')
checkout.scan('TSHIRT')
checkout.scan('VOUCHER')
checkout.scan('VOUCHER')
checkout.scan('MUG')
total = checkout.total()

print('total: ' + str(total))