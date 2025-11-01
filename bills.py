from fastapi import APIRouter, HTTPException
from models import BillModel
from mongo_db import bills_collection
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=BillModel)
def save_bill(bill: BillModel):
    bill.timestamp = datetime.utcnow().isoformat()
    bills_collection.insert_one(bill.dict())
    return bill

@router.get("/")
def get_bills(user: str):
    bills = list(bills_collection.find({"user": user}, {"_id": 0}))
    return bills