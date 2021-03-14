import models
from fastapi import FastAPI
from database import engine, get_db
from routers import blog, authentication 


app = FastAPI()

# if the table is not exist, then create
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)