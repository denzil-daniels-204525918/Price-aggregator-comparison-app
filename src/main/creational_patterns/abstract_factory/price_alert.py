class PriceAlert:
    def __init__(self, alert_id, threshold_price, is_active=True):
        self.alert_id = alert_id
        self.threshold_price = threshold_price
        self.is_active = is_active
