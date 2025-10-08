class ProductReportBuilder:
    def __init__(self):
        self.report = {
            'products': [],
            'summary': {}
        }

    def add_product(self, product):
        self.report['products'].append(product)
        return self

    def set_summary(self, key, value):
        self.report['summary'][key] = value
        return self

    def build(self):
        return self.report