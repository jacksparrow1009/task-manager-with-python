from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dbutils import get_db
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
import os
from auth.schemas import UserCreate, UserLogin
from auth.models import User
from auth.utils import hash_password, verify_password, create_access_token

router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed_password = hash_password(password=user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "status": status.HTTP_200_OK,
        "message": "User registered successfully",
    }


@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.email})

    return {
            "access_token": access_token, 
            "token_type": "bearer",
            "user": db_user, 
            "status": status.HTTP_200_OK,
            "message": "Login successful"
            }
