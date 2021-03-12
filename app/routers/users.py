from typing import List
from fastapi import Depends, APIRouter, status, Response, HTTPException
from sqlalchemy.orm import Session
import schemas
import database
import models
from repository import user


router = APIRouter(
    tags=['users'],
    prefix='/user'

)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

