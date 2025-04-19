import unittest
from src.main.saved_list import SavedList
from src.main.product import Product

class TestSavedList(unittest.TestCase):
    def test_saved_list_creation(self):
        saved_list = SavedList(list_id="L101", user_id="U101")
        self.assertEqual(saved_list.list_id, "L101")
        self.assertEqual(saved_list.user_id, "U101")

    def test_add_product_to_list(self):
        saved_list = SavedList(list_id="L101", user_id="U101")
        product = Product(product_id="P101", name="Product A", price=100.00, description="Description of Product A")
        saved_list.add_product_to_list(product)
        self.assertIn(product, saved_list.products)

    def test_remove_product_from_list(self):
        saved_list = SavedList(list_id="L101", user_id="U101")
        product = Product(product_id="P101", name="Product A", price=100.00, description="Description of Product A")
        saved_list.add_product_to_list(product)
        saved_list.remove_product_from_list(product)
        self.assertNotIn(product, saved_list.products)

if __name__ == '__main__':
    unittest.main()
