# 🛣️ Price Content Aggregator – Product Roadmap

This roadmap outlines the upcoming features and improvements planned for the Price Content Aggregator App. The goal is to help consumers in South Africa make smarter, cost-effective grocery shopping decisions through transparent price comparison and AI-powered insights.

---

## ✅ Completed

- [x] Core product and store models
- [x] REST API with FastAPI
- [x] Basic product search and price comparison
- [x] User authentication and saved lists
- [x] Initial testing and documentation

---

## 🔨 In Progress

- [ ] Geolocation support in product search
- [ ] Admin panel for managing stores and products
- [ ] Initial OpenAPI/Swagger documentation updates

---

## 🧠 Planned Features

### 📍 Location-Aware Features
- [ ] Store filtering based on city/suburb or user location
- [ ] Radius-based product search using GPS/geolocation
- [ ] Display nearest stores and available deals

### 🔁 Price History & Trends
- [ ] Track historical price changes for each product
- [ ] Add endpoint: `/api/products/{id}/price-history`
- [ ] Display price trend graphs in frontend (optional)

### 🛍️ Promotions & Deals
- [ ] Daily Deals API endpoint
- [ ] Add deal expiry dates and highlighting in UI
- [ ] Support for multi-store promotion comparison

### 🔔 Notifications & Alerts
- [ ] Price drop alerts (via email or push)
- [ ] Custom price threshold notifications
- [ ] Subscription to category or store deals

### 🤖 AI & Smart Suggestions
- [ ] Personalized product recommendations
- [ ] Best-value basket suggestions (based on cart items)
- [ ] Predictive pricing trends

---

## 📦 Technical Enhancements

- [ ] Implement PostgreSQL backend
- [ ] Add Redis caching for frequent queries
- [ ] CI/CD integration with GitHub Actions
- [ ] Dockerize the app for easy deployment
- [ ] Add Sentry for error tracking and monitoring

---

## 🧪 Developer Experience

- [ ] Improve setup scripts and Makefile coverage
- [ ] Add more unit and integration tests
- [ ] Interactive API documentation (Swagger & ReDoc)
- [ ] Contribution badges and GitHub templates

---

## 💬 Have Suggestions?

We welcome feature ideas and feedback from the community!  
Feel free to [open an issue](https://github.com/your-repo/issues/new?template=feature_request.md) or start a [GitHub Discussion](https://github.com/your-repo/discussions).

---

*Let’s build smarter shopping tools—together.* 🛒✨
