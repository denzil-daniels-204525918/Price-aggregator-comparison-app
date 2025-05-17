# Contributing to Price Aggregator Comparison App

Thank you for considering contributing to the Price Content Aggregator! 🎉  
This project is built to help consumers make smarter grocery decisions by comparing prices across stores in South Africa. Your help makes it better!

---

## 📦 Project Setup

### ✅ Prerequisites

Ensure you have the following installed:
- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency and virtualenv management)
- Git
- Make (optional, for automation)

### 🔧 Installation

1. Fork this repository and clone it to your local machine:
   ```bash
   git clone https://github.com/your-username/price-aggregator.git
   cd price-aggregator
   ```
   
2. Set up the project environment:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

  ```bash
  poetry shell
  ```

4. Run initial setup and migrations (if any):

  ```bash
  make setup  # Optional if Makefile is provided
  ```

5. Start the development server:

    ```bash
    uvicorn app.main:app --reload
    ```
---
### 🧪 Coding Standards
✅ Linting & Formatting

We follow PEP8 and use:

    Black (for formatting)

    Flake8 (for linting)

    isort (for import sorting)

Run lint checks before committing:

make lint

Auto-format the codebase:

make format
---
### 🧪 Testing

All tests are written using pytest. Please write tests for any new features or bug fixes.

To run tests:

make test

You can also run:

pytest
---
### 🧩 Picking Issues

    Check the Issues tab.

    Look for labels like:

        good first issue – great for new contributors

        help wanted – active areas of need

    Comment on the issue to express interest.

    Wait for a maintainer to assign it to you before starting work.

---
🚀 Submitting Pull Requests

    Fork the repo and create a new branch:

git checkout -b feature/my-awesome-feature

Follow the commit message style:

feat: add user authentication
fix: correct store name sorting

Push your branch:

    git push origin feature/my-awesome-feature

    Open a Pull Request (PR) against the main branch.

    Your PR should include:

        A clear title and description

        Screenshots if UI-related

        A link to the issue it resolves (e.g. Closes #42)

        Confirmation that linting and tests pass

    A maintainer will review and provide feedback or merge.
---
### 💬 Communication

    For general questions or ideas, open a discussion.

    For bugs or feature requests, open a GitHub Issue.
---
### Thank you for contributing! ❤️
Let’s make smart shopping easier together.


Let me know if you'd like to add badges, CI/CD contribution guidelines, or database configuration instructions as well.

