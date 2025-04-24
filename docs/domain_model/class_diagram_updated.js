classDiagram
class User {
+String userId
+String name
+String email
+String password
+login()
+logout()
}

class Product {
+String productId
+String name
+double price
+String description
+addProduct()
+removeProduct()
}

class PriceAlert {
+String alertId
+double priceThreshold
+Boolean isActive
+subscribe()
+unsubscribe()
}

class Retailer {
+String retailerId
+String name
+String contactInfo
+addProduct()
+removeProduct()
}

class SavedList {
+String listId
+String userId
+addProductToList()
+removeProductFromList()
}

class Promotion {
+String promotionId
+String description
+double discount
+applyPromotion()
}

class RepositoryFactory {
+get_promotion_repository(storage_type: String)
+get_product_repository(storage_type: String)
}

class PromotionRepository {
+save(promotion: Promotion)
+find_by_id(promotion_id: String)
+find_all()
+delete(promotion_id: String)
}

class ProductRepository {
+save(product: Product)
+find_by_id(product_id: String)
+find_all()
+delete(product_id: String)
}

class FileSystemPromotionRepositoryStub {
+save(promotion: Promotion)
+find_by_id(promotion_id: String)
+find_all()
+delete(promotion_id: String)
}

class DatabasePromotionRepositoryStub {
+save(promotion: Promotion)
+find_by_id(promotion_id: String)
+find_all()
+delete(promotion_id: String)
}

class RedisPromotionRepositoryStub {
+save(promotion: Promotion)
+find_by_id(promotion_id: String)
+find_all()
+delete(promotion_id: String)
}

User "1" -- "0..*" PriceAlert : subscribes
User "1" -- "0..*" SavedList : saves
Retailer "1" -- "0..*" Product : lists
User "1" -- "0..*" Product : views
Product "1" -- "0..*" Promotion : has
SavedList "1" -- "0..*" Product : contains
RepositoryFactory "1" -- "0..*" PromotionRepository : creates
RepositoryFactory "1" -- "0..*" ProductRepository : creates
PromotionRepository "1" -- "0..*" FileSystemPromotionRepositoryStub : implements
PromotionRepository "1" -- "0..*" DatabasePromotionRepositoryStub : implements
PromotionRepository "1" -- "0..*" RedisPromotionRepositoryStub : implements
ProductRepository "1" -- "0..*" FileSystemProductRepositoryStub : implements
ProductRepository "1" -- "0..*" DatabaseProductRepositoryStub : implements
ProductRepository "1" -- "0..*" RedisProductRepositoryStub : implements
