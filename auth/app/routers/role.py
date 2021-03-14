from typing import List
from fastapi import Depends, APIRouter, status, Response, HTTPException
from sqlalchemy.orm import Session
from schema import schemas
from db import database, models
from repository import role


router = APIRouter(
    tags=['role'],
    prefix='/role'

)
get_db = database.get_db


@router.post('/', response_model=schemas.Role)
def create_role(request: schemas.RoleCreate, db: Session = Depends(get_db)):
    return role.create(request, db)


@router.get('/', response_model=List[schemas.Role])
def all(db: Session = Depends(get_db)):
    return role.get_all(db)
