# simple_factory

from main.creational_patterns.simple_factory.product_factory import ProductFactory

def main():
    # Create an instance of ProductFactory
    factory = ProductFactory()

    # Create products for different product types
    product1 = factory.create_product("101", "Milk", 3.50, "1L of full cream milk", product_type="grocery")
    product2 = factory.create_product("102", "Eggs", 2.99, "Dozen large eggs", product_type="grocery")

    # Print out the created products
    print(product1)
    print(product2)

if __name__ == "__main__":
    main()

#factory_method
from main.creational_patterns.factory_method.data_source_factory import DataSourceFactory

def main():
    factory = DataSourceFactory()

    # Use factory to delegate instantiation
    picknpay_source = factory.get_data_source("PicknPay")
    checkers_source = factory.get_data_source("Checkers")

    print(picknpay_source.fetch_data())
    print(checkers_source.fetch_data())

if __name__ == "__main__":
    main()

# abstract_factory
from main.creational_patterns.abstract_factory.retailer_a_factory import RetailerAFactory

def main():
    factory = RetailerAFactory()

    product = factory.create_product("101", "Bread", 1.99, "Whole wheat bread")
    promo = factory.create_promotion("P101", "Spring Sale", 10)
    alert = factory.create_price_alert("PA101", 1.50)

    print(product)
    print(promo)
    print(alert)

if __name__ == "__main__":
    main()

from main.creational_patterns.builders.product_report_builder import ProductReportBuilder
from main.product import Product
from main.promotion import Promotion
from src.main.price_alert import PriceAlert

def main():
    builder = ProductReportBuilder()

    product = Product("201", "Rice", 4.99, "5kg white rice")
    promotion = Promotion("P202", "Spring Special", 15.0)
    alert = PriceAlert("A1001", 4.50)

    report = (
        builder
        .set_product(product)
        .add_price_history([5.49, 5.29, 4.99])
        .set_promotion(promotion)
        .set_alert(alert)
        .build()
    )

    print(report)

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    factory = RepositoryFactory(storage_type="inmemory")
    service = PromotionService(factory)

    promo = Promotion(promotion_id="promo1", title="Easter Sale", description="20% off!", discount_percentage=20)
    service.create_promotion(promo)

    print(service.get_all_promotions())
