from src.scraper import checkers_scraper, picknpay_scraper, woolworths_scraper

search = "Clover Tropika Orange 2L"

prices = {
    "Checkers": checkers_scraper.get_products(search),
    "Pick n Pay": picknpay_scraper.get_products(search),
    "Woolworths": woolworths_scraper.get_products(search)
}

for store, products in prices.items():
    for name, price in products.items():
        print(f"{store} → {name}: R{price}")
