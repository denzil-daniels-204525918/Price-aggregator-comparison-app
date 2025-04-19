from .data_source import DataSource

class CheckersDataSource(DataSource):
    def fetch_data(self):
        return "Fetched data from Checkers"
