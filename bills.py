from fastapi import APIRouter, HTTPException, Form, File, UploadFile
from models import BillModel
from mongo_db import bills_collection
from datetime import datetime
import base64

router = APIRouter()

@router.post("/")
async def save_bill(
    user: str = Form(...),
    text: str = Form(...),
    type: str = Form("ocr"),
    image: UploadFile | None = File(None)
):
    try:
        image_data = None
        if image:
            image_bytes = await image.read()
            image_data = base64.b64encode(image_bytes).decode("utf-8")

        bill = {
            "user": user,
            "text": text,
            "type": type,
            "timestamp": datetime.utcnow().isoformat(),
            "image": image_data
        }
        bills_collection.insert_one(bill)
        return {"message": "Bill saved", "data": bill}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def get_bills(user: str):
    bills = list(bills_collection.find({"user": user}, {"_id": 0}))

    return bills


