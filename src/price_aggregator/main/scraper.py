import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def fetch_food_lovers_prices():
    url = "https://foodloversmarket.co.za/weekly-specials/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all("div", class_="product-tile"):
        name = item.find("span", class_="product-name").text.strip()
        price_text = item.find("span", class_="price").text.strip()
        price = float(price_text.replace("R", "").replace(",", "."))
        products.append({"name": name, "price": price})
    return products

def fetch_checkers_prices():
    url = "https://www.checkers.co.za/cms/category/milk"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all("div", class_="product-tile"):
        name = item.find("span", class_="product-name").text.strip()
        price_text = item.find("span", class_="price").text.strip()
        price = float(price_text.replace("R", "").replace(",", "."))
        products.append({"name": name, "price": price})
    return products

def fetch_woolworths_prices():
    url = "https://www.woolworths.co.za/cat/Food/_/N-1z141p7"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    products = []
    for item in soup.find_all("div", class_="product-tile"):
        name = item.find("span", class_="product-name").text.strip()
        price_text = item.find("span", class_="price").text.strip()
        price = float(price_text.replace("R", "").replace(",", "."))
        products.append({"name": name, "price": price})
    return products
