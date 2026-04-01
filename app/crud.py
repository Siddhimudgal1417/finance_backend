from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

# --- Record Operations ---

def get_records(db: Session, skip: int = 0, limit: int = 100):
    """Fetch all financial records with pagination."""
    return db.query(models.FinancialRecord).offset(skip).limit(limit).all()

def create_record(db: Session, record: schemas.RecordCreate):
    """Create a new financial entry."""
    db_record = models.FinancialRecord(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def update_record(db: Session, record_id: int, record_data: schemas.RecordCreate):
    """Update an existing record."""
    db_query = db.query(models.FinancialRecord).filter(models.FinancialRecord.id == record_id)
    db_record = db_query.first()
    if db_record:
        db_query.update(record_data.model_dump(), synchronize_session=False)
        db.commit()
        return db_record
    return None

def delete_record(db: Session, record_id: int):
    """Hard delete a record."""
    db_record = db.query(models.FinancialRecord).filter(models.FinancialRecord.id == record_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
        return True
    return False

# --- Dashboard Analytics ---

def get_financial_summary(db: Session):
    """Calculate totals using SQL aggregation for efficiency."""
    income = db.query(func.sum(models.FinancialRecord.amount)).filter(
        models.FinancialRecord.type == "income"
    ).scalar() or 0.0
    
    expense = db.query(func.sum(models.FinancialRecord.amount)).filter(
        models.FinancialRecord.type == "expense"
    ).scalar() or 0.0
    
    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }

def get_category_breakdown(db: Session):
    """Returns totals grouped by category."""
    return db.query(
        models.FinancialRecord.category, 
        func.sum(models.FinancialRecord.amount).label("total")
    ).group_by(models.FinancialRecord.category).all()