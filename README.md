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

## 🧪 Language Choice & Key Design Decisions

➡️ [Click here](#-language-choice-python) to jump to the section explaining why Python was chosen and how key classes were designed using object-oriented principles and creational design patterns.

---

Folder structure

    ├── docs
    │   ├── agile_planning
    │   │   ├── agile_planning_document.md
    │   │   ├── backlog.md
    │   │   ├── reflection.md
    │   │   ├── sprint_planning.md
    │   │   └── user_stories.md
    │   ├── diagrams
    │   │   ├── activity_diagrams
    │   │   │   ├── activity_diagrams.md
    │   │   │   ├── price_alert.md
    │   │   │   ├── product.md
    │   │   │   ├── retailer_profile.md
    │   │   │   └── user_account.md
    │   │   ├── state_transition_diagrams
    │   │   │   ├── price_alert.md
    │   │   │   ├── product.md
    │   │   │   ├── retailer_profile.md
    │   │   │   ├── state_transition_diagrams.md
    │   │   │   └── user_account.md
    │   │   ├── reflection.md
    │   │   ├── Traceability Matrix.md
    │   ├── domain_model
    │   │   ├── class_diagram.js
    │   │   ├── domain_model_documentation.md
    │   │   ├── explanation_of_the_class_diagram.md
    │   │   └── reflection.md
    │   ├── kanban
    │   │   ├── index.md
    │   │   ├── kanban_board.md
    │   │   ├── kanban_explanation.md
    │   │   ├── reflection.md
    │   │   └── template_analysis.md
    │   ├── specification
    │   │   ├── architecture.md
    │   │   ├── reflection.md
    │   │   ├── specification.md
    │   │   ├── stakeholder_analysis.md
    │   │   └── system_requirements_document.md
    │   ├── test_use_case_documentation
    │   │   ├── reflection.md
    │   │   ├── test_case_development.md
    │   │   ├── test_use_case_documentation.md
    │   │   ├── use_case_diagrams.md
    │   │   └── use_case_specifications.md
    │   ├── notes.md
    ├── project
    │   └── build.properties
    ├── src
    │   ├── main
    │   │   ├── creational_patterns
    │   │   │   ├── abstract_factory
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── price_alert.py
    │   │   │   │   ├── product.py
    │   │   │   │   ├── promotion.py
    │   │   │   │   ├── retailer_a_factory.py
    │   │   │   │   └── retailer_data_factory.py
    │   │   │   ├── builder
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── price_alert.py
    │   │   │   │   ├── product_report.py
    │   │   │   │   ├── product_report_builder.py
    │   │   │   │   └── promotion.py
    │   │   │   ├── factory_method
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── checkers_data_source.py
    │   │   │   │   ├── data_source.py
    │   │   │   │   ├── data_source_factory.py
    │   │   │   │   └── picknpay_data_source.py
    │   │   │   ├── prototype
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── clone_example.py
    │   │   │   │   └── clone_method.py
    │   │   │   ├── simple_factory
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── product_factory.py
    │   │   │   └── singleton
    │   │   │       ├── __init__.py
    │   │   │       ├── database_connection.py
    │   │   │       └── database_connection_example.py
    │   │   ├── __init__.py
    │   │   ├── price_alert.py
    │   │   ├── product.py
    │   │   ├── promotion.py
    │   │   ├── retailer.py
    │   │   ├── saved_list.py
    │   │   └── user.py
    │   ├── tests
    │   │   ├── creational_pattern
    │   │   │   ├── __init__.py
    │   │   │   ├── test_abstract_factory.py
    │   │   │   ├── test_builder.py
    │   │   │   ├── test_factory_method.py
    │   │   │   ├── test_prototype.py
    │   │   │   ├── test_simple_factory.py
    │   │   │   └── test_singleton.py
    │   │   ├── __init__.py
    │   │   ├── test_price_alert.py
    │   │   ├── test_product.py
    │   │   ├── test_promotion.py
    │   │   ├── test_retailer.py
    │   │   ├── test_saved_list.py
    │   │   └── test_user.py
    │   ├── __init__.py
    │   └── main.py
    ├── build.sbt
    ├── changelog.md
    ├── gitinore
    ├── main.src
    └── README.md

---

## Initial sprint Documentation
[Agile planning document](docs/agile_planning/agile_planning_document.md)

## Test and use case Documentation

* [Test and Use Case Document](docs/Test%20and%20Use%20Case%20Documentation/Test%20and%20Use%20Case%20Document.md)

## Additional Documentation

* Specifications: [Specification](docs/specification/specification)
* Architecture: [Architecture](docs/specification/architecture)
* System Requirements Document (SRD): [SRD](docs/specification/system_requirements_document.md)
* Stakeholder Analysis: [Stakeholder Analysis](docs/specification/stakeholder_analysis.md)

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

* User: manages login and logout - [user.py](src/main/user.py)
* Product: holds product details - [product.py](src/main/product.py)
* SavedList: allows users to save preferred items - [saved_list.py](src/main/saved_list.py)
* Retailer: stores information about stores and available products - [retailer.py](src/main/retailer.py)
* Promotion: handles discount logic - [promotion.py](src/main/promotion.py)
* PriceAlert: notifies users when price thresholds are met - [price_alert.py](src/main/price_alert.py)

---

[**Test cases**](src/tests) 

---

# 🧱 Creational Design Patterns

---
| **Creational Pattern** | **Purpose / Use**                                                                 | **Example in the App**                                                                 | **Location** |
|------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----|
| Simple Factory         | Encapsulates object creation logic for product types in a single factory class.  | ProductFactory creates Product objects based on type like "grocery" or "electronics". |[simple_factory](src/main/creational_patterns/simple_factory)|
| Factory Method         | Delegates object creation to subclasses based on input or context.                | DataSourceFactory returns specific data sources like PicknPaySource, CheckersSource.  |[factory_method](src/main/creational_patterns/factory_method) |
| Abstract Factory       | Creates related objects (product, promotion, alert) without specifying classes.   | RetailerAFactory creates a Product, Promotion, and PriceAlert for a retailer.         |[abstract_factory](src/main/creational_patterns/abstract_factory) |
| Builder                | Constructs complex objects step-by-step, useful when object has many parts.       | ProductReportBuilder builds a report with product, price history, promo, and alert.   |[builder](src/main/creational_patterns/builder) |
| Prototype              | Creates object copies using cloning, to replicate existing templates.             | milk_template.clone() creates a copy of a pre-defined Product template.               |[prototype](src/main/creational_patterns/prototype) |
| Singleton              | Ensures only one instance of a class exists globally throughout the app.          | DatabaseConnection maintains a single database connection shared across the app.      |[singleton](src/main/creational_patterns/singleton) |

---

### 💡 Justification

In our content aggregator application, the use of creational patterns helps manage the complexity of object creation across different layers and modules of the system.

* Simple Factory and Factory Method make the app flexible and extensible, allowing us to add new product types or data sources without changing core logic.
* Abstract Factory ensures that products, promotions, and alerts created for different retailers are consistent and grouped logically.
* Builder simplifies the construction of complex objects like detailed reports, making the code cleaner and more readable.
* Prototype enables rapid duplication of predefined objects like template products, which improves efficiency and consistency.
* Singleton ensures centralized management of shared resources like database connections, avoiding redundancy and potential conflicts.

Together, these patterns promote modularity, scalability, and maintainability, which are essential for a growing application that integrates multiple retailers and serves a wide range of consumer needs.

---


### ✅ Running Tests

To run the test suite locally:

1. Ensure you have `pytest` installed:
   ```bash
   pip install pytest

2. Navigate to the root directory and run: 
   ```bash
   pytest src/tests
