from src.main.factories.repository_factory import RepositoryFactory
from src.main.repositories.promotion.filesystem_promotion_repository import FileSystemPromotionRepositoryStub
from src.main.repositories.promotion.database_promotion_repository import DatabasePromotionRepositoryStub
from src.main.repositories.promotion.redis_promotion_repository import RedisPromotionRepositoryStub
def test_get_promotion_repository_filesystem():
    repo = RepositoryFactory.get_promotion_repository(storage_type="filesystem")
    assert isinstance(repo, FileSystemPromotionRepositoryStub)

def test_get_promotion_repository_database():
    # Now the factory returns the DatabasePromotionRepositoryStub
    repo = RepositoryFactory.get_promotion_repository(storage_type="database")
    assert isinstance(repo, DatabasePromotionRepositoryStub)

def test_get_promotion_repository_redis():
    # Now the factory returns the RedisPromotionRepositoryStub
    repo = RepositoryFactory.get_promotion_repository(storage_type="redis")
    assert isinstance(repo, RedisPromotionRepositoryStub)

