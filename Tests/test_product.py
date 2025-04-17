import unittest
from src.product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product(product_id="101", name="Laptop", price=999.99, description="A high-performance laptop")
        self.assertEqual(product.product_id, "101")
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.description, "A high-performance laptop")

    def test_add_product(self):
        product = Product(product_id="101", name="Laptop", price=999.99, description="A high-performance laptop")
        product.addProduct("Smartphone", 599.99, "A mid-range smartphone")
        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.price, 599.99)

    def test_remove_product(self):
        product = Product(product_id="101", name="Laptop", price=999.99, description="A high-performance laptop")
        product.removeProduct()
        self.assertEqual(product.name, None)
        self.assertEqual(product.price, None)

if __name__ == '__main__':
    unittest.main()
