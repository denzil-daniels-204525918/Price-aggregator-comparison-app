### 📌 User Account
```mermaid
graph TD;
    Created -->|Email Verified| Active
    Active -->|User Deactivates| Deactivated
    Active -->|Admin Suspends| Suspended
    Suspended -->|User Appeals| Active
    Deactivated -->|User Reactivates| Active
```
**Explanation:**
- **Key states:** Created, Active, Suspended, Deactivated
- **Transitions:** Email verification activates account; account can be suspended or deactivated by user or admin
- **Mapping to Functional Requirements:** FR-001 (Account management and access control)

---

### 📌 Promotion
```mermaid
graph TD;
    Created -->|Submitted for Approval| Pending
    Pending -->|Approved| Active
    Pending -->|Rejected| Rejected
    Active -->|Expires| Expired
```
**Explanation:**
- **Key states:** Created, Pending, Active, Rejected, Expired
- **Transitions:** Tied to campaign lifecycle and approval system
- **Mapping to Functional Requirements:** FR-005 (Promotion and deal lifecycle)

---

### 📌 Saved List
```mermaid
graph TD;
    Empty -->|User Adds Items| Active
    Active -->|User Shares| Shared
    Active -->|User Removes All Items| Empty
    Shared -->|User Edits| Active
```
**Explanation:**
- **Key states:** Empty, Active, Shared
- **Transitions:** Users manage and share product collections
- **Mapping to Functional Requirements:** FR-006 (List creation and sharing for user convenience)

---

### 📌 Subscription
```mermaid
graph TD;
    Free -->|User Upgrades| Premium
    Premium -->|Subscription Expires| Expired
    Expired -->|User Renews| Premium
    Premium -->|User Cancels| Canceled
```
**Explanation:**
- **Key states:** Free, Premium, Expired, Canceled
- **Transitions:** Managed by user actions and system triggers
- **Mapping to Functional Requirements:** FR-007 (Subscription management and renewal process)

---

### 📌 Retailer Deal Submission
```mermaid
graph TD;
    Draft -->|Submitted| UnderReview
    UnderReview -->|Approved| Published
    UnderReview -->|Rejected| Draft
    Published -->|Deal Expires| Archived
```
**Explanation:**
- **Key states:** Draft, UnderReview, Published, Archived
- **Transitions:** Admin oversight ensures quality and current info
- **Mapping to Functional Requirements:** FR-008 (Retailer submissions and updates to deals)

---
* [Back to State Transition Diagrams](../../State%20Transition%20Diagrams.md)
* [Back to README](../../../README.md)