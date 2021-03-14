from sqlalchemy.orm import Session
from db import models
from schema import schemas
from fastapi import HTTPException, status
from auth_module import hashing


def create(request: schemas.UserCreate, db: Session):
    new_user = models.User(
        name=request.name, email=request.email, role_id=request.role_id, password=hashing.Hash.bcrypt(request.password))
    role = db.query(models.Role).filter(models.Role.id == request.role_id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Role with the id {request.role_id} is not available')
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user