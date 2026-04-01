# 💰 Finance Data Processing & Access Control Backend

## 🚀 Project Overview
This project is a high-performance backend for a **Finance Dashboard**, featuring a robust **Role-Based Access Control (RBAC)** system. It allows for the secure management of financial records, provides automated summary analytics, and enforces strict permission boundaries between different user roles.

The system is built using **FastAPI** and **SQLAlchemy**, following a clean, modular architecture that separates concerns between routing, data validation, and database logic.

### Key Features
- **RBAC Security:** Custom FastAPI dependency injection to enforce permissions for Admins, Analysts, and Viewers.
- **Automated Summaries:** Efficient SQL-level data aggregation for real-time dashboard totals.
- **Strict Validation:** Data integrity ensured via Pydantic v2 models and SQLAlchemy types.
- **Interactive Documentation:** Fully configured Swagger UI for easy API testing and evaluation.

---

## 🛠️ Technical Stack
- **Language:** Python 3.10+
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ORM:** SQLAlchemy (with SQLite for portability)
- **Validation:** Pydantic v2
- **Server:** Uvicorn (ASGI)

---

## 🏗️ Architecture & Design Decisions
1. **Service-Repository Pattern:** Instead of a monolithic structure, logic is divided into `models`, `schemas`, `crud`, and `routes`. This ensures the code is unit-testable and scalable.
2. **Database Aggregation:** To optimize performance, dashboard totals (Net Balance, Category Totals) are calculated within the SQL engine using `func.sum()` and `group_by`, minimizing Python memory overhead.
3. **Seamless DX (Developer Experience):** The root URL (`/`) automatically redirects to `/docs`, and a startup script seeds the database with test users, allowing reviewers to test functionality immediately.

---

## 🔑 Access Control Matrix
The system uses the `x-user-id` header to identify users:

| Feature | Admin (ID: 1) | Analyst (ID: 2) | Viewer (ID: 3) |
| :--- | :---: | :---: | :---: |
| View Financial Records | ✅ | ✅ | ✅ |
| Create/Update Records | ✅ | ❌ | ❌ |
| View Dashboard Summary | ✅ | ✅ | ❌ |
| Delete Records | ✅ | ❌ | ❌ |

---

## 🏃 How to Run Locally

### 1. Setup Environment
```bash
# Clone the repository
cd finance_backend

# Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt