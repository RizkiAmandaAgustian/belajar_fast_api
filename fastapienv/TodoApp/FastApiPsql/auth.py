from fastapi import APIRouter, Depends , HTTPException, Form
from pydantic import BaseModel
from TodoApp.FastApiPsql.models import users
from passlib.context import CryptContext
from TodoApp.FastApiPsql.database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone
from bcrypt import hashpw,gensalt
from TodoApp.FastApiPsql import models



router = APIRouter(
    prefix='/auth', #AGAR SEMUA API DIBAWAH INI AKAN MEMILIKI AWALAN AUTH
    tags=['auth'] #agar semua api di bawah ini dikelompokkan dalam bagan auth di swagger
)

SECRET_KEY = 'TES32'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer2 = OAuth2PasswordBearer(tokenUrl='auth/token_tanpaorm',scheme_name="Schema_ganti_password")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token',scheme_name="Schema_Basic") #MENCARI BYDEFAULT KENAPA INI YANG ADA UNTUK LOGIN

'''Penjelasan tambahan terkait kode bcrypt_context dan oauth2_bearer
schemes=['bcrypt']: Parameter ini digunakan saat membuat objek CryptContext untuk menentukan algoritma hashing yang akan digunakan. 
Dalam hal ini, 'bcrypt' menandakan bahwa algoritma bcrypt akan digunakan untuk hashing kata sandi. 
Bcrypt adalah algoritma hashing yang kuat dan disarankan untuk digunakan dalam menyimpan kata sandi karena kemampuannya dalam melindungi 
terhadap serangan brute force.

deprecated='auto': Parameter ini menentukan bagaimana perilaku harus saat algoritma hashing dianggap sudah kedaluwarsa (deprecated). 
Nilai 'auto' berarti FastAPI akan memberikan peringatan jika algoritma hashing yang digunakan dianggap kedaluwarsa, tetapi masih akan 
mendukung penggunaan algoritma tersebut. Dengan demikian, aplikasi akan tetap berjalan tanpa masalah, tetapi pengguna dianjurkan untuk 
memperbarui penggunaan algoritma hashing.

OAuth2PasswordBearer(tokenUrl='auth/token'): Ini adalah objek untuk skema autentikasi OAuth2 menggunakan metode bearer token. 
Parameter tokenUrl menentukan URL tempat aplikasi klien dapat meminta token akses. Dalam hal ini, tokenUrl='auth/token' 
menandakan bahwa endpoint untuk meminta token akses adalah /auth/token.
'''

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    Last_name: str
    password: str
    role: str


def get_current_user_tanpaorm(token: Annotated[str, Depends(oauth2_bearer2)]):
    try:
        print(f' ini adalah token {token}')
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('username')
        hashed_password: str = payload.get('hashed_password')  # Menambahkan ini
        role: str = payload.get('role')
        id : str = payload.get('id')
        print(f' INI ADALAH USERNAME {username} dan ini adalah user_id {hashed_password} dan ini role nya {role} dan yang terakhir ini adalah {id}')

        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {'username': username, 'hashed_password': hashed_password, 'role': role, 'id':id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user1.')

    

class Token(BaseModel):
    access_token : str
    token_type : str 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user_tanpaorm)] #berisi untuk mendapatkan akses kedalam get_current_user



def autentikasi_user(username: str, password: str, db: db_dependency):
    user = db.query(users).filter(users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_acces_token(username :str , user_id : int ,role :str,  expires_delta : timedelta):
    encode = {'sub': username, 'id' : user_id, 'role':role} #mengisi akses token yang berisi username user id dan role
    expired = datetime.now() + expires_delta #memasukkan expired dengan memasukkan jam sekarang + expired delta yang dimasukkan sebagai parameter nanti
    encode.update({'exp': expired}) #menambahkan waktu expired kepada encode
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM) #membuat jwt token yang didalamnya terdapat informasi username, user_id, secret key dan

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]): #dalam chat gpt dikatakan fungsinya mirip dengan jwt_required() di flask api
    try:
        print(f' ini adalah token {token}')
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) #melakukan proses decodes terhadap isi token 
        username: str = payload.get('sub') #pengambilan sub
        user_id: int = payload.get('id') #pengambilan id
        role :str = payload.get('role') #pengambilan role
        print(f' INI ADALAH USERNAME {username} dan ini adalah user_id {user_id} dan ini role nya {role}')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user.')
        return {'username': username, 'id': user_id, 'role' : role} #jika memang benar ada username dan userid maka akan mengembalikan nilai username, id dan role
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user1.')

    
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    hashed_password = bcrypt_context.hash(create_user_request.password)
    new_user = users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.Last_name,
        role=create_user_request.role,
        hashed_password=hashed_password,
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/tesaja", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest, db: db_dependency):
    hashed_password = bcrypt_context.hash(create_user_request.password)
    new_user = users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.Last_name,
        role=create_user_request.role,
        hashed_password=hashed_password,
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    print(f' ini adalah form data {form_data}')

    user = autentikasi_user(form_data.username, form_data.password, db)
    #penggunaan db dalam parameter variabel user untuk mendapatkan koneksi ke database guna verivikasi data
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Couldntttt validate user')
    token = create_acces_token(user.username, user.id,user.role, timedelta(hours=24))
    return {'access_token': token, 'token_type': 'bearer'} #kepenulisan harus sama dengan class token
'''
masalah ternyata bukan di penamaan class tapi memang fast api ketika menggunakan OAUTHBEARER mengharuskan kita
mengembalikan atau return sebuah akses token dengan nama access token dengan double S ketika menggunakan
single S entah kenapa sistem tidak mengenali akses token tersebut 
penjelasan dari chatGPT:
Kesimpulan
Untuk menggunakan OAuth2PasswordBearer di FastAPI, Anda harus mengembalikan token dengan kunci "access_token".
Jika Anda menggunakan kunci lain seperti "acces_token" (dengan single 's'), 
FastAPI tidak akan dapat mengenali token dengan benar, dan ini akan menyebabkan masalah dalam autentikasi. '
Konsistensi dalam penggunaan kunci "access_token" adalah kunci untuk memastikan implementasi 
yang benar dan sesuai dengan standar.
https://chatgpt.com/c/8801a37f-5052-496f-9bbc-0306f6829d01
'''


def buat_akses_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    print(f'INI ADALAH ISI TO ENCODE {to_encode}')
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post('/token_tanpaorm')
async def login_tanpa_orm(form: OAuth2PasswordRequestForm = Depends()):
    try_login = models.login_user(form.username)
    print(f'INI ADALAH ISI DARI TRY LOGIN {try_login}')
    if try_login is None:
        raise HTTPException(status_code=401, detail='Username tidak ditemukan')
    if not bcrypt_context.verify(form.password, try_login['hashed_password']):
        raise HTTPException(status_code=401, detail='Input password anda salah')
    access_token = buat_akses_token(try_login, timedelta(hours=1))
    return {'access_token': access_token, 'token_type': 'bearer'}

    
@router.post('/buat_users')
async def buat_users_tanpa_orm(
    email: str = Form(min_length=5),
    username: str = Form(min_length=4, max_length=20),
    first_name: str = Form(min_length=4, max_length=50),
    last_name: str = Form(min_length=4, max_length=50),
    password: str = Form(None),
    is_active: bool = Form(False),
    role: str = Form(None)
):
    hashed_password = bcrypt_context.hash(password)
    models.buat_users(email, username, first_name, last_name, hashed_password, is_active, role)
    return status.HTTP_204_NO_CONTENT

@router.post('/ganti_password_user')
async def ganti_password_tanpaorm(user: user_dependency, password: str = Form(None), password_lama: str = Form(None)):
    print(user)
    if user is None:
        raise HTTPException(status_code=401, detail='Tidak bisa validasi user')
    
    if not bcrypt_context.verify(password_lama, user['hashed_password']):
        raise HTTPException(status_code=401, detail='Password lama salah')
    new_hashed_password = bcrypt_context.hash(password)
    models.change_password(new_hashed_password, user['id'])
    return status.HTTP_204_NO_CONTENT

@router.post("/rehash_passwords", status_code=status.HTTP_200_OK)
async def rehash_passwords_endpoint(db: db_dependency):
    users = db.query(models.users).all()
    for user in users:
        if not user.hashed_password.startswith("$2b$"):  # Memeriksa apakah hash adalah bcrypt
            user.hashed_password = bcrypt_context.hash(user.hashed_password)
    db.commit()
    return {"message": "Passwords have been rehashed"}