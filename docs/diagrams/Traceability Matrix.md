## 📌 Traceability Matrix

---

### 🎯 Case: Price aggregator comparison system

---
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

* [SRD.md](SRD.md)
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
* [Back to README](../../../README.md)
