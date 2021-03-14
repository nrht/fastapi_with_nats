from typing import List
from fastapi import Depends, APIRouter, status, Response, HTTPException
from sqlalchemy.orm import Session
from schema import schemas
from auth_module import oauth2
from db import database, models
from repository import role


router = APIRouter(
    tags=['role'],
    prefix='/api/role'

)
get_db = database.get_db


@router.post('/', response_model=schemas.Role)
def create_role(request: schemas.RoleCreate, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return role.create(request, db)


@router.get('/', response_model=List[schemas.Role])
def all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return role.get_all(db)
