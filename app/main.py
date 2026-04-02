import logging
import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv

from .database import engine, Base, SessionLocal
from . import models
from .routes import records, dashboard

# Setup Professional Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load Environment Variables
load_dotenv()

# Create Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Dashboard API",
    description="Backend for financial records with Role-Based Access Control.",
    version="1.0.0",
    debug=os.getenv("DEBUG", "False") == "True"
)

@app.on_event("startup")
def startup_populate_db():
    """
    Seeds the database with initial users if it's empty.
    This ensures the reviewer has immediate accounts to test with.
    """
    db = SessionLocal()
    try:
        if not db.query(models.User).first():
            logger.info("Database is empty. Seeding initial users...")
            test_users = [
                models.User(email="admin@company.com", role="Admin"),
                models.User(email="analyst@company.com", role="Analyst"),
                models.User(email="viewer@company.com", role="Viewer")
            ]
            db.add_all(test_users)
            db.commit()
            logger.info("Successfully seeded 3 users (Admin, Analyst, Viewer).")
        else:
            logger.info("Database already contains data. Skipping seeding.")
    except Exception as e:
        logger.error(f"Error during startup seeding: {e}")
    finally:
        db.close()

@app.get("/", include_in_schema=False)
async def root_redirect():
    """Redirects the root URL to the interactive Swagger UI."""
    return RedirectResponse(url="/docs")

# Include Modular Routers
app.include_router(records.router)
app.include_router(dashboard.router)