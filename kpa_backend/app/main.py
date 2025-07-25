from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .db import SessionLocal, engine, Base
from typing import List, Optional
from fastapi import Query

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecListResponse, status_code=201)
def create_wheel_spec(form: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
    existing = db.query(models.WheelSpecification).filter_by(formNumber=form.formNumber).first()
    if existing:
        raise HTTPException(status_code=400, detail="Form already exists")

    db_form = models.WheelSpecification(**form.model_dump())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)


    return {
        "success": True,
        "message": "Wheel specification submitted successfully",
        "data": {
            "formNumber": db_form.formNumber,
            "submittedBy": db_form.submittedBy,
            "submittedDate": db_form.submittedDate,
            "status": "Saved"
        }
    }




@app.get("/api/forms/wheel-specifications", response_model=schemas.WheelSpecListResponse)
def get_wheel_specs(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[str] = Query(None),  
    db: Session = Depends(get_db)
):
    query = db.query(models.WheelSpecification)

    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)


    SELECTED_KEYS = ["treadDiameterNew", "lastShopIssueSize",  "condemningDia","wheelGauge"]

    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully",
        "data": [{
            "formNumber": spec.formNumber,
            "submittedBy": spec.submittedBy,
            "submittedDate": spec.submittedDate.isoformat(),
            "fields": {key: spec.fields[key] for key in SELECTED_KEYS if key in spec.fields}
        } for spec in query.all()],
    }
