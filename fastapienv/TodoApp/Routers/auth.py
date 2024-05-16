from fastapi import APIRouter, Depends , HTTPException
from pydantic import BaseModel
from TodoApp.models import users
from passlib.context import CryptContext
from TodoApp.database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone


router = APIRouter(
    prefix='/auth', #AGAR SEMUA API DIBAWAH INI AKAN MEMILIKI AWALAN AUTH
    tags=['auth'] #agar semua api di bawah ini dikelompokkan dalam bagan auth di swagger
)

SECRET_KEY = 'TES32'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
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


# class Token(BaseModel):
#     access_token : str
#     token_type : str 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

def autentikasi_user(username : str , password : str , db: db_dependency):
    user = db.query(users).filter(users.username == username).first() #disini akan mendapatkan semua informasi user 
    if not user :
        return False #jika tidak ada username tersebut akan mendapatkan false 
    if not bcrypt_context.verify(password,user.hashed_password):#disini akan dilakukan pengecekan password dibandingkan dengan yang sudah di hashed
        return False
    return user #jika sudah berhasil akan dikembalikan semua informasi user tersebut 

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

    
@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user (db : db_dependency, create_user_request : CreateUserRequest):
    create_user_request = users(
        email = create_user_request.email,
        username = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.Last_name,
        role = create_user_request.role,
        hashed_password = bcrypt_context.hash(create_user_request.password),
        is_active = True
    )
    

    db.add(create_user_request)
    db.commit()

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    print(f' ini adalah form data {form_data}')

    user = autentikasi_user(form_data.username, form_data.password, db)
    #penggunaan db dalam parameter variabel user untuk mendapatkan koneksi ke database guna verivikasi data
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Couldnt validate user')
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

