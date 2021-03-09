from enum import Enum
from typing import Optional
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import schemas, models
from database import engine, SessionLocal

app = FastAPI()

# if the table is not exist, then create
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog