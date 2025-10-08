from .picknpay_data_source import PicknPayDataSource
from .checkers_data_source import CheckersDataSource

class DataSourceFactory:
    def get_data_source(self, retailer: str):
        if retailer.lower() == "picknpay":
            return PicknPayDataSource()
        elif retailer.lower() == "checkers":
            return CheckersDataSource()
        else:
            raise ValueError("Unknown data source type")
