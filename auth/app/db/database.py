import os
import configparser
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
config_ini = configparser.ConfigParser()
config_ini.read(path)
POSTGRES_SERVER = config_ini['POSTGRES']['POSTGRES_SERVER']
POSTGRES_DB = config_ini['POSTGRES']['POSTGRES_DB']
# POSTGRES_SERVER = os.getenv('POSTGRES_SERVER')
POSTGRES_PORT = config_ini['POSTGRES']['POSTGRES_PORT']
POSTGRES_USER = config_ini['POSTGRES']['POSTGRES_USER']
POSTGRES_PASSWORD = config_ini['POSTGRES']['POSTGRES_PASSWORD']
# SQLALCHAMY_DATABASE_URL = os.getenv('POSTGRES_URI')
SQLALCHAMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@/{POSTGRES_DB}?host={POSTGRES_SERVER}&port={POSTGRES_PORT}'

engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
