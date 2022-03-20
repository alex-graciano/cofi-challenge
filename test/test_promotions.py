import json
from ..lib import (
    TwoForOnePromotion,
    BulkPromotion,
    SwagPromotion
)

sample_items = {}
with open('fixtures/in_items.json') as json_file:
    sample_items = json.load(json_file)


def test_two_for_one_promotion():
    promotion = TwoForOnePromotion('VOUCHER', 5.0)
    total, remaining = promotion.check_promotion(sample_items)
    expected_reamining = [
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
        }
    ]

    assert total == 5.0
    assert remaining == expected_reamining


def test_bulk_promotion():
    promotion = BulkPromotion('TSHIRT', 4.0, 3)
    total, remaining = promotion.check_promotion(sample_items)
    expected_reamining = [
        {
            "code": "VOUCHER",
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

    assert total == 16.0
    assert remaining == expected_reamining


def test_swag_promotion():
    promotion = SwagPromotion(['VOUCHER', 'MUG', 'TSHIRT'], 25.0)
    total, remaining = promotion.check_promotion(sample_items)
    expected_reamining = [
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
            "code": "VOUCHER",
            "name": "Cofi Voucher",
            "price": 5.0
        }       
    ]

    assert total == 25.0
    assert remaining == expected_reamining


def test_promotion_pipleine():
    prom_3 = BulkPromotion('TSHIRT', 4.0, 3)
    prom_2 = TwoForOnePromotion('VOUCHER', 5.0, prom_3)
    prom_1 = SwagPromotion(['VOUCHER', 'MUG', 'TSHIRT'], 25.0, prom_2)
    total, remaining = prom_1.check_promotion(sample_items)
    expected_reamining = []
    
    assert total == 42.0
    assert remaining == expected_reamining