from .data_source import DataSource

class PicknPayDataSource(DataSource):
    def fetch_data(self):
        return "Fetched data from Pick n Pay"
