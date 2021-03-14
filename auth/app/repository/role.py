from sqlalchemy.orm import Session
from db import models
from schema import schemas
from fastapi import HTTPException, status
from auth_module import hashing


def create(request: schemas.RoleCreate, db: Session):
    new_role = models.Role(role=request.role)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_all(db: Session):
    return db.query(models.Role).all()
