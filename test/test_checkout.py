import json
from ..lib import (
    Checkout,
    TwoForOnePromotion
)

sample_items = {}
with open('fixtures/in_items.json') as json_file:
    sample_items = json.load(json_file)

database = {}
with open('../fixtures/database.json') as json_file:
    database = json.load(json_file)


def test_checkout_scan():
    checkout = Checkout(database)
    checkout.scan('VOUCHER')
    checkout.scan('TSHIRT')
    checkout.scan('VOUCHER')
    checkout.scan('VOUCHER')
    checkout.scan('MUG')

    expected_items = [
        {'code': 'VOUCHER', 'name': 'Cofi Voucher', 'price': 5.0}, 
        {'code': 'TSHIRT', 'name': 'Cofi T-shirt', 'price': 20.0}, 
        {'code': 'VOUCHER', 'name': 'Cofi Voucher', 'price': 5.0}, 
        {'code': 'VOUCHER', 'name': 'Cofi Voucher', 'price': 5.0}, 
        {'code': 'MUG', 'name': 'Cofi Coffee Mug ', 'price': 7.5}
    ]

    assert checkout.get_scanned_items() == expected_items


def test_checkout_total_promotion():
    promotion = TwoForOnePromotion('VOUCHER', 5.0)
    checkout = Checkout(database, promotion)
    checkout.scan('VOUCHER')
    checkout.scan('VOUCHER')
    checkout.scan('VOUCHER')
    checkout.scan('VOUCHER')
    checkout.scan('MUG')
    total = checkout.total()

    assert total == 17.5


def test_checkout_total_no_promotion():
    checkout = Checkout(database)
    checkout.scan('VOUCHER')
    checkout.scan('VOUCHER')
    checkout.scan('VOUCHER')
    checkout.scan('VOUCHER')
    checkout.scan('MUG')
    total = checkout.total()

    assert total == 27.5