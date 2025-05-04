# Changelog

## [0.1.0] - 2025-05-04
### Added
- Initial FastAPI setup with `/` root route.
- `GET /products/{product_id}` endpoint returning mock product data.
- Swagger UI (`/docs`) and OpenAPI spec (`/openapi.json`) available.
- Product model using `pydantic.BaseModel`.
- Project folder structure organized under `src/` with support for modular development.
- `openapi.json` generated for documentation purposes and saved to `docs/openapi/`.

### Changed
- Renamed `main.py` to `app.py` for proper FastAPI loading with Uvicorn.
- Updated `uvicorn` launch command to reference `app:app`.

### Fixed
- Resolved ASGI app loading error due to incorrect module path.
- Fixed OpenAPI generation by ensuring server is running during `curl` operation.

---


## [v1.0.0] - 2025-04-20
### Added
- Implemented Singleton design pattern
- Added Factory Method with product and creator classes
- Created Builder pattern for product reports
- Developed Abstract Factory for retailer and product creation
- Added unit tests for Singleton, Factory, Builder, and Abstract Factory

### Fixed
- Fixed import issues in test_factory_method.py and test_builder.py
- Updated PYTHONPATH for pytest compatibility
- Improved test coverage and assertions

### Changed
- Refactored Singleton to be thread-safe
- Restructured project folder for clarity and testability

### Removed
- Deprecated unused class `OldRetailerFactory`

