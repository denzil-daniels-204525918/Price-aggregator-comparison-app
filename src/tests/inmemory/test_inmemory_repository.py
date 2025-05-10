# src/tests/inmemory/test_inmemory_repository.py

import unittest
from src.main.product import Product
from src.main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository

class TestInMemoryProductRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryProductRepository()
        self.product1 = Product(product_id="p1", name="Apple", price=10.0, retailer_id="r1")

    def test_save_and_find_by_id(self):
        self.repo.save(self.product1)
        self.assertEqual(self.repo.find_by_id("p1"), self.product1)

    def test_find_all(self):
        self.repo.save(self.product1)
        products = self.repo.find_all()
        self.assertEqual(len(products), 1)

    def test_delete(self):
        self.repo.save(self.product1)
        self.repo.delete("p1")
        self.assertIsNone(self.repo.find_by_id("p1"))
