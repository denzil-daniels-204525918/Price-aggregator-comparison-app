# 📌 Activity Diagrams

## 🎯 Objective
This document presents UML activity diagrams for key workflows in the system. Each workflow is designed to enhance system efficiency, user experience, and stakeholder satisfaction.


✅ User Registration – Creating an account.
✅ User Login & Authentication – Secure access.
✅ Search for a Product – Finding grocery items.
✅ Filter & Sort Prices – Customizing search results.
✅ Save a Shopping List – Organizing favorite items.
✅ Share a Shopping List – Sending lists to others.
✅ Set Price Alerts – Notifying users of price drops.
✅ Retailer Price Updates – Ensuring accurate data.

---
# Activity Workflow Modeling

## 1. User Registration

```mermaid
graph TD;
    A[Start] --> B[Enter User Details];
    B --> C[Validate Input];
    C -->|Valid| D[Create Account];
    C -->|Invalid| E[Show Error Message];
    D --> F[Send Confirmation Email];
    F --> G[User Verifies Email];
    G --> H[Account Activated];
    H --> I[End];
```

### Explanation:
- Ensures users enter valid information before creating an account.
- Confirmation email step adds security and prevents fake accounts.

---

## 2. User Login & Authentication

```mermaid
graph TD;
    A[Start] --> B[Enter Username & Password];
    B --> C[Validate Credentials];
    C -->|Valid| D[Grant Access];
    C -->|Invalid| E[Show Error Message];
    D --> F[End];
```

### Explanation:
- Basic authentication ensures secure access.
- Error handling prevents unauthorized access.

---

## 3. Search for a Product

```mermaid
graph TD;
    A[Start] --> B[User Enters Search Query];
    B --> C[Fetch Matching Products];
    C --> D[Display Results];
    D --> E[End];
```

### Explanation:
- Ensures users can find items efficiently.
- Fetches data dynamically for real-time updates.

---

## 4. Filter & Sort Prices

```mermaid
graph TD;
    A[Start] --> B[User Applies Filters];
    B --> C[Sort by Price, Retailer, Rating];
    C --> D[Update Results];
    D --> E[End];
```

### Explanation:
- Enhances usability by allowing filtering options.
- Sorting improves decision-making.

---

## 5. Save a Shopping List

```mermaid
graph TD;
    A[Start] --> B[User Selects Items];
    B --> C[Click Save List];
    C --> D[Store List in User Profile];
    D --> E[End];
```

### Explanation:
- Allows users to track preferred products.
- Saves data for future reference.

---

## 6. Share a Shopping List

```mermaid
graph TD;
    A[Start] --> B[User Selects Saved List];
    B --> C[Click Share];
    C --> D[Generate Shareable Link];
    D --> E[Send via Email/Social Media];
    E --> F[End];
```

### Explanation:
- Helps users collaborate on grocery shopping.
- Shareable links make distribution seamless.

---

## 7. Set Price Alerts

```mermaid
graph TD;
    A[Start] --> B[User Selects Product];
    B --> C[Click 'Set Price Alert'];
    C --> D[User Defines Target Price];
    D --> E[System Monitors Prices];
    E -->|Price Drops| F[Send Notification];
    F --> G[End];
```

### Explanation:
- Helps users get notified of deals.
- Automates price tracking for convenience.

---

## 8. Retailer Price Updates

```mermaid
graph TD;
    A[Start] --> B[Retailer Logs In];
    B --> C[Navigate to Dashboard];
    C --> D[Update Product Prices];
    D --> E[Changes Reflected in System];
    E --> F[End];
```

### Explanation:
- Ensures accurate price updates from retailers.
- Keeps system data fresh and relevant.

---

These workflows align with the system’s functional requirements and use cases by ensuring **smooth user interactions, real-time updates, and a seamless shopping experience**.

---