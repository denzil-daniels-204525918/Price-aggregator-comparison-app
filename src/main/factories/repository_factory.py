from src.main.repositories.promotion.filesystem_promotion_repository import FileSystemPromotionRepositoryStub
from src.main.repositories.promotion.database_promotion_repository import DatabasePromotionRepositoryStub
from src.main.repositories.promotion.redis_promotion_repository import RedisPromotionRepositoryStub
from src.main.repositories.promotion_repository import PromotionRepository

class RepositoryFactory:
    @staticmethod
    def get_promotion_repository(storage_type: str = "filesystem") -> PromotionRepository:
        if storage_type == "database":
            return DatabasePromotionRepositoryStub()
        elif storage_type == "redis":
            return RedisPromotionRepositoryStub()
        else:
            return FileSystemPromotionRepositoryStub()
