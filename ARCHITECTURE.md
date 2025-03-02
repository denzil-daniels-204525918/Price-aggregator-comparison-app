```mermaid
graph TD;
    User["🛒 Shopper\n(End User)"] -->|Uses| System["Grocery Price Comparison Platform"]
    System -->|Fetches Prices From| StoreAPIs["🏪 Store APIs"]
    System -->|Scrapes Data From| WebScraper["🌐 Web Scraper"]
    System -->|Displays Prices & Promotions| User
