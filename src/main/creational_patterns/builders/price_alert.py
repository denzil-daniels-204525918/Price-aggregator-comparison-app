class PriceAlert:
    def __init__(self, alert_id: str, threshold_price: float, is_active: bool):
        self.alert_id = alert_id
        self.threshold_price = threshold_price
        self.is_active = is_active

    def __repr__(self):
        return f"<PriceAlert(id={self.alert_id}, threshold={self.threshold_price}, active={self.is_active})>"
