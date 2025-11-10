from fastapi import APIRouter, HTTPException, Form, File, UploadFile
from models import BillModel
from mongo_db import bills_collection
from datetime import datetime
import base64

router = APIRouter()

@router.post("/", response_model=dict)
async def save_bill(
    user: str = Form(...),
    text: str = Form(...),
    type: str = Form("ocr"),
    image: UploadFile | None = File(None)
):
    """
    Lưu hóa đơn (bill) vào MongoDB.
    - Nếu có ảnh QR được upload, ảnh sẽ được mã hóa base64 và lưu trực tiếp trong Mongo.
    - Không lưu file ảnh vào máy chủ.
    """
    try:
        # Mã hóa ảnh sang base64 nếu có
        image_data = None
        if image:
            image_bytes = await image.read()
            image_data = base64.b64encode(image_bytes).decode("utf-8")

        # Tạo document để lưu
        bill = {
            "user": user,
            "text": text,
            "type": type,
            "timestamp": datetime.utcnow().isoformat(),
            "image_base64": image_data,  # đổi key rõ nghĩa hơn
        }

        # Lưu vào MongoDB
        result = bills_collection.insert_one(bill)

        # Trả về kết quả
        return {
            "message": "Bill saved successfully",
            "bill_id": str(result.inserted_id),
            "data": bill
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving bill: {e}")


@router.get("/", response_model=list)
def get_bills(user: str):
    """
    Lấy danh sách hóa đơn của user (lọc theo 'user').
    Không trả về _id để dễ xử lý phía frontend.
    """
    try:
        bills = list(bills_collection.find({"user": user}, {"_id": 0}))
        return bills
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching bills: {e}")
