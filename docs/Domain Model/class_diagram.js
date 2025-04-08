classDiagram
%% === User ===
class User {
+String userID
+String name
+String email
+String password
+register()
+login()
+updateProfile()
+manageAlerts()
+saveList()
}

%% === Retailer ===
class Retailer {
+String retailerID
+String name
+String location
+String status
+submitProduct()
+updatePrice()
+manageCampaign()
}

%% === Product ===
class Product {
+String productID
+String name
+String description
+String category
+comparePrices()
+viewRetailers()
}

%% === PriceEntry ===
class PriceEntry {
+String entryID
+Float price
+String productID
+String retailerID
+Date dateListed
+updatePrice()
+trackChanges()
}

%% === PriceAlert ===
class PriceAlert {
+String alertID
+String userID
+String productID
+Float targetPrice
+Boolean isActive
+checkTrigger()
+notifyUser()
}

%% === SavedList ===
class SavedList {
+String listID
+String userID
+String name
+addProduct()
+removeProduct()
+shareList()
}

%% === AdvertisementCampaign ===
class AdvertisementCampaign {
+String campaignID
+String retailerID
+String title
+String status
+Date endDate
+startCampaign()
+endCampaign()
+cancelCampaign()
}

%% === Relationships ===
User "1" -- "*" SavedList : owns >
User "1" -- "*" PriceAlert : sets >
Retailer "1" -- "*" Product : publishes >
Product "1" -- "*" PriceEntry : has >
Retailer "1" -- "*" PriceEntry : lists >
Retailer "1" -- "*" AdvertisementCampaign : manages >
SavedList "1" -- "*" Product : includes >
PriceAlert "1" -- "1" Product : monitors >
PriceEntry "1" -- "1" Product : related to >

%% Notes for clarification
    note for PriceEntry "Linked to both Product and Retailer"
note for SavedList "Lists are private by default, shareable via URL"
note for PriceAlert "Max 10 active alerts per user"
