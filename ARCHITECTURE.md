# Grocery Price Comparison - C4 Context Diagram (Level 1)

* **Context (Level 1)** – High-level system overview and interactions with users/external systems.
* **Container (Level 2)** – Breakdown of the system into main components such as web apps, databases, and APIs.
* **Component (Level 3)** – Internal structure of each container, showing major modules and their interactions.
* **Code (Level 4)** – Low-level details (typically class diagrams, not always needed).

```mermaid
graph TD;
    User["🛒 Shopper\n(End User)"] -->|Uses| System["Grocery Price Comparison Platform"]
    System -->|Fetches Prices From| StoreAPIs["🏪 Store APIs"]
    System -->|Scrapes Data From| WebScraper["🌐 Web Scraper"]
    System -->|Displays Prices & Promotions| User
