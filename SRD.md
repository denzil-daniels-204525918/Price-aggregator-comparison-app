## 📌 System Requirements Document (SRD) Overview
This document categorizes functional and non-functional requirements, aligning them with key quality attributes to ensure a well-structured system design. As the foundation for the system, it ensures that both business objectives and user expectations are met. 
* **Functional Requirements:** Defines the core features and functionality of the system. Focus on capabilities that directly address stakeholder concerns. Includes acceptance criteria for critical requirements. <br/>
* **Non-Functional Requirements:** Address the overall system usability, deployability, maintenance, scalability, security and performance. <br/>
Also view: #### Stakeholder Analysis: [Stakeholder Analysis.md](Stakeholder Analysis.md) 

## 📌 Functional Requirements

---    
|                     | **Requirement**              | **Acceptance Criteria** |
|---------------------|------------------------------|-------------------------|
| **Usability**       | **Search Functionality**     | ✅ Users can search for specific grocery items by name or category. <br> ✅ Search results return relevant products within **2 seconds**. |
|                     | **Comparison Engine**        | ✅ Users can see a side-by-side price comparison across multiple retailers. <br> ✅ The cheapest option is highlighted for easy selection. |
|                     | **Filter Options**           | ✅ Users can filter results by **price, location, retailer, brand, or promotions**. <br> ✅ Filters apply instantly without page reloads. |
|                     | **Geolocation Integration**  | ✅ Users can view deals available **near their location** or within a **custom radius**. <br> ✅ Location-based filtering updates automatically when the user moves. |
|                     | **Notifications**            | ✅ Users receive **push/email notifications** when prices drop on saved items. <br> ✅ Users can enable or disable notifications in settings. |
|                     | **Save or Share Feature**    | ✅ Users can **save their shopping lists** within the app. <br> ✅ Users can **share price comparisons** via WhatsApp, SMS, or social media. |
| &nbsp;              |                              |                         |
| **Deployability**   | **Platform Compatibility**   | ✅ The system should be deployable on **Windows, Linux**, and major cloud services (AWS, Azure). <br> ✅ The system supports deployment on modern web servers. |
| &nbsp;              |                              |                         |
| **Maintainability** | **Documentation**            | ✅ The documentation shall include an **API guide** for future integrations. <br> ✅ Clear setup instructions for developers and system administrators. |
|                     | **Modular Codebase**         | ✅ Codebase should be **modular** for easy future upgrades. <br> ✅ Each module must have unit tests and clear comments. |
| &nbsp;              |                              |                         |
| **Scalability**     | **System Scalability**       | ✅ The system can handle **1,000 concurrent users** during peak hours. <br> ✅ The database is capable of scaling to handle high traffic. |
|                     | **Store Coverage Expansion** | ✅ New stores can be integrated within **14 business days** without major system changes. <br> ✅ The system scales efficiently as new stores are added. |
| &nbsp;              |                              |                         |
| **Security**        | **Data Security**          | ✅ All user data shall be encrypted using **AES-256** encryption both **in transit and at rest**. <br> ✅ User passwords are stored securely using **bcrypt** hashing. |
|                     | **User Authentication**      | ✅ Users will authenticate via email/password or OAuth (Google, Facebook). <br> ✅ The system shall implement **multi-factor authentication (MFA)**. |
| &nbsp;              |                              |                         |
| **Performance**     | **Search Performance**       | ✅ Search results shall load within **2 seconds** for any query. <br> ✅ The system shall handle search requests efficiently under high load. |
|                     | **Real-Time Price Updates**  | ✅ The system fetches price data via APIs or web scraping at regular intervals. <br> ✅ Data accuracy is maintained above **95%** with minimal latency. |
---

## 📌 Non-Functional Requirements

---
|                              | **Requirement**              | **Acceptance Criteria**           |
|------------------------------|------------------------------|-----------------------------------|
| **Usability**                | **User Interface Design**    | ✅ The system shall have an intuitive, user-friendly interface with a how to secttion to educate users on how to use the app <br> ✅ The interface shall comply with **WCAG 2.1 accessibility standards** to ensure accessibility for users with disabilities. |
|                              | **Search Functionality**     | ✅ The search feature shall be easy to use and return relevant results quickly. <br> ✅ Search filters shall be simple to apply and clear in their purpose.|
| &nbsp;                       |                              |                         |
| **Deployability**            | **Cross-Platform Compatibility** | ✅ The system shall be deployable on **Windows, Linux**, and modern cloud platforms (e.g., AWS, Google Cloud). <br> ✅ Deployment on **Docker containers** should be supported for flexibility. |
|                              | **Continuous Integration/Deployment** | ✅ The system shall have a CI/CD pipeline set up to deploy updates smoothly to production with minimal downtime. |
| &nbsp;                       |                              |                         |
| **Maintainability**          | **Code Documentation**       | ✅ The codebase shall be well-documented, with clear comments and explanations. <br> ✅ An **API guide** will be included for ease of future integrations. |
|                              | **Error Logging & Monitoring** | ✅ The system shall have logging for system errors and user actions to aid future troubleshooting and maintenance. <br> ✅ There will be automated alerts for system failures. |
| &nbsp;                       |                              |                         |
| **Scalability**              | **Horizontal Scalability**   | ✅ The system shall support **horizontal scaling** to accommodate an increasing number of users and stores. <br> ✅ Load balancing shall be implemented to ensure even distribution of traffic. |
|                              | **Database Scalability**     | ✅ The system shall be able to scale the database to accommodate millions of records without significant performance degradation. <br> ✅ Partitioning and replication strategies should be in place to improve database performance. |
| &nbsp;                       |                              |                         |
| **Security**                 | **Data Encryption**          | ✅ All sensitive data (e.g., user passwords, personal information) shall be encrypted using **AES-256** or stronger encryption. <br> ✅ Communication with third-party services shall also be encrypted using **TLS**. |
|                              | **Access Control**           | ✅ Users shall only have access to data they are authorized to view. <br> ✅ Role-based access control (RBAC) shall be implemented. |
|                              | **Session Management**       | ✅ Sessions shall expire after **30 minutes of inactivity**. <br> ✅ Users shall be logged out after multiple failed login attempts, requiring additional authentication steps (e.g., CAPTCHA). |
| &nbsp;                       |                              |                         |
| **Performance**              | **Response Time**            | ✅ The system shall respond to user requests (e.g., searches, comparisons) within **2 seconds**. <br> ✅ High traffic periods shall not result in degraded user experience. |
|                              | **Real-Time Updates**        | ✅ The system shall provide **real-time updates** of prices without requiring page refresh. <br> ✅ Real-time data should be retrieved and displayed with a latency of less than **3 seconds**. |
|                              | **Throughput**               | ✅ The system shall handle at least **1,000 concurrent users** during peak periods. <br> ✅ Each user request shall be handled within **2 seconds**. |
---
