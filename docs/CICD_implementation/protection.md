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

# .github/branch-protection-rules.yml
rules:
- name: Main Branch Protection
  branches: [main]
  required_status_checks:
  strict: true
  contexts:
  - test
  - security-scan
  - build
  required_pull_request_reviews:
  required_approving_review_count: 1
  dismiss_stale_reviews: true
  require_code_owner_reviews: false
  restrictions: null
  enforce_admins: false
  allow_force_pushes: false
  allow_deletions: false