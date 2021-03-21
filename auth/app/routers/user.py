from typing import List
from fastapi import Depends, APIRouter, status, Response, HTTPException
from sqlalchemy.orm import Session
from schema import schemas
from db import database, models
from repository import user
from auth_module import oauth2


router = APIRouter(
    tags=['users'],
    prefix='/api/user'

)
get_db = database.get_db


@router.post('/', response_model=schemas.User)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/', response_model=List[schemas.User])
def all(db: Session = Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
# def get_user(id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.show(id, db)

