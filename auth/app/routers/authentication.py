from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schema import schemas
from db import database, models
from auth_module import hashing, token_2

router = APIRouter(
    tags=['authentication'],
    prefix='/login'
)
get_db = database.get_db

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Credentials')

    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')
    
    # data = {
    #     "user": user.email,
    #     "role": user.role
    # }

    access_token = token_2.create_access_token(data={"sub": user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
