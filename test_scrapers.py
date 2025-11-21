# Create test_scrapers.py in the root directory (Price-aggregator-comparison-app/)
cat > test_scrapers.py << 'EOF'
import sys
import os

# Add the src directory to the path so we can import the scrapers
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scraper.checkers_scraper import get_products as get_checkers_products
from scraper.picknpay_scraper import get_products as get_picknpay_products
from scraper.woolworths_scraper import get_products as get_woolworths_products

# Test Checkers
print("=== Checkers Products ===")
checkers_products = get_checkers_products("")
print(f"Checkers found {len(checkers_products)} products")
for name, price in list(checkers_products.items())[:3]:  # Show first 3
    print(f"  {name}: R{price}")

print("\n=== Pick n Pay Products ===")
picknpay_products = get_picknpay_products("")
print(f"Pick n Pay found {len(picknpay_products)} products")
for name, price in list(picknpay_products.items())[:3]:  # Show first 3
    print(f"  {name}: R{price}")

print("\n=== Woolworths Products ===")
woolworths_products = get_woolworths_products("")
print(f"Woolworths found {len(woolworths_products)} products")
for name, price in list(woolworths_products.items())[:3]:  # Show first 3
    print(f"  {name}: R{price}")

# Test specific searches
print("\n=== Testing Search for 'Coca-Cola' ===")
coca_cola_checkers = get_checkers_products("Coca-Cola")
print(f"Checkers 'Coca-Cola' results: {len(coca_cola_checkers)}")
for name, price in coca_cola_checkers.items():
    print(f"  {name}: R{price}")
EOF