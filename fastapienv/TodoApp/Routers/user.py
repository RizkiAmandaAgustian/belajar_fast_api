from fastapi import FastAPI, Depends , HTTPException, Path , Query , Form ,APIRouter
from sqlalchemy.orm import Session
from typing import List,Annotated, Optional
from TodoApp import models
from TodoApp.database import engine, SessionLocal
from TodoApp.models import todos , users
from starlette import status
from pydantic import BaseModel, Field
from TodoApp.Routers import auth
from .auth import get_current_user
from passlib.context import CryptContext


router = APIRouter(
    prefix='/user',
    tags=['user']
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
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
'''Penjelasan tambahan terkait kode bcrypt_context
schemes=['bcrypt']: Parameter ini digunakan saat membuat objek CryptContext untuk menentukan algoritma hashing yang akan digunakan. 
Dalam hal ini, 'bcrypt' menandakan bahwa algoritma bcrypt akan digunakan untuk hashing kata sandi. 
Bcrypt adalah algoritma hashing yang kuat dan disarankan untuk digunakan dalam menyimpan kata sandi karena kemampuannya dalam melindungi 
terhadap serangan brute force.

deprecated='auto': Parameter ini menentukan bagaimana perilaku harus saat algoritma hashing dianggap sudah kedaluwarsa (deprecated). 
Nilai 'auto' berarti FastAPI akan memberikan peringatan jika algoritma hashing yang digunakan dianggap kedaluwarsa, tetapi masih akan 
mendukung penggunaan algoritma tersebut. Dengan demikian, aplikasi akan tetap berjalan tanpa masalah, tetapi pengguna dianjurkan untuk 
memperbarui penggunaan algoritma hashing.
'''



@router.post('/userpassword',status_code=status.HTTP_202_ACCEPTED)
def change_password_user(user : user_dependency , db : db_dependency ,password_lama : str, password_baru : str = Form(min_length=3)):
    if user is None :
        raise HTTPException(status_code=401 ,detail='FAILED AUTH')
    todo = db.query(users).filter( users.id == user['id']).first()
    #todo akan memiliki users id yang sama dengan user yang login
    if todo is None:
        raise HTTPException(status_code=401,detail='no user information found')
    if not bcrypt_context.verify(password_lama,todo.hashed_password):
        raise HTTPException(status_code=401,detail='Failed Auth')
    todo.hashed_password = bcrypt_context.hash(password_baru)
    db.add(todo) #kata chat gpt digantikan dengan db.add(todo.hashed_password) tidak masalah 
    db.commit()
    # return f'password lama anda adalah {password_lama} dan pasword baru anda adalah {password_baru}' pengecekan password nya saja hehe :)

class VervikiasiPassword (BaseModel):
    password : str
    new_password :str = Field(min_length=6)

@router.put('/password',status_code=status.HTTP_204_NO_CONTENT) #PUNYA MENTOR UDEMY
async def change_password (user : user_dependency, db : db_dependency, user_verification : VervikiasiPassword):
    if user is None:
        raise HTTPException(status_code=401 , detail='auth failed')
    user_model = db.query(users).filter(users.id == user.get('id')).first()
    if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
        raise HTTPException(status_code=401, detail= 'auth failed')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()


@router.get('/todo',status_code=status.HTTP_200_OK)
async def read_all(user : user_dependency, db : db_dependency):
    if user is None or user.get('role') != 'user' :
        raise HTTPException(status_code=401,detail="auth FAil" )
    return db.query(users).filter(todos.owner_id == user.get('id')).first()
    # return db.query(todos).filter(todos.owner_id == user.get('id')).all() jika ingin mendapatkan semua todo yang ada



