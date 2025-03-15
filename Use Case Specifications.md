# Use Case Specifications  

## 🎯 1. Use Case Name  
**Price Comparison & Deal Notification System**  

## 👥 2. Actors  
- **User**: Searches for grocery items and compares prices.  
- **Retailer**: Provides product pricing and promotions.  
- **Admin**: Manages system data and ensures accuracy.  
- **Data Provider**: Supplies real-time product pricing and availability.  
- **Advertiser**: Publishes promotional offers and targeted deals.  
- **System**: Processes user queries, stores data, and sends notifications.  

## 📌 3. Preconditions  
- Users must have **internet access** and a valid account (if required).  
- Retailers must have **price data available** via API, web scraping, or manual entry.  
- System must be **connected to data sources** and running without errors.  

## 🔄 4. Main Flow  
1. User **searches for a product** (e.g., "Milk 2L").  
2. System **retrieves prices** from multiple retailers.  
3. System **displays a comparison chart** showing price differences.  
4. User **applies filters** (e.g., cheapest first, nearby stores).  
5. User **selects a retailer** for more details.  
6. System **suggests deals and promotions** if available.  
7. User **subscribes to notifications** for future price changes.  
8. System **sends alerts** when price drops occur.  

## 🚨 5. Alternative Flows  
- **Retailer price not available** → Display "Price Unavailable" message.  
- **User enters incorrect product name** → Show suggested alternatives.  
- **API failure** → Fall back to stored price data (if available).  

## ❌ 6. Exception Handling  
- If a **user searches for an out-of-stock item**, display an estimated restock date.  
- If the **system cannot fetch live data**, notify the user and retry in the background.  
- If a **retailer withdraws pricing data**, exclude them from future comparisons.  

## ✅ 7. Postconditions  
- User successfully **compares prices** and identifies the best deal.  
- System **logs user interactions** for future recommendations.  
- Notifications are **scheduled for future price changes** if subscribed.  
