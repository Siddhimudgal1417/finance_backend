from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from . import models
from .routes import records, dashboard

# 1. Initialize Database Tables
# This creates the .db file and all tables defined in models.py if they don't exist
Base.metadata.create_all(bind=engine)

# 2. App Instance with Metadata
# This information shows up at the top of your /docs page
app = FastAPI(
    title="Finance Data Management API",
    description="""
    A secure backend for managing financial records with Role-Based Access Control (RBAC).
    
    ### Access Credentials (Use 'x-user-id' Header):
    * **User ID 1**: Admin (Full Access)
    * **User ID 2**: Analyst (View + Dashboard)
    * **User ID 3**: Viewer (View Records Only)
    """,
    version="1.0.0",
    contact={
        "name": "Backend Developer Assessment",
    }
)

# 3. Seed Initial Data
# This ensures the reviewer has users to test with immediately
@app.on_event("startup")
def startup_populate_db():
    db = SessionLocal()
    try:
        # Check if users already exist to avoid duplicates on reload
        if not db.query(models.User).first():
            print("Seeding initial users...")
            users = [
                models.User(email="admin@finance.com", role="Admin"),
                models.User(email="analyst@finance.com", role="Analyst"),
                models.User(email="viewer@finance.com", role="Viewer")
            ]
            db.add_all(users)
            db.commit()
            print("Database seeded successfully.")
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        db.close()

# 4. Root Redirect
# This sends anyone visiting the base URL directly to the interactive docs
@app.get("/", include_in_schema=False)
async def root_redirect():
    """Redirects base URL to the Swagger UI documentation."""
    return RedirectResponse(url="/docs")

# 5. Include Domain Routers
# Keeps the main file clean by importing logic from the routes folder
app.include_router(records.router)
app.include_router(dashboard.router)