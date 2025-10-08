def test_basic():
    assert 1 + 1 == 2

def test_imports():
    try:
        from price_aggregator.main.user import User
        from price_aggregator.main.product import Product
        assert True
    except ImportError:
        assert False, "Import failed"
