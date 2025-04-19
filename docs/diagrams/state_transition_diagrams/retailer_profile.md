Retailer Profile
```mermaid
graph TD;
    Created -->|Admin Verifies| Active
    Active -->|Retailer Suspended| Suspended
    Suspended -->|Retailer Appeals| UnderReview
    UnderReview -->|Admin Approves| Active
    UnderReview -->|Admin Denies| Suspended
```
**Explanation:**
- **Key states:** Created, Active, Suspended, UnderReview
- **Transitions:** Controlled by admin moderation and appeal processes
- **Mapping to Functional Requirements:** FR-004 (Retailer access and visibility)

---
* [Back to State Transition Diagrams](State%20Transition%20Diagrams.md)
* [Back to README](../../../README.md)
