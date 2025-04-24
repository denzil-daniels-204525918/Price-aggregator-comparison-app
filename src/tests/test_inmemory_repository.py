import unittest
from src.main.product import Product
from src.main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository

class TestInMemoryProductRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryProductRepository()
        self.product1 = Product(product_id="1", name="Apple", price=1.5)
        self.product2 = Product(product_id="2", name="Banana", price=0.8)

    def test_save_and_find_by_id(self):
        self.repo.save(self.product1)
        self.assertEqual(self.repo.find_by_id("1"), self.product1)

    def test_find_all(self):
        self.repo.save(self.product1)
        self.repo.save(self.product2)
        self.assertEqual(self.repo.find_all(), [self.product1, self.product2])

    def test_delete(self):
        self.repo.save(self.product1)
        self.repo.delete("1")
        self.assertIsNone(self.repo.find_by_id("1"))

    def test_find_by_id(self):
        self.repo.save(self.product1)
        self.assertEqual(self.repo.find_by_id("p1"), self.product1)
        self.assertIsNone(self.repo.find_by_id("Orange"))

if __name__ == "__main__":
    unittest.main()
