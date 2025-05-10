class Promotion:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount
        self.promo_id = f"A-{name}"
        self.description = name
