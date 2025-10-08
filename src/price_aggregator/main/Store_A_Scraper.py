import requests
from bs4 import BeautifulSoup

def fetch_store_a_prices():
    url = 'https://www.woolworths.co.za/cat/New/Food/_/N-1z13sk5?No=0&inv=0'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all('div', class_='product'):
        name = item.find('h2').text.strip()
        price = float(item.find('span', class_='price').text.strip().replace('$', ''))
        products.append({'name': name, 'price': price})

    return products
