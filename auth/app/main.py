import os
from fastapi import FastAPI, Request
from db.database import engine, get_db
from routers import user, authentication , role
from db import models


app = FastAPI()

# if the table is not exist, then create
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(role.router)
app.include_router(user.router)


app = FastAPI(openapi_prefix=os.getenv('ROOT_PATH', ''))

@app.get("/")
def read_root(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}
