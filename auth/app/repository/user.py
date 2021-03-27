from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import Optional
from db import models
from schema import schemas
from auth_module import hashing, email_validating
from auth_module.exceptions import ValidatingError


def create(request: schemas.UserCreate, db: Session):
    new_user: models.User = models.User(
        name=request.name, email=request.email, role_id=request.role_id, password=hashing.Hash.bcrypt(request.password))
    try:
        email: Optional[str] = email_validating.Validating.validating(
            request.email)
    except ValidatingError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'The email {request.email} is invalid format')

    existing_user: models.User = db.query(models.User).filter(
        models.User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the email {email} is already exist')

    role = db.query(models.Role).filter(
        models.Role.id == request.role_id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Role with the id {request.role_id} is not available')
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    # user = db.query(models.User).filter(models.User.id == id).first()
    user = db.query(models.User, models.Role).join(
        models.User, models.User.role_id == models.Role.id).filter(models.User.id == id).first()
    # role = db.query(models.Role)
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user


def get_all(db: Session):
    # users = db.query(models.User).join(
    #     models.Role, models.User.role_id == models.Role.id).all()
    users = db.query(models.User, models.Role).join(
        models.Role, models.User.role_id == models.Role.id).all()
    return users
