# src/tests/creational_pattern/test_builder.py
from src.main.creational_patterns.builder import ProductReportBuilder
from src.main.product import Product
from src.main.promotion import Promotion

def test_build_product_report():
    builder = ProductReportBuilder()
    product = Product(
        product_id="201",
        name="Rice",
        price=4.99,
        description="5kg white rice"
    )
    promo = Promotion(
        promotion_id="Promo202",
        title="Spring Sale",
        description="10% off seasonal items",
        discount_percentage=10.0,
        duration_days=12
    )

    report = (
        builder
        .add_product(product.dict())
        .set_summary("total_products", 1)
        .set_summary("promotion", promo.title)
        .build()
    )

    assert report["summary"]["total_products"] == 1
    assert report["summary"]["promotion"] == "Spring Sale"
    assert report["products"][0]["name"] == "Rice"
