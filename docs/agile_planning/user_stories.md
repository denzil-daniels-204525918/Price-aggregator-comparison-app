# 📌 User Stories

---
### 🎯 Case: Price aggregator comparison system

---
## Overview

User stories define key features from the end user's perspective, focusing on actions and outcomes. They follow the 
INVEST criteria for clarity and feasibility, and are prioritized using the MoSCoW method. These stories ensure the system 
delivers valuable features first, such as product search and price comparison, guiding the development to meet user needs 
and business objectives efficiently.

---
## Functional Requirements
| **Story ID** | **Feature**                     | **User Story**                                                                                                            | **Acceptance Criteria**                                                                                                                                                                   | **Priority** |
|--------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| US-001       | **Search Functionality**        | As a user, I want to search for products so that I can quickly find the items I need.                                     | ✅ The system shall allow users to enter search terms and return relevant results within 2 seconds. <br> ✅ Search results shall include product name, price, retailer, and availability. | High         |
| US-002       | **Comparison Engine**           | As a user, I want to compare product prices across multiple retailers so that I can choose the most affordable option.    | ✅ The system shall display a side-by-side price comparison for the same product from different retailers. <br> ✅ Users shall be able to sort results by price, rating, and retailer.    | High         |
| US-003       | **Filter Options**              | As a user, I want to filter products by price, location, and retailer so that I can refine my search results.             | ✅ The system shall provide filter options for price range, retailer, and location. <br> ✅ The applied filters shall immediately update the search results.                              | Medium       |
| US-004       | **Geolocation Integration**     | As a user, I want the system to suggest deals based on my location so that I can find the best prices nearby.             | ✅ The system shall request location permission from users. <br> ✅ Users shall be able to see deals available within a user-defined radius (e.g., 5km, 10km).                            | Medium       |
| US-005       | **Daily Specials & Promotions** | As a user, I want to see daily promotions and discounts so that I can take advantage of the best deals.                   | ✅ The system shall display a dedicated section for daily promotions and store-specific deals. <br> ✅ Users shall be able to filter promotions by category or retailer.                  | Medium       |
| US-006       | **Price Drop Alerts**           | As a user, I want to receive notifications when a product’s price drops so that I can purchase it at the best time.       | ✅ Users shall be able to subscribe to price drop alerts for specific products. <br> ✅ Notifications shall be sent via email or app alerts when a price drop occurs.                     | High         |
| US-007       | **Retailer Pricing Updates**    | As a retailer, I want to update my product prices in real time so that customers see accurate pricing information.        | ✅ Retailers shall have access to a dashboard where they can update pricing instantly. <br> ✅ Price changes shall reflect in the system within 1 minute.                                 | High         |
| US-008       | **Advertisement Management**    | As an advertiser, I want to publish promotions on the platform so that I can reach potential customers more effectively.  | ✅ Advertisers shall be able to create and schedule promotional campaigns. <br> ✅ Users shall see targeted promotions based on browsing history and preferences.                         | Medium       |

---
1. **Search Functionality:** As a user, I want to search for products so that I can quickly find the items I need.
2. **Comparison Engine:** As a user, I want to compare product prices across multiple retailers so that I can choose the most affordable option.
3. **Filter Options:** As a user, I want to filter products by price, location, and retailer so that I can refine my search results.
4. **Geolocation Integration:** As a user, I want the system to suggest deals based on my location so that I can find the best prices nearby.
5. **Daily Specials & Promotions:** As a user, I want to see daily promotions and discounts so that I can take advantage of the best deals.
6. **Price Drop Alerts:** As a user, I want to receive notifications when a product’s price drops so that I can purchase it at the best time.
7. **Retailer Pricing Updates:** As a retailer, I want to update my product prices in real time so that customers see accurate pricing information.
8. **Advertisement Management:** As an advertiser, I want to publish promotions on the platform so that I can reach potential customers more effectively.
---
## Non-functional Requirements
| **Story ID** | **Requirement**              | **Acceptance Criteria** | **Priority** |
|-------------|-----------------------------|-------------------------|------------|
| NFR-001     | **Usability** – User Interface Design | ✅ The system shall have an intuitive, user-friendly interface with a "How To" section for user guidance. <br> ✅ The interface shall comply with WCAG 2.1 accessibility standards for users with disabilities. | High |
| NFR-002     | **Deployability** – Cross-Platform Compatibility | ✅ The system shall be deployable on Windows, Linux, and cloud platforms (AWS, Google Cloud). <br> ✅ Docker support shall be included for flexible deployment. | High |
| NFR-003     | **Maintainability** – Code Documentation | ✅ The codebase shall be well-documented, including inline comments and API documentation. <br> ✅ A developer guide shall be provided to assist future enhancements. | Medium |
| NFR-004     | **Maintainability** – Error Logging & Monitoring | ✅ The system shall include logging for errors and user actions. <br> ✅ Automated alerts shall notify admins of system failures or downtime. | High |
| NFR-005     | **Scalability** – Horizontal Scaling | ✅ The system shall support horizontal scaling to handle increasing users and retailers. <br> ✅ Load balancing shall ensure even traffic distribution. | High |
| NFR-006     | **Scalability** – Database Performance | ✅ The system shall efficiently store and retrieve large volumes of data without performance degradation. <br> ✅ Partitioning and replication strategies shall be implemented for scalability. | Medium |
| NFR-007     | **Security** – Data Encryption | ✅ All sensitive data (e.g., passwords, personal details) shall be encrypted using AES-256. <br> ✅ All communications with third-party services shall be encrypted using TLS. | High |
| NFR-008     | **Security** – Access Control | ✅ Role-Based Access Control (RBAC) shall be implemented to restrict data access. <br> ✅ Users shall only access information they are authorized for. | High |
| NFR-009     | **Security** – Session Management | ✅ Sessions shall automatically expire after 30 minutes of inactivity. <br> ✅ Users shall be logged out after multiple failed login attempts, requiring CAPTCHA for re-login. | Medium |
| NFR-010     | **Performance** – Response Time | ✅ Search results shall be returned within 2 seconds. <br> ✅ The system shall handle 1,000 concurrent users during peak hours. | High |
| NFR-011     | **Performance** – Real-Time Updates | ✅ The system shall provide real-time price updates without requiring a page refresh. <br> ✅ Updates shall be displayed within 3 seconds of data change. | Medium |
| NFR-012     | **Performance** – Throughput | ✅ The system shall process at least 1,000 API requests per second without failure. <br> ✅ The database shall be optimized to handle high read/write operations efficiently. | High |

---
1. Usability
* As a user, I want an intuitive and accessible interface so that I can easily navigate and use the system without confusion.
* As a user with disabilities, I want the system to comply with WCAG 2.1 accessibility standards so that I can interact with it without barriers.

2. Deployability
* As a developer, I want the system to be deployable on Windows, Linux, and cloud platforms so that it can run on various environments without modification.
* As a DevOps engineer, I want Docker support so that deployment remains flexible and consistent across different environments.

3. Maintainability
* As a developer, I want well-documented code so that future maintenance and feature enhancements are easier to implement.
* As a team lead, I want logging and monitoring in place so that system issues can be detected and resolved quickly.

4. Scalability
* As a system architect, I want the system to scale horizontally so that it can handle an increasing number of users and retailers without performance issues.
* As a database administrator, I want efficient data storage and retrieval so that performance is not affected by large datasets.

5. Security
* As a user, I want my personal data to be securely encrypted so that my privacy is protected from unauthorized access.
* As a security officer, I want role-based access control (RBAC) implemented so that users can only access authorized information.
* As an admin, I want session management policies in place so that inactive users are logged out after a period of inactivity.

6. Performance
* As a user, I want the system to return search results within 2 seconds so that I don’t experience delays when looking for products.
* As a user, I want real-time price updates so that I see the latest pricing without having to refresh the page.
* As a system administrator, I want the system to process at least 1,000 API requests per second so that performance remains stable under heavy usage.
---