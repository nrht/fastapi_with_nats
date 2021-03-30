from typing import List
from fastapi import Depends, APIRouter, status, Response, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import pandas as pd
import json
from schema import schemas
from auth_module import oauth2
from db import database, models
from repository import role


router = APIRouter(
    tags=['files'],
    prefix='/files'

)
get_db = database.get_db


@router.post('/csv/')
async def parsecsv(file: UploadFile = File(...)):
    contents = await file.read()
    json_string = convertBytesToString(contents)
    return {'file_contents': json_string}


def convertBytesToString(bytes):
    print(bytes)
    data = bytes.decode('cp932').splitlines()
    df = pd.DataFrame(data)
    return parse_csv(df)


def parse_csv(df):
    result = df.to_json(orient='records')
    parsed = json.loads(result)
    return parsed
