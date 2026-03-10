from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model import User
from schemas import UserCreate, UserLogin, Token, UserOut
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

router = APIRouter(prefix="/account", tags=["Account"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM  = os.getenv("ALGORITHM", "HS256")
EXPIRE_MIN = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


def create_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MIN)
    return jwt.encode(
        {"sub": str(user_id), "exp": expire},
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# POST /account/register
@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=pwd_context.hash(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "access_token": create_token(new_user.id),
        "token_type": "bearer",
        "user": new_user
    }


# POST /account/login
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "access_token": create_token(db_user.id),
        "token_type": "bearer",
        "user": db_user
    }


# GET /account/{user_id}
@router.get("/{user_id}", response_model=UserOut)
def get_account(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user