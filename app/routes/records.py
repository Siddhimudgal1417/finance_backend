from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, security

router = APIRouter(prefix="/records", tags=["Records"])

@router.post("/", response_model=schemas.RecordResponse)
def create_new_record(
    record: schemas.RecordCreate, 
    db: Session = Depends(database.get_db),
    # Only Admin can create
    current_user = Depends(security.RoleChecker(["Admin"])) 
):
    return crud.create_record(db=db, record=record)

@router.get("/", response_model=list[schemas.RecordResponse])
def read_records(
    db: Session = Depends(database.get_db),
    # Admin, Analyst, and Viewer can all read
    current_user = Depends(security.RoleChecker(["Admin", "Analyst", "Viewer"]))
):
    return crud.get_records(db)