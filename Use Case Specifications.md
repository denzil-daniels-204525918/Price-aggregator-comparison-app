# Use Case Specifications  

## 🎯 1. Use Case Name  
**Price aggregator comparison system**  

## 👥 2. Actors  
- **User**: A customer who searches for grocery items, compares prices, and subscribes to notifications.  
- **Retailer**: A business entity that provides product pricing and promotional data.  
- **Admin**: A system administrator who manages data integrity and system performance.  
- **Data Provider**: A third-party service that supplies real-time product pricing and availability data.  
- **Advertiser**: A marketing entity that publishes promotional offers and targeted deals.  

## 📌 3. Preconditions  
- Users must have **internet access** and a valid account (if required).  
- Retailers must have **price data available** via API, web scraping, or manual entry.  
- Advertisers must have **promotional data ready** for publication.  
- System must be **connected to data sources** and running without errors.  
- System must have **sufficient storage** to log user interactions and store historical data.  

## 🔄 4. Main Flow  
1. User **searches for a product** (e.g., "Milk 2L").  
2. System **retrieves prices** from multiple retailers via APIs or web scraping.  
3. System **displays a comparison chart** showing price differences.  
4. User **applies filters** (e.g., cheapest first, nearby stores).  
5. User **selects a retailer** for more details.  
6. System **suggests deals and promotions** based on user preferences and browsing history.  
7. User **subscribes to notifications** for future price changes.  
8. System **sends alerts via email or SMS** when price drops occur.  

## 🚨 5. Alternative Flows  
- **Retailer price not available** → Display "Price Unavailable" message.  
- **User enters incorrect product name** → Show suggested alternatives.  
- **API failure** → Fall back to stored price data (if available).  
- **User is not logged in** → Prompt user to log in or create an account.  
- **No promotions available** → Display a message: "No current promotions for this product."  
- **User selects an unavailable retailer** → Display a message: "This retailer is currently unavailable."  

## ❌ 6. Exception Handling  
- If a **user searches for an out-of-stock item**, display an estimated restock date.  
- If the **system cannot fetch live data**, notify the user and retry in the background.  
- If a **retailer withdraws pricing data**, exclude them from future comparisons.  
- If a **user’s notification preferences are not set**, prompt them to configure preferences.  
- If a **data provider fails to respond**, notify the admin and log the error for troubleshooting.  
- If a **user’s search query is too vague**, display a list of popular or trending products.  

## ✅ 7. Postconditions  
- User successfully **compares prices** and identifies the best deal.  
- System **logs user interactions** for future recommendations.  
- Notifications are **scheduled for future price changes** if subscribed.  
- Retailers receive **feedback** on user interactions (e.g., clicks, views, or subscriptions).  
- Advertisers receive **analytics** on the performance of their promotions.  
- System updates **historical price data** for future comparisons.  
