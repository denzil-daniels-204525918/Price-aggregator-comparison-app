# compare_prices.py
import pandas as pd
from .scraper import fetch_store_a_prices, fetch_store_b_prices  # relative import

def compare_prices():
    store_a_prices = fetch_store_a_prices()
    store_b_prices = fetch_store_b_prices()

    df_a = pd.DataFrame(store_a_prices)
    df_b = pd.DataFrame(store_b_prices)

    df = pd.merge(df_a, df_b, on='name', suffixes=('_store_a', '_store_b'))

    df['best_price'] = df[['price_store_a', 'price_store_b']].min(axis=1)
    df['cheapest_store'] = df.apply(lambda row: 'Store A' if row['price_store_a'] == row['best_price'] else 'Store B', axis=1)

    return df[['name', 'price_store_a', 'price_store_b', 'best_price', 'cheapest_store']]

# Only print if run as main module
if __name__ == "__main__":
    print(compare_prices())
