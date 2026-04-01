from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class RecordBase(BaseModel):
    amount: float
    type: str
    category: str
    description: Optional[str] = None

class RecordCreate(RecordBase):
    pass

class RecordResponse(RecordBase):
    id: int
    date: datetime
    class Config:
        from_attributes = True

class DashboardSummary(BaseModel):
    total_income: float
    total_expense: float
    net_balance: float