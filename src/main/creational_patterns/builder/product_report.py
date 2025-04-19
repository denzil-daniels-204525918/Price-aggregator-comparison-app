class ProductReport:
    def __init__(self, product, price_history, promotion, alert):
        self.product = product
        self.price_history = price_history
        self.promotion = promotion
        self.price_alert = alert  # Add this line to store the alert

    def __repr__(self):
        return f"ProductReport(product={self.product}, price_history={self.price_history}, promotion={self.promotion}, price_alert={self.price_alert})"
