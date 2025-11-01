from fastapi import APIRouter, HTTPException
from models import UserModel
from mongo_db import users_collection
from jose import jwt
import datetime

SECRET_KEY = "your-secret-key"

router = APIRouter()

@router.post("/register")
def register(user: UserModel):
    if users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="User exists")
    users_collection.insert_one(user.dict())
    return {"msg": "registered"}

@router.post("/login")
def login(user: UserModel):
    found = users_collection.find_one({"username": user.username})
    if not found or found.get("password") != user.password:
        raise HTTPException(status_code=401, detail="Bad credentials")
    token = jwt.encode(
        {"sub": user.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)},
        SECRET_KEY,
        algorithm="HS256"
    )
    return {"access_token": token, "token_type": "bearer"}

@router.post("/forgot_password")
def forgot_password(user: UserModel):
    # For demo: just check user exists
    found = users_collection.find_one({"username": user.username})
    if not found:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "Password reset link would be sent to your email (demo)"}