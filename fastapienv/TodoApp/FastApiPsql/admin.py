from fastapi import FastAPI, Depends , HTTPException, Path , Query , Form ,APIRouter
from sqlalchemy.orm import Session
from typing import List,Annotated, Optional
from TodoApp.FastApiPsql import models
from TodoApp.FastApiPsql.database import engine, SessionLocal
from TodoApp.FastApiPsql.models import todos
from starlette import status
from pydantic import BaseModel, Field
from TodoApp.Routers import auth
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

# Fungsi untuk mendapatkan instance Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)] #berisi untuk mendapatkan akses kedalam get db
user_dependency = Annotated[dict,Depends(get_current_user)] #berisi untuk mendapatkan akses kedalam get_current_user

class TodoRequest(BaseModel): 
    title : str = Field(min_length=3) #Field pemberian batasan2 value tertentu dalam body request 
    description : str = Field( min_length=3, max_length= 100)
    priority : int = Field(gt=0 , lt=6)
    complete : bool


@router.get('/todo',status_code=status.HTTP_200_OK)
async def read_all(user : user_dependency, db : db_dependency):
    if user is None or user.get('role') != 'Admin' : #atau juga bisa menggunakan user['role']
        raise HTTPException(status_code=401,detail="auth FAil" )
    return db.query(todos).all()#mengembalikan semua nilai todos

@router.delete('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo (user : user_dependency , db : db_dependency,todo_id : int = Path(gt=0)):
    if user is None or user.get('role') != 'Admin':
        raise HTTPException (status_code=401, detail='AUTH FAILED')
    todo_model = db.query(todos).filter(todos.id == todo_id).first()
    #todo model akan memiliki nilai untuk bisa mendapatkan todos yang memiliki id yang sama dengan todo id yang dikirimkan dari parameter
    if todo_model is None:
        raise HTTPException(status_code=401, detail='AUTH FAILDER')
    db.delete(todo_model)
    db.commit()
    