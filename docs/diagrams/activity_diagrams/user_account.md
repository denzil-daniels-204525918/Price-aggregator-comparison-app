### 📌 User Registration

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

### 📌 User Login & Authentication

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



### 📌 Filter & Sort Prices

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

### 📌 Save a Shopping List

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

### 📌 Share a Shopping List

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

[Back to README.md](../../../README.md)