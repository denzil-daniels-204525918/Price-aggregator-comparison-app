# 📌 Use Case Specifications  

---
### 🎯 Use Case: Price aggregator comparison system

---

## Overview

This section outlines the **Use Case Specifications** for the **Price Aggregator Comparison System**, detailing the core functionalities and interactions between users, retailers, admins, data providers, and advertisers.

    1. **Search for Products**: Users can search for grocery items, view matching results, and apply filters to refine their search. If no results are found or data sources are unavailable, the system provides appropriate feedback.
    2. **Compare Prices**: Users can compare prices of a selected product across multiple retailers, apply filters (e.g., price, location), and choose the best option. The system handles scenarios where retailer data is missing or out of stock.
    3. **Subscribe to Price Drop Alerts**: Users can subscribe to price drop alerts for their selected products, ensuring they are notified when prices change. Alternative flows account for situations like unlogged users or missing notification preferences.
    4. **Update Pricing (Retailer)**: Retailers can upload or sync pricing data to keep the system up to date. The system handles errors like invalid data formats or connection failures to ensure data integrity.
    5. **Manage System Data (Admin)**: Admins can manage system data, resolve inconsistencies, and monitor performance. They can also handle data corruption or unauthorized access attempts.
    6. **Publish Promotions (Advertiser)**: Advertisers can upload promotional offers that are displayed to users. The system ensures that data is validated and any conflicts or API failures are appropriately managed.
    7. **Provide Real-Time Data (Data Provider)**: Data providers sync real-time product pricing and availability. The system validates incoming data, handles conflicts, and confirms successful updates to maintain data accuracy.

These use cases collectively outline the critical functionalities of the price comparison platform and ensure that all stakeholders can interact effectively with the system while addressing various edge cases and potential issues.

---

### Use Case 1: Search for Products

---
### Description
- **Purpose**: To allow users to search for grocery items and view available options.
- **Scope**: Covers the process of searching for products, retrieving results, and displaying them to the user.

### Preconditions
- User has internet access.
- System is connected to data sources (e.g., APIs, databases).
- Product data is available from retailers.

### Postconditions
- User views a list of products matching their search query.
- System logs the search query for analytics and recommendations.

### Basic Flow
1. User enters a search query (e.g., "Milk 2L") in the search bar.
2. System validates the query and retrieves product data from connected data sources.
3. System filters and sorts the results based on relevance or user preferences.
4. System displays the list of matching products to the user.
5. User selects a product to view more details.

### Alternative Flows
- **No Results Found**:
  - If no products match the search query, the system displays a message: "No results found. Try a different search."
  - The system suggests popular or related products.
- **Data Source Unavailable**:
  - If a data source fails to respond, the system uses cached data (if available) and notifies the user: "Some data may be outdated."
  - The system logs the error for admin review.
- **Invalid Search Query**:
  - If the user enters an invalid or empty query, the system displays an error message: "Please enter a valid search term."

---

### Use Case 2: Compare Prices

---
### Description
- **Purpose**: To enable users to compare prices of a product across multiple retailers.
- **Scope**: Covers the process of retrieving prices, displaying comparisons, and allowing users to filter results.

### Preconditions
- User has searched for a product.
- Retailers have provided pricing data.
- System is connected to data sources.

### Postconditions
- User views a comparison chart of prices across retailers.
- System logs the comparison for future recommendations.

### Basic Flow
1. User selects a product from the search results.
2. System retrieves pricing data for the product from multiple retailers.
3. System displays a comparison chart showing prices, retailer names, and availability.
4. User applies filters (e.g., sort by price, filter by location).
5. User selects a retailer to view more details or make a purchase.

### Alternative Flows
- **No Retailer Data Available**:
  - If no retailer data is available, the system displays a message: "No pricing data available for this product."
- **Retailer Out of Stock**:
  - If a retailer is out of stock, the system displays: "Out of Stock" next to the retailer’s name.
- **API Failure**:
  - If the system cannot retrieve live data, it uses cached data and notifies the user: "Data may not be up to date."

---

### Use Case 3: Subscribe to Price Drop Alerts

---


### Description
- **Purpose**: To enable users to receive notifications when the price of a product drops.
- **Scope**: Covers the process of subscribing to alerts, monitoring price changes, and sending notifications.

### Preconditions
- User is logged into their account.
- Product is available in the system.
- System has permission to send notifications (e.g., email or SMS).

### Postconditions
- User is subscribed to price drop alerts for the selected product.
- System monitors the product’s price and schedules notifications.

### Basic Flow
1. User selects a product and clicks the "Subscribe to Price Alerts" button.
2. System prompts the user to confirm their notification preferences (e.g., email or SMS).
3. User confirms their preferences.
4. System adds the product to the user’s alert list and begins monitoring its price.
5. System sends a confirmation message: "You are now subscribed to price alerts for [Product Name]."

### Alternative Flows
- **User Not Logged In**:
  - If the user is not logged in, the system prompts them to log in or create an account.
  - After logging in, the system resumes the subscription process.
- **Notification Preferences Not Set**:
  - If the user has not set notification preferences, the system prompts them to configure preferences before subscribing.
- **Product No Longer Available**:
  - If the product is removed from the system, the system notifies the user: "This product is no longer available. Your subscription has been canceled."

---

### Use Case 4: Update Pricing (Retailer)

---

### Description
- **Purpose**: To allow retailers to update product pricing and availability in the system.
- **Scope**: Covers the process of uploading or syncing pricing data with the system.

### Preconditions
- Retailer has access to the system (e.g., via API or admin portal).
- Pricing data is ready for upload or syncing.

### Postconditions
- Product pricing and availability are updated in the system.
- System reflects the latest data for user searches and comparisons.

### Basic Flow
1. Retailer logs into the system or connects via API.
2. Retailer uploads or syncs pricing data for their products.
3. System validates the data and updates the database.
4. System confirms the update: "Pricing data updated successfully."

### Alternative Flows
- **Invalid Data Format**:
  - If the data format is invalid, the system rejects the upload and notifies the retailer: "Invalid data format. Please check your file."
- **Data Conflict**:
  - If there is a conflict with existing data (e.g., duplicate entries), the system prompts the retailer to resolve the conflict.
- **API Connection Failure**:
  - If the API connection fails, the system notifies the retailer: "Connection failed. Please try again later."

---

### Use Case 5: Manage System Data (Admin)

---
### Description
- **Purpose**: To allow admins to manage system data, ensure accuracy, and resolve issues.
- **Scope**: Covers data management, error resolution, and system monitoring.

### Preconditions
- Admin has access to the admin portal.
- System is operational and connected to data sources.

### Postconditions
- System data is accurate and up to date.
- Errors are resolved, and system performance is optimized.

### Basic Flow
1. Admin logs into the admin portal.
2. Admin reviews system data (e.g., product listings, pricing, user logs).
3. Admin resolves any data inconsistencies or errors.
4. Admin monitors system performance and optimizes as needed.
5. System confirms successful updates or changes.

### Alternative Flows
- **Data Corruption**:
  - If data corruption is detected, the system notifies the admin and provides recovery options.
- **Unauthorized Access**:
  - If an unauthorized user attempts to access the admin portal, the system blocks access and logs the attempt.
- **System Outage**:
  - If the system experiences an outage, the admin is notified and provided with troubleshooting steps.

---

### Use Case 6: Publish Promotions (Advertiser)

---

### Description
- **Purpose**: To allow advertisers to publish promotional offers and targeted deals.
- **Scope**: Covers the process of creating, uploading, and displaying promotions.

### Preconditions
- Advertiser has access to the system (e.g., via API or advertiser portal).
- Promotional data is ready for publication.

### Postconditions
- Promotions are published and displayed to users.
- System logs promotional performance for analytics.

### Basic Flow
1. Advertiser logs into the system or connects via API.
2. Advertiser uploads promotional data (e.g., discounts, deals).
3. System validates the data and publishes the promotions.
4. System confirms the publication: "Promotions published successfully."

### Alternative Flows
- **Invalid Promotion Data**:
  - If the promotional data is invalid, the system rejects the upload and notifies the advertiser: "Invalid data. Please check your file."
- **Promotion Conflict**:
  - If there is a conflict with existing promotions, the system prompts the advertiser to resolve the conflict.
- **API Connection Failure**:
  - If the API connection fails, the system notifies the advertiser: "Connection failed. Please try again later."

---

### Use Case 7: Provide Real-Time Data (Data Provider)

---

### Description
- **Purpose**: To allow data providers to supply real-time product pricing and availability data.
- **Scope**: Covers the process of syncing data with the system.

### Preconditions
- Data provider has access to the system (e.g., via API).
- Real-time data is ready for syncing.

### Postconditions
- System reflects the latest product pricing and availability data.
- Data provider’s updates are successfully integrated.

### Basic Flow
1. Data provider connects to the system via API.
2. Data provider syncs real-time pricing and availability data.
3. System validates the data and updates the database.
4. System confirms the sync: "Data synced successfully."

### Alternative Flows
- **Invalid Data Format**:
  - If the data format is invalid, the system rejects the sync and notifies the data provider: "Invalid data format. Please check your file."
- **Data Conflict**:
  - If there is a conflict with existing data, the system prompts the data provider to resolve the conflict.
- **API Connection Failure**:
  - If the API connection fails, the system notifies the data provider: "Connection failed. Please try again later."
---

[Back to Test and Use Case Document.md](Test%20and%20Use%20Case%20Document.md)