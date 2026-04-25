# 💰 Finance Data Processing & Access Control Backend

A high-performance backend for a **Finance Dashboard** featuring a Role-Based Access Control (RBAC) system. Built with FastAPI and SQLAlchemy following a clean, modular service-repository architecture.

---

## What It Does

- Manages financial records with strict role-based permission boundaries
- Provides automated summary analytics and real-time dashboard totals
- Enforces Admin / Analyst / Viewer access tiers via custom FastAPI dependency injection
- Aggregates data at the SQL level using `func.sum()` and `group_by` for performance
- Auto-seeds database with test users so reviewers can test immediately via Swagger UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Validation | Pydantic v2 |
| Database | SQLite (portable) |
| Server | Uvicorn (ASGI) |

---

## Access Control Matrix

Uses `x-user-id` header to identify users:

| Feature | Admin (ID: 1) | Analyst (ID: 2) | Viewer (ID: 3) |
|---|---|---|---|
| View Financial Records | ✅ | ✅ | ✅ |
| Create / Update Records | ✅ | ❌ | ❌ |
| View Dashboard Summary | ✅ | ✅ | ❌ |
| Delete Records | ✅ | ❌ | ❌ |

---

## Project Structure

```
finance_backend/
├── app/
│   ├── models/        # SQLAlchemy database models
│   ├── schemas/       # Pydantic v2 validation schemas
│   ├── crud/          # Database operations
│   └── routes/        # API endpoint definitions
├── tests/             # Unit tests
├── finance.db         # SQLite database (auto-generated)
└── requirements.txt
```

---

## Setup & Run

```bash
git clone https://github.com/Siddhimudgal1417/finance_backend.git
cd finance_backend

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) — auto-redirects to Swagger UI for immediate testing.

---

## Key Design Decisions

- **Service-Repository Pattern** — separates models, schemas, CRUD, and routes for testability and scalability
- **SQL-level aggregation** — dashboard totals computed in the database engine, not in Python memory
- **Auto-seeded test data** — startup script populates test users so reviewers can test all permission tiers immediately

---

## Skills Demonstrated

`Python` `FastAPI` `SQLAlchemy` `Pydantic v2` `RBAC` `REST API` `SQLite` `Uvicorn` `Dependency Injection`

---

**Author:** Siddhi Mudgal · [LinkedIn](https://linkedin.com/in/YOUR-LINKEDIN) · [GitHub](https://github.com/Siddhimudgal1417)
