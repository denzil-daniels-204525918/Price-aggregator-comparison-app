# src/price_alert.py

class PriceAlert:
    def __init__(self, alert_id: str, price_threshold: float, is_active: bool):
        self.alert_id = alert_id
        self.price_threshold = price_threshold
        self.is_active = is_active

    def subscribe(self):
        # Logic to subscribe to a price alert (simplified for demonstration)
        if self.is_active:
            print(f"Subscribed to price alert: {self.alert_id} for {self.price_threshold}")
        else:
            print(f"Price alert {self.alert_id} is not active.")

    def unsubscribe(self):
        # Logic to unsubscribe from a price alert (simplified for demonstration)
        print(f"Unsubscribed from price alert: {self.alert_id}")
