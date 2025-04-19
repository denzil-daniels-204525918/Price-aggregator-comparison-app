import pytest
from main.creational_patterns.builder.product_report_builder import ProductReportBuilder
from src.main.product import Product
from src.main.promotion import Promotion
from src.main.creational_patterns.builder.price_alert import PriceAlert
from main.creational_patterns.builder.product_report import ProductReport

def test_build_product_report():
    builder = ProductReportBuilder()

    product = Product(product_id="201", name="Rice", price=4.99, description="5kg white rice")
    price_history = [5.49, 5.29, 4.99]
    promo = Promotion("Spring Sale", 10.0, 12)

    alert = PriceAlert(alert_id="PA101", threshold_price=4.50, is_active=True)


    report = builder.set_product(product) \
        .add_price_history(price_history)\
        .set_promotion(promo) \
        .add_price_alert(alert)\
        .build()

    assert isinstance(report, ProductReport)
    assert report.product == product
    assert report.price_history == price_history
    assert report.promotion == promo
    assert report.price_alert == alert

def test_invalid_price_history():
    builder = ProductReportBuilder()

    product = Product(product_id="202", name="Wheat", price=3.50, description="1kg wheat")
    price_history = []
    promo = Promotion("Winter Sale", 15.0, 15)

    alert = PriceAlert(alert_id="PA102", threshold_price=3.00, is_active=True)


    with pytest.raises(ValueError):
        builder.set_product(product) \
            .add_price_history(price_history)\
            .set_promotion(promo) \
            .add_price_alert(alert)\
            .build()
