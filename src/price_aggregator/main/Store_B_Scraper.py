import requests
from bs4 import BeautifulSoup

def fetch_store_b_prices():
    url = 'https://www.checkers.co.za/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all('div', class_='product-item'):
        name = item.find('h3').text.strip()
        price = float(item.find('span', class_='product-price').text.strip().replace('$', ''))
        products.append({'name': name, 'price': price})

    return products
