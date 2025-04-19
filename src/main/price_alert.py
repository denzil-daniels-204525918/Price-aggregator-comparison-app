# src/main/price_alert.py

class PriceAlert:
    def __init__(self, alert_id, price_threshold, is_active=True):
        self.alert_id = alert_id
        self.price_threshold = price_threshold
        self.is_active = is_active

    def subscribe(self):
        self.is_active = True

    def unsubscribe(self):
        self.is_active = False

    def __str__(self):
        return f"Price Alert ID: {self.alert_id}, Threshold: {self.price_threshold}, Active: {self.is_active}"


