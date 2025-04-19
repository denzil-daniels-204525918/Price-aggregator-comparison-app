import pytest
from main.creational_patterns.factory_method.data_source_factory import DataSourceFactory
from main.creational_patterns.factory_method.picknpay_data_source import PicknPayDataSource
from main.creational_patterns.factory_method.checkers_data_source import CheckersDataSource

def test_get_picknpay_data_source():
    factory = DataSourceFactory()
    source = factory.get_data_source("PicknPay")

    assert isinstance(source, PicknPayDataSource)
    assert source.fetch_data() == "Fetched data from Pick n Pay"

def test_get_checkers_data_source():
    factory = DataSourceFactory()
    source = factory.get_data_source("Checkers")

    assert isinstance(source, CheckersDataSource)
    assert source.fetch_data() == "Fetched data from Checkers"

def test_get_unknown_source():
    factory = DataSourceFactory()

    with pytest.raises(ValueError) as e:
        factory.get_data_source("Game")

    assert "Unknown data source type" in str(e.value)
