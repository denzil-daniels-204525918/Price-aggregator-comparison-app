# 🧩 Domain Model

---

### 🎯 Case: Price aggregator comparison system

---
## Objective

This document presents a detailed domain model for the Grocery Price Aggregator app. It defines the core entities, their attributes and responsibilities, relationships, and business rules aligned with previous assignments (requirements, user stories, use cases, state/activity diagrams).

---

## 🗂️ Key Domain Entities

### 1. **User**
| Attribute       | Type     | Description                     |
|----------------|----------|---------------------------------|
| userID          | String   | Unique identifier for the user  |
| name            | String   | Full name                       |
| email           | String   | Email address                   |
| password        | String   | Encrypted password              |

**Responsibilities (Methods):**
- `register()`
- `login()`
- `updateProfile()`
- `manageAlerts()`
- `saveList()`

---

### 2. **Retailer**
| Attribute       | Type     | Description                     |
|----------------|----------|---------------------------------|
| retailerID      | String   | Unique ID for the retailer      |
| name            | String   | Store name                      |
| location        | String   | Store address/location          |
| status          | String   | Active, Suspended, or Inactive  |

**Responsibilities (Methods):**
- `submitProduct()`
- `updatePrice()`
- `manageCampaign()`

---

### 3. **Product**
| Attribute       | Type     | Description                     |
|----------------|----------|---------------------------------|
| productID       | String   | Unique product identifier       |
| name            | String   | Product name                    |
| description     | String   | Product details                 |
| category        | String   | E.g., Beverage, Grain           |

**Responsibilities (Methods):**
- `comparePrices()`
- `viewRetailers()`

---

### 4. **PriceEntry**
| Attribute       | Type     | Description                     |
|----------------|----------|---------------------------------|
| entryID         | String   | Unique ID for the price record  |
| price           | Float    | Price of the product            |
| productID       | String   | FK - Related product            |
| retailerID      | String   | FK - Retailer who listed it     |
| dateListed      | Date     | Timestamp of price entry        |

**Responsibilities (Methods):**
- `updatePrice()`
- `trackChanges()`

---

### 5. **PriceAlert**
| Attribute       | Type     | Description                     |
|----------------|----------|---------------------------------|
| alertID         | String   | Unique alert ID                 |
| userID          | String   | FK - Related user               |
| productID       | String   | FK - Product of interest        |
| targetPrice     | Float    | User-defined alert threshold    |
| isActive        | Boolean  | True if alert is active         |

**Responsibilities (Methods):**
- `checkTrigger()`
- `notifyUser()`

---

### 6. **SavedList**
| Attribute       | Type     | Description                     |
|----------------|----------|---------------------------------|
| listID          | String   | Unique list ID                  |
| userID          | String   | FK - List owner                 |
| name            | String   | List name (e.g., “Weekly Groceries”) |

**Responsibilities (Methods):**
- `addProduct()`
- `removeProduct()`
- `shareList()`

---

### 7. **AdvertisementCampaign**
| Attribute       | Type     | Description                     |
|----------------|----------|---------------------------------|
| campaignID      | String   | Unique campaign ID              |
| retailerID      | String   | FK - Associated retailer        |
| title           | String   | Campaign title                  |
| status          | String   | Active, Rejected, Completed     |
| endDate         | Date     | Expiry date of campaign         |

**Responsibilities (Methods):**
- `startCampaign()`
- `endCampaign()`
- `cancelCampaign()`

---

## 🔗 Relationships Overview

- A **User** can create many **SavedLists**
- A **Retailer** can post multiple **Products**
- A **Product** has many **PriceEntries** (from different retailers)
- A **User** can set **PriceAlerts** for Products
- A **Retailer** manages **AdvertisementCampaigns**

---

## 📏 Business Rules

- A **User** can have a maximum of 10 active **PriceAlerts**
- A **Retailer** must be **active** to publish **Products** or **Campaigns**
- A **PriceEntry** must be linked to both a valid **Product** and **Retailer**
- **SavedLists** are private by default but can be shared via URL
- **AdvertisementCampaigns** must be reviewed before activation

---

* [View Class Diagram](class_diagram.js)
* [View Explanation of the Class Diagram](explanation_of_the_class_diagram.md)
