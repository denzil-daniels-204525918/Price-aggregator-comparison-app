# Test Case Documentation

---
### 🎯 Test Case:
**Price aggregator comparison system**

---

## Functional Test Cases

| Test Case ID | Requirement ID | Description                          | Steps                                                                 | Expected Result                     | Actual Result | Status (Pass/Fail) |
|--------------|----------------|--------------------------------------|-----------------------------------------------------------------------|-------------------------------------|---------------|--------------------|
| TC-001       | FR-001         | User searches for a product          | 1. Enter product name. <br> 2. Click "Search."                        | Results display within 2 seconds.   |               |                    |
| TC-002       | FR-002         | User compares prices                 | 1. Select a product. <br> 2. Click "Compare Prices."                  | Price comparison chart displayed.   |               |                    |
| TC-003       | FR-003         | User subscribes to price alerts      | 1. Select a product. <br> 2. Click "Subscribe to Alerts."             | Confirmation message displayed.     |               |                    |
| TC-004       | FR-004         | Retailer updates pricing             | 1. Retailer logs in. <br> 2. Upload pricing data.                     | Pricing updated successfully.       |               |                    |
| TC-005       | FR-005         | Admin manages system data            | 1. Admin logs in. <br> 2. Resolve data inconsistencies.               | Data accuracy confirmed.            |               |                    |
| TC-006       | FR-006         | Advertiser publishes promotions      | 1. Advertiser logs in. <br> 2. Upload promotional data.               | Promotions published successfully.  |               |                    |
| TC-007       | FR-007         | Data provider syncs real-time data   | 1. Data provider connects via API. <br> 2. Sync pricing data.         | Data synced successfully.           |               |                    |
| TC-008       | FR-008         | User applies filters to search       | 1. Enter search query. <br> 2. Apply filters (e.g., price range).     | Filtered results displayed.         |               |                    |

---

## Non-Functional Test Scenarios

### Performance Test
- **Scenario**: Simulate 1,000 concurrent users searching for products.
- **Steps**:
  1. Use a load testing tool (e.g., JMeter) to simulate 1,000 users.
  2. Execute search queries simultaneously.
  3. Measure response time for each query.
- **Expected Result**: Response time ≤ 2 seconds for 95% of queries.
- **Actual Result**: [To be filled after testing]
- **Status**: [Pass/Fail]

### Security Test
- **Scenario**: Verify secure access to the admin portal.
- **Steps**:
  1. Attempt to access the admin portal without credentials.
  2. Attempt to access with incorrect credentials.
  3. Attempt to access with valid credentials.
- **Expected Result**:
  - Access denied for unauthorized users.
  - Access granted for authorized users.
- **Actual Result**: [To be filled after testing]
- **Status**: [Pass/Fail]

---

[Back to Test and Use Case Document.md](Test%20and%20Use%20Case%20Document.md)