from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/fastapi_postgresql'


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)

Base = declarative_base()

db_config = {
    'dbname': 'fastapi_postgresql',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}

conn = psycopg2.connect(**db_config)