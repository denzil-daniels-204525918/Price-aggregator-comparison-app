```mermaid
classDiagram
    class User {
        +String userId
        +String name
        +String email
        +String password
        +login()
        +logout()
    }

    class Product {
        +String productId
        +String name
        +double price
        +String description
        +addProduct()
        +removeProduct()
    }

    class PriceAlert {
        +String alertId
        +double priceThreshold
        +Boolean isActive
        +subscribe()
        +unsubscribe()
    }

    class Retailer {
        +String retailerId
        +String name
        +String contactInfo
        +addProduct()
        +removeProduct()
    }

    class SavedList {
        +String listId
        +String userId
        +addProductToList()
        +removeProductFromList()
    }

    User "1" -- "0..*" PriceAlert : subscribes
    User "1" -- "0..*" SavedList : saves
    Retailer "1" -- "0..*" Product : lists
    User "1" -- "0..*" Product : views

    class Promotion {
        +String promotionId
        +String description
        +double discount
        +applyPromotion()
    }

    Product "1" -- "0..*" Promotion : has
    SavedList "1" -- "0..*" Product : contains
```
/*
Explanation of the Class Diagram

Classes:
- User: Represents a user of the system. Attributes include user ID, name, email, and password, with methods for logging
in and logging out.
- Product: Represents a product listed by a retailer. Attributes include product ID, name, price, and description.
Methods include adding or removing products.
- PriceAlert: Represents a price alert set by a user for a specific product. Attributes include alert ID, price threshold,
and whether the alert is active.
- Retailer: Represents a retailer who lists products. Attributes include retailer ID, name, and contact information.
Methods include adding and removing products.
- SavedList: Represents a list where a user can save products for future reference. Attributes include list ID and user
ID, with methods for adding/removing products.
- Promotion: Represents a promotional offer for a product. Includes attributes for promotion ID, description, and discount,
with methods to apply promotions.

Relationships:
- User to PriceAlert: A user can subscribe to multiple price alerts, but each alert is associated with one user (1 -- 0..*).
- User to SavedList: A user can save multiple products in a saved list (1 -- 0..*).
- Retailer to Product: A retailer can list multiple products, but each product is associated with only one retailer (1 -- 0..*).
- User to Product: A user can view multiple products, and products can be viewed by many users (1 -- 0..*).
- Product to Promotion: A product can have multiple promotions applied, and each promotion can apply to multiple products (1 -- 0..*).
- SavedList to Product: A saved list can contain multiple products, and each product can appear in multiple lists (1 -- 0..*).

Key Design Decisions:
- Separation of Concerns: Each class has clear responsibilities. For example, the User class handles user-related actions,
while the Product class focuses on product details.
- Aggregation vs. Association: The relationships between Product and Promotion, and SavedList and Product, are modeled
as associations, reflecting that one can exist without the other but can be related.
- Multiplicity: The design uses multiplicity to show how entities are related to each other. For instance, one user can
save many lists, and a product can have multiple promotions associated with it.
- Extensibility: The system allows for scalability. For instance, the PriceAlert class and Promotion class could be
expanded to handle additional features like expiration dates or additional attributes for discounts.

This class diagram effectively models the system, keeping it modular and adaptable for future changes.
 */