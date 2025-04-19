import pytest
from src.main.creational_patterns.abstract_factory.retailer_a_factory import RetailerAFactory


from src.main.creational_patterns.abstract_factory.promotion import Promotion
from src.main.creational_patterns.abstract_factory.price_alert import PriceAlert

from src.main.creational_patterns.abstract_factory.product import Product




def test_create_product():
    factory = RetailerAFactory()
    product = factory.create_product("101", "Bread", 1.99, "Whole wheat bread")

    assert isinstance(product, Product)
    assert product.product_id == "A-101"
    assert product.name == "Bread"
    assert product.price == 1.99
    assert product.description == "Whole wheat bread"

def test_create_promotion():
    factory = RetailerAFactory()
    promo = factory.create_promotion("Spring Sale", 10)

    assert isinstance(promo, Promotion)
    assert promo.promo_id == "A-Spring Sale"
    assert promo.description == "Spring Sale"
    assert promo.discount == 10.0

def test_create_price_alert():
    factory = RetailerAFactory()
    alert = factory.create_price_alert("PA101", 1.50)

    assert isinstance(alert, PriceAlert)
    assert alert.alert_id == "A-PA101"
    assert alert.threshold_price == 1.50
    assert alert.is_active == True
