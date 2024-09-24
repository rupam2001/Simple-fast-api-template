from fastapi import APIRouter, Path, Depends, HTTPException
from app.dependencies import get_token_header
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.database.schemas.user import User, UserCreate
from app.database.repositories import user_repository
from typing import List

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()


## Endpoints

@router.get("/", tags=['users'], response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_repository.get_users(db=db, skip=skip, limit=limit)
    return users

@router.post("/",tags=['users'], response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existed_user = user_repository.get_user_by_email(db=db, email=user.email)
    if existed_user:
        raise HTTPException(status_code=400, detail="Email already exisit.")
    return user_repository.create_user(db=db, user=user)



