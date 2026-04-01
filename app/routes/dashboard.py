from fastapi import APIRouter, Depends
from sqlalchemy import func
from .. import models, schemas, database, security

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary", response_model=schemas.DashboardSummary)
def get_summary(db=Depends(database.get_db), 
                user=Depends(security.RoleChecker(["Admin", "Analyst"]))):
    income = db.query(func.sum(models.FinancialRecord.amount)).filter(models.FinancialRecord.type == "income").scalar() or 0
    expense = db.query(func.sum(models.FinancialRecord.amount)).filter(models.FinancialRecord.type == "expense").scalar() or 0
    
    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }