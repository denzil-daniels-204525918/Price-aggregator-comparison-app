from src.main.promotion import Promotion
from src.main.repositories.promotion.filesystem_promotion_repository import FileSystemPromotionRepositoryStub

def test_save_and_find_promotion():
    repo = FileSystemPromotionRepositoryStub()
    promo = Promotion(
        promotion_id="promo123",
        title="10% off",
        description="A great discount",
        discount_percentage=10,
        duration_days=30  # ✅ Required field added
    )

    repo.save(promo)
    found_promo = repo.find_by_id("promo123")

    assert found_promo is not None
    assert found_promo.promotion_id == "promo123"
    repo._storage.clear()  # Clear the storage after the test

def test_find_all_promotions():
    repo = FileSystemPromotionRepositoryStub()
    promo1 = Promotion(
        promotion_id="promo123",
        title="10% off",
        description="A great discount",
        discount_percentage=10,
        duration_days=30
    )
    promo2 = Promotion(
        promotion_id="promo124",
        title="20% off",
        description="Even better discount",
        discount_percentage=20,
        duration_days=45
    )

    repo.save(promo1)
    repo.save(promo2)

    all_promos = repo.find_all()
    assert len(all_promos) == 2
    assert any(p.promotion_id == "promo123" for p in all_promos)
    assert any(p.promotion_id == "promo124" for p in all_promos)

    repo._storage.clear()  # Clear after the test

def test_delete_promotion():
    repo = FileSystemPromotionRepositoryStub()
    promo = Promotion(
        promotion_id="promo123",
        title="10% off",
        description="A great discount",
        discount_percentage=10,
        duration_days=30
    )

    repo.save(promo)
    repo.delete("promo123")
    deleted_promo = repo.find_by_id("promo123")

    assert deleted_promo is None
    repo._storage.clear()  # Clear after the test

