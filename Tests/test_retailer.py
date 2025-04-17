import unittest
from src.retailer import Retailer
from src.product import Product

class TestRetailer(unittest.TestCase):
    def test_retailer_creation(self):
        retailer = Retailer(retailer_id="R101", name="Retailer A", contact_info="contact@retailera.com")
        self.assertEqual(retailer.retailer_id, "R101")
        self.assertEqual(retailer.name, "Retailer A")
        self.assertEqual(retailer.contact_info, "contact@retailera.com")

    def test_add_product(self):
        retailer = Retailer(retailer_id="R101", name="Retailer A", contact_info="contact@retailera.com")
        product = Product(product_id="P101", name="Product A", price=100.00, description="Description of Product A")
        retailer.add_product(product)
        self.assertIn(product, retailer.products)

    def test_remove_product(self):
        retailer = Retailer(retailer_id="R101", name="Retailer A", contact_info="contact@retailera.com")
        product = Product(product_id="P101", name="Product A", price=100.00, description="Description of Product A")
        retailer.add_product(product)
        retailer.remove_product(product)
        self.assertNotIn(product, retailer.products)

if __name__ == '__main__':
    unittest.main()
