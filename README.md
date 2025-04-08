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

Folder structure
    
     ── Docs
            ── Agile Planning
                ── Agile Planning Document
                ── Backlog
                ── Reflection  
                ── Sprint Planning
                ── User Stories
            ──  Diagrams
                ── Activity Diagrams
                    ── Activity Diagrams.md
                    ── price_alert.md
                    ── product.md
                    ── retailer_profile.md 
                    ── useer_account.md
                ── State Transition Diagrams
                    ── price_alert.md
                    ── product.md
                    ── retailer_profile.md 
                    ── State Transition Diagrams.md
                    ── user_account.md
                ──  reflection.md
                ──  Traceability Matrix.md
            ──  Kanban
                ──  index.md
                ──  kanban_board.md
                ──  kanban_explanation.md
                ──  reflection.md
                ──  template_analysis.md
            ── Test and Use Case Documentation
                ── Test and Use Case Document.md
                ── Test Case Development.md
                ── Use Case Diagrams.md
                ── Use Case Specifications.md
    src──
    ── Architecture.md
    ── README.md
    ── Reflection.md
    ── Specification.md
    ── SRD.md
    ── Stakeholder Analysis
---

## Initial sprint Documentation



## Test and use case Documentation

* [Test and Use Case Document](docs/Test%20and%20Use%20Case%20Documentation/Test%20and%20Use%20Case%20Document.md)

## Additional Documentation

* Specifications: [Specification](docs/specification/Specification.md)
* Architecture: [Architecture](docs/specification/Architecture.md)
* System Requirements Document (SRD): [SRD](docs/specification/system_requirements_document.md)
* Stakeholder Analysis: [Stakeholder Analysis](Stakeholder%20Analysis.md)
* Reflection: [Reflection](docs/specification/Reflection.md)

---

## 🔄 UML State Transition Diagrams

This project models key system behaviors using **UML State Transition Diagrams** to support planning, design, and traceability.

### 📊 Diagrams Overview
| Object           | Activity Diagram & Explanation                                     | State Transition Diagram & Explanation                                  |
|------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------|
| User Account     | [View](docs/Diagrams/Activity%20Diagrams/user_account.md)          | [View](./docs/explanations/user_account.md)                             |
| User Login & Authentication | [View](Diagrams/Activity%20Diagrams/user_account.md)    | [View](./docs/explanations/user_account.md)                             |
| Product          | [View](docs/Diagrams/Activity%20Diagrams/product.md)               | [View](docs/Diagrams/State%20Transition%20Diagrams/product.md)          |
| Price Alert      | [View](docs/Diagrams/Activity%20Diagrams/price_alert.md)           | [View](docs/Diagrams/State%20Transition%20Diagrams/price_alert.md)      |
| Retailer Profile | [View](docs/Diagrams/Activity%20Diagrams/retailer_profile.md)      | [View](docs/Diagrams/State%20Transition%20Diagrams/retailer_profile.md) |
| Saved List       | [View](Diagrams/Activity%20Diagrams/user_account.md)               | [View](./docs/explanations/user_account.md)                             |
| Subscription     | [View](Diagrams/Activity%20Diagrams/user_account.md)               | [View](./docs/explanations/user_account.md)                             |
| Retailer Deal Submission | [View](Diagrams/Activity%20Diagrams/user_account.md)       | [View](./docs/explanations/user_account.md)                             |

---
Overview

* [Activity Diagrams.md](docs/Diagrams/Activity%20Diagrams/Activity%20Diagrams.md)
* [State Transition Diagrams.md](docs/Diagrams/State%20Transition%20Diagrams/State%20Transition%20Diagrams.md)
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