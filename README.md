# Price aggregator comparison app

### A pricing aggregator and comparison application that aims to consolidate information from major grocery stores, allowing users find the best deals on food and beverages in a central location.

---
## Key Features	

* **Search Functionality:** Users can search for specific items.
* **Comparison Engine:** Displays the price differences across multiple retailers.
* **Filter Options:** Allow users to sort by price, location, or retailer.
* **Geolocation Integration:** Suggest deals available nearby or within a specific radius.
* **Daily Specials:** Highlight discounted items or promotions from stores.
* **Notifications:** Send alerts for new deals or when prices drop for a user’s favorite items.
* **Save or share:** Save list to notes or share via text applications.

---

## **_Quick Links_**

### 🧪 Language Choice & Key Design Decisions

➡️ [Click here](#-language-choice-python) 

### Factory Pattern
➡️ [Click here](#Storage-Abstraction-Mechanism)

### Repository Interface Design

➡️ [Click here](#-Justification-for-Repository-Design)

---

Folder structure
      
      Price-aggregator-comparison-app/
         .github/
         .venv/
         docs/
         │
         ├── agile_planning/
         │   ├── agile_planning_document.md
         │   ├── backlog.md
         │   ├── sprint_planning.md
         │   └── user_stories.md
         │
         ├── CICD_implementation/
         │   ├── branch_protection_rules.png
         │   └── protection.md
         │
         ├── diagrams/
         │   ├── activity_diagrams/
         │   │   ├── activity_diagrams.md
         │   │   ├── price_alert.md
         │   │   ├── product.md
         │   │   ├── retailer_profile.md
         │   │   └── user_account.md
         │   ├── state_transition_diagrams/
         │   │   ├── price_alert.md
         │   │   ├── product.md
         │   │   ├── retailer_profile.md
         │   │   ├── state_transition_diagrams.md
         │   │   └── user_account.md
         │   └── Traceability Matrix.md
         ├── domain_model/
         │   ├── class_diagram.js
         │   ├── class_diagram_updated.js
         │   ├── domain_model_documentation.md
         │   └── explanation_of_the_class_diagram.md
         │
         ├── kanban/
         │   ├── index.md
         │   ├── kanban_board.md
         │   ├── kanban_explanation.md
         │   ├── template_analysis.md
         │   └── update 20250504.jpg
         │
         ├── specification/
         │   ├── architecture.md
         │   ├── specification.md
         │   ├── stakeholder_analysis.md
         │   └── system_requirements_document.md
         │
         └── test_use_case_documentation/
             ├── test_case_development.md
             ├── test_use_case_documentation.md
             ├── use_case_diagrams.md
             └── use_case_specifications.md
      src/
      │
      ├── main/
      │   ├── __init__.py
      │   ├── run_scraper.py          # Entry point for scraper
      │   ├── app.py                  # Main orchestrator (optional)
      │   ├── compare_prices.py       # Optional comparison logic
      │   ├── requirements.txt
      │   │
      │   ├── api/
      │   │   ├── __init__.py
      │   │   ├── price_api.py
      │   │   ├── product_api.py
      │   │   └── retailer_api.py
      │   │
      │   ├── models/
      │   │   ├── __init__.py
      │   │   ├── price.py
      │   │   ├── price_alert.py
      │   │   ├── product.py
      │   │   ├── promotion.py
      │   │   ├── retailer.py
      │   │   ├── saved_list.py
      │   │   └── user.py
      │   │
      │   ├── repositories/
      │   │   ├── __init__.py
      │   │   ├── repository.py
      │   │   ├── price_alert_repository.py
      │   │   ├── product_repository.py
      │   │   ├── promotion_repository.py
      │   │   ├── retailer_repository.py
      │   │   ├── saved_list_repository.py
      │   │   ├── user_repository.py
      │   │   └── inmemory/
      │   │       ├── __init__.py
      │   │       ├── inmemory_price_alert_repository.py
      │   │       ├── inmemory_product_repository.py
      │   │       ├── inmemory_promotion_repository.py
      │   │       ├── inmemory_retailer_repository.py
      │   │       ├── inmemory_saved_list_repository.py
      │   │       └── inmemory_user_repository.py
      │   │
      │   ├── services/
      │   │   ├── __init__.py
      │   │   ├── price_service.py
      │   │   ├── product_service.py
      │   │   └── retailer_service.py
      │   │
      │   └── factories/
      │       ├── __init__.py
      │       └── repository_factory.py
      │
      ├── scraper/
      │   ├── __init__.py
      │   ├── checkers_scraper.py
      │   ├── picknpay_scraper.py
      │   └── woolworths_scraper.py
      │
      ├── tests/
      │   ├── __init__.py
      │   ├── unit/
      │   │   ├── __init__.py
      │   │   ├── test_basic.py
      │   │   ├── test_product.py
      │   │   └── test_user.py
      │   └── integration/
      │       ├── __init__.py
      │       └── test_integration.py
      │
      .gitignore
      README.md
      changelog.md
      pyproject.toml
      setup.py

---

## Initial sprint Documentation
[Agile planning document](docs/agile_planning/agile_planning_document.md)

## Test and use case Documentation

* [Test and Use Case Document](docs/Test%20and%20Use%20Case%20Documentation/Test%20and%20Use%20Case%20Document.md)

## Additional Documentation

* Specifications: [specification.md](docs/specification/specification.md)
* Architecture: [architecture.md](docs/specification/architecture.md)
* System Requirements Document (SRD):[system_requirements_document.md](docs/specification/system_requirements_document.md)
* Stakeholder Analysis: [stakeholder_analysis.md](docs/specification/stakeholder_analysis.md)

---

## 🔄 UML State Transition Diagrams

This project models key system behaviors using **UML State Transition Diagrams** to support planning, design, and traceability.

### 📊 Diagrams Overview
| Object           | Activity Diagram & Explanation                                     | State Transition Diagram & Explanation                                  |
|------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------|
| User Account     | [View](docs/diagrams/Activity%20Diagrams/user_account.md)          | [View](./docs/explanations/user_account.md)                             |
| User Login & Authentication | [View](Diagrams/Activity%20Diagrams/user_account.md)    | [View](./docs/explanations/user_account.md)                             |
| Product          | [View](docs/diagrams/Activity%20Diagrams/product.md)               | [View](docs/diagrams/State%20Transition%20Diagrams/product.md)          |
| Price Alert      | [View](docs/diagrams/Activity%20Diagrams/price_alert.md)           | [View](docs/diagrams/State%20Transition%20Diagrams/price_alert.md)      |
| Retailer Profile | [View](docs/diagrams/Activity%20Diagrams/retailer_profile.md)      | [View](docs/diagrams/State%20Transition%20Diagrams/retailer_profile.md) |
| Saved List       | [View](Diagrams/Activity%20Diagrams/user_account.md)               | [View](./docs/explanations/user_account.md)                             |
| Subscription     | [View](Diagrams/Activity%20Diagrams/user_account.md)               | [View](./docs/explanations/user_account.md)                             |
| Retailer Deal Submission | [View](Diagrams/Activity%20Diagrams/user_account.md)       | [View](./docs/explanations/user_account.md)                             |

---
Overview

* [Activity Diagrams.md](docs/diagrams/Activity%20Diagrams/Activity%20Diagrams.md)
* [State Transition Diagrams.md](docs/diagrams/State%20Transition%20Diagrams/State%20Transition%20Diagrams.md)
---

### 📌 Functional Mapping

Each diagram supports functional requirements and sprint work outlined in:

* [SRD.md](docs/specification/system_requirements_document.md)
* [Agile Planning Document.md](Agile%20Planning/Agile%20Planning%20Document.md)

---

| Diagram/Object             | Mapped Functional Requirement (FR)              | User Story / Sprint Task Reference                                                |
|----------------------------|--------------------------------------------------|------------------------------------------------------------------------------------|
| User Account               | FR-001: User account management                 | US-01: "As a user, I want to sign up and manage my profile."                      |
| Product                    | FR-002: Retailers submit/manage items           | US-02: "As a retailer, I want to list and update product info."                  |
| Price Alert                | FR-006: Price drop alerts                       | US-05: "As a user, I want to subscribe to alerts for savings."                   |
| Retailer Dashboard Access | FR-007: Dashboard permission control            | US-06: "As a retailer, I need access to update prices."                          |
| Advertisement Campaign     | FR-008: Ad campaign lifecycle                   | US-07: "As an advertiser, I want to schedule promotions."                        |
| Promotion Content          | FR-009: Filtered promotions view                | US-08: "As a user, I want to filter deals by retailer."                          |
| Saved List                 | FR-010: Saved items                             | US-09: "As a user, I want to save my favorite products."                         |

---

## Class Implementation

---

### 🐍 Language Choice: Python

* Readability & Simplicity
* Strong Support for OOP
* Testing Support
* Cross-Platform

I chose Python for this project because I have some prior knowledge of the language, and it supports object-oriented programming. Python made it easier to define the relationships between classes, which aligned well with the class diagram I had previously created. It also allowed me to clearly structure the methods and responsibilities within each class, and accurately implement the attributes and logic outlined in my domain model.

---

### 🧠 Key Design Decisions

Modular Design with Single Responsibility Principle (SRP)
Each class was designed with a clear responsibility:

* User: manages login and logout - [user.py](src/main/models/user.py)
* Product: holds product details - [product.py](src/main/models/product.py)
* SavedList: allows users to save preferred items - [saved_list.py](src/main/models/saved_list.py)
* Retailer: stores information about stores and available products - [retailer.py](src/main/models/retailer.py)
* Promotion: handles discount logic - [promotion.py](src/main/models/promotion.py)
* PriceAlert: notifies users when price thresholds are met - [price_alert.py](src/main/models/price_alert.py)

---

[**Test cases**](src/price_aggregator/tests) 

---

### ✅ Running Tests

To run the test suite locally:

1. Ensure you have `pytest` installed:
   ```bash
   pip install pytest

2. Navigate to the root directory and run: 
   ```bash
   pytest src/tests

---

# Repository Interface Design

### ✅ Justification for Repository Design

* **Generic Repository Interface:**<br/>
By using a generic repository, we avoid writing duplicate methods for each type of object we want 
to store. Instead, we can use this one interface for all entities.

* **Entity-Specific Repositories:**<br/>
The ProductRepository is specific to the Product entity. It provides the implementation of the CRUD operations using an in-memory storage (_storage dictionary). 
Other repositories (like RetailerRepository) will follow the same pattern but focus on their respective entities.

* **In-Memory Implementation:**<br/>
In-memory storage is fast and easy to implement. We don’t need an external database for now, and it allows for quick testing of CRUD functionality.
It’s also ideal for unit testing, since it doesn’t rely on any external dependencies.

* **Abstraction with Factory Pattern:**<br/>
The Factory Pattern allows easy switching between different repository implementations without modifying other parts of the codebase. 
We can swap out the in-memory store with other storage options (like a database or file system) without changing the business logic.

* **Future-Proofing for Other Backends:**<br/>
We are future-proofing by designing the system to easily switch storage backends. Adding a new storage type (e.g., database) will be straightforward. 
This ensures the application can scale when switching to a more permanent solution like a database.

----
### Storage-Abstraction Mechanism

✅ Why the Factory Pattern 

### 🔁 1. Support multiple storage backends

* App may start with in-memory storage, but later Migrate to a PostgreSQL or MongoDB backend. 
* Add support for external APIs or cloud databases.
* A RepositoryFactory allows you to easily switch.

### 🧱 2. Clear separation of concerns

* The factory pattern keeps your services clean. They ask the factory for a repository — without knowing or caring how it’s implemented.

### ⚙️ 3. Easy extensibility
* You can plug in new backends (e.g., FirestorePromotionRepository, RedisCacheRepository) without changing your service logic.

### 🧪 4. Simpler for testing

* You can inject mock or test versions of repositories easily via the factory.