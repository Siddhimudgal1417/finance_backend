from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String)  # Admin, Analyst, Viewer
    is_active = Column(Integer, default=1)

class FinancialRecord(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)  # income or expense
    category = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String)