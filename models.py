from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    password: str

class BillModel(BaseModel):
    user: str
    text: str
    type: str = "ocr"  # or "qr"
    timestamp: str = ""  # Optional: ISO date string