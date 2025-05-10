# Branch Protection Rules for `main`

This document explains why branch protection is enforced in this repository.

## **Why Protect `main`?**
✅ **Prevents Broken Code** – Ensures all changes are reviewed and tested before merging.  
✅ **Enforces Code Quality** – Mandates PR reviews, reducing bugs and bad commits.  
✅ **Blocks Direct Pushes** – No accidental/unreviewed changes bypassing CI.

## **Rules Applied**
1. **PR Review Required** – At least 1 approval before merging.
2. **CI Checks Must Pass** – Ensures tests/linting pass before merging.
3. **No Direct Pushes** – All changes must go through a PR.

🚀 **Result:** A stable, reliable `main` branch with fewer production issues!  