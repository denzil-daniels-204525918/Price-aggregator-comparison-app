import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.checkers_scraper import get_products as get_checkers_products
from scraper.picknpay_scraper import get_products as get_picknpay_products
from scraper.woolworths_scraper import get_products as get_woolworths_products
from scraper.checkers_scraper import get_products_by_category as get_checkers_by_category
from scraper.picknpay_scraper import get_products_by_category as get_picknpay_by_category
from scraper.woolworths_scraper import get_products_by_category as get_woolworths_by_category
from scraper.checkers_scraper import get_categories as get_checkers_categories

def merge_products(*stores):
    """Merge products from multiple stores into a single dictionary"""
    merged = {}
    for store_name, products in stores:
        for product_name, price in products.items():
            if product_name not in merged:
                merged[product_name] = {}
            merged[product_name][store_name] = price
    return merged

def display_comparison(merged_products):
    """Display price comparison and highlight cheapest store"""
    print("\n=== Price Comparison Across Stores ===\n")
    for product_name, store_prices in merged_products.items():
        cheapest_store = min(store_prices, key=store_prices.get)
        for store, price in store_prices.items():
            highlight = "✅" if store == cheapest_store else ""
            print(f"{store} → {product_name}: R{price:.2f} {highlight}")
        print("-" * 50)

def list_categories():
    """List all available categories"""
    categories = get_checkers_categories()  # Assuming all stores have same categories
    print("\n=== Available Categories ===")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    print(f"\nUsage: python src/main/run_scraper.py --category 'Bakery'")
    return categories

def search_by_category(category_name):
    """Search for products by category across all stores"""
    checkers_products = get_checkers_by_category(category_name)
    picknpay_products = get_picknpay_by_category(category_name)
    woolworths_products = get_woolworths_by_category(category_name)

    merged = merge_products(
        ("Checkers", checkers_products),
        ("Pick n Pay", picknpay_products),
        ("Woolworths", woolworths_products)
    )

    return merged

def main():
    # Handle command line arguments
    if len(sys.argv) == 1:
        # No arguments - show all products
        print("📦 Showing all products:")
        checkers_products = get_checkers_products("")
        picknpay_products = get_picknpay_products("")
        woolworths_products = get_woolworths_products("")

        merged = merge_products(
            ("Checkers", checkers_products),
            ("Pick n Pay", picknpay_products),
            ("Woolworths", woolworths_products)
        )

    elif len(sys.argv) == 2:
        # One argument - could be search term or category flag
        arg = sys.argv[1]

        if arg == "--categories" or arg == "-c":
            list_categories()
            return
        else:
            # Regular product search
            search_query = arg
            print(f"🔍 Searching for '{search_query}'...")

            checkers_products = get_checkers_products("")
            picknpay_products = get_picknpay_products("")
            woolworths_products = get_woolworths_products("")

            merged = merge_products(
                ("Checkers", checkers_products),
                ("Pick n Pay", picknpay_products),
                ("Woolworths", woolworths_products)
            )

            # Filter by search term
            search_query_lower = search_query.lower()
            filtered_products = {}
            for product_name, prices in merged.items():
                if search_query_lower in product_name.lower():
                    filtered_products[product_name] = prices

            merged = filtered_products

            if not merged:
                print(f"❌ No products found matching '{search_query}'")
                return

    elif len(sys.argv) == 3:
        # Two arguments - check if it's a category search
        if sys.argv[1] == "--category" or sys.argv[1] == "-cat":
            category_name = sys.argv[2]
            print(f"🛒 Showing products in category: '{category_name}'")
            merged = search_by_category(category_name)

            if not merged:
                print(f"❌ No products found in category '{category_name}'")
                print("\n💡 Available categories:")
                list_categories()
                return
        else:
            print("❌ Invalid arguments")
            print("\nUsage:")
            print("  python src/main/run_scraper.py                                 # Show all products")
            print("  python src/main/run_scraper.py 'bread'                         # Search for product")
            print("  python src/main/run_scraper.py --categories                    # List all categories")
            print("  python src/main/run_scraper.py --category 'Bakery'             # Show products by category")
            return
    else:
        print("❌ Too many arguments")
        return

    if not merged:
        print("❌ No products found")
        return

    print(f"\n📊 Found {len(merged)} product(s)")
    display_comparison(merged)

if __name__ == "__main__":
    main()