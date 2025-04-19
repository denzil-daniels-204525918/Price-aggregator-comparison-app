import unittest
from src.main.price_alert import PriceAlert

class TestPriceAlert(unittest.TestCase):
    def test_price_alert_creation(self):
        price_alert = PriceAlert(alert_id="PA101", price_threshold=500.00, is_active=True)
        self.assertEqual(price_alert.alert_id, "PA101")
        self.assertEqual(price_alert.price_threshold, 500.00)
        self.assertEqual(price_alert.is_active, True)

    def test_subscribe(self):
        price_alert = PriceAlert(alert_id="PA101", price_threshold=500.00, is_active=False)
        price_alert.subscribe()
        self.assertEqual(price_alert.is_active, True)

    def test_unsubscribe(self):
        price_alert = PriceAlert(alert_id="PA101", price_threshold=500.00, is_active=True)
        price_alert.unsubscribe()
        self.assertEqual(price_alert.is_active, False)

if __name__ == '__main__':
    unittest.main()
