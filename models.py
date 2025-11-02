from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    password: str

class BillModel(BaseModel):
    user: str
    text: str
    type: str = "ocr"  # or "qr"
    image: str | None = None # base64 encoded image
    timestamp: str = ""  # Optional: ISO date string
