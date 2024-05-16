from fastapi import FastAPI, Depends , HTTPException, Path , Query , Form ,APIRouter
from sqlalchemy.orm import Session
from typing import List,Annotated, Optional
from TodoApp import models
from TodoApp.database import engine, SessionLocal
from TodoApp.models import todos
from starlette import status
from pydantic import BaseModel, Field
from TodoApp.Routers import auth
from .auth import get_current_user

router = APIRouter()



# Fungsi untuk mendapatkan instance Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)] #berisi untuk mendapatkan akses kedalam get db
user_dependency = Annotated[dict,Depends(get_current_user)] #berisi untuk mendapatkan akses kedalam get_current_user

'''Penjelasan Annotated
Annotated digunakan untuk memberikan tipe atau metadata tambahan pada dependensi di FastAPI.
Dalam kasus Anda:
db_dependency dijelaskan sebagai Annotated[Session, Depends(get_db)]. 
Ini berarti bahwa db_dependency adalah dependency yang bertipe Session dan dependensinya adalah fungsi get_db().

user_dependency dijelaskan sebagai Annotated[dict, Depends(get_current_user)]. 
Ini berarti bahwa user_dependency adalah dependency yang bertipe dict (yang mengandung informasi pengguna) 
dan dependensinya adalah fungsi get_current_user().
'''

class TodoRequest(BaseModel): 
    title : str = Field(min_length=3) #Field pemberian batasan2 value tertentu dalam body request 
    description : str = Field( min_length=3, max_length= 100)
    priority : int = Field(gt=0 , lt=6)
    complete : bool

# # Fungsi untuk membuat todo baru  # VERSI AI
# def create_todo(db: db_dependency, title: str , description: str, priority: int, complete : bool ):
#     new_todo = models.todos(title=title, description=description, priority=priority, complete=complete)
#     db.add(new_todo)
#     db.commit()
#     db.refresh(new_todo)
#     return new_todo

# Rute untuk menambahkan todo baru/ create DB
@router.post("/todos/",status_code=status.HTTP_201_CREATED)
def add_todo(user : user_dependency,db: db_dependency, title: str = Form (min_length=3), description: str = Form(min_length=3), priority: int = Form(gt=0, lt=6),complete:bool = Form( False)):
    # todo = create_todo(db, title, description, priority,complete) # murni dari AI DAN PROSES BAGIAN INI MASIH MENGGUNAKAN FUNGSI DIATAS NYA 
    # return todo
    todo_baru = models.todos(title = title , description = description, priority = priority, complete = complete, owner_id = user.get('id'))
    db.add(todo_baru)
    db.commit()
    db.refresh(todo_baru)
    return todo_baru

@router.put('/todos/{todo_id}',status_code=status.HTTP_204_NO_CONTENT) 
async def Edit_by_id(db : db_dependency,user:user_dependency,todo_id: int, title: Optional [str] = Form(None,min_length=3) , description: Optional [str] = Form(None,min_length=3,max_length=100), priority: Optional [int]= Form(None,gt=0, lt=6), complete: Optional[bool] = Form()):
#Pemberian parameter menjadi optional dan diberikan nilai default terlebih dahulu sebelum memberikan batasan agar tidak menjadi *required di swagger api dan kita bisa menjadikan nilai terakhir tidak berubah jika memang tidak ditulis
#async def Edit_by_id(db : db_dependency,todo_id: int, title: str = Form(...), description: str = Form(...), priority: int = Form(...), complete: bool = Form(False)):
    # commentar diatas ini MASIH berbentuk REQUEST BODY TAPI BERBENTUK FORMM HMM MENARIK coba diganti aja kalo pengen cek 
    todo_model = db.query(models.todos).filter(models.todos.id == todo_id).filter(todos.owner_id == user['id']).first()
    #jika todo model berhasil mendapatkan id yang sama dengan todo id yang dimasukkan dalam parameter maka todo_model memiliki semua value dalam id tersebut
    if todo_model is None:
        raise HTTPException(status_code=404, detail='TODO NOT FOUND or TODO with different owner id')
    if title is not None and title != '' :
        todo_model.title = title 
    if description is not None and description != '' :
        todo_model.description = description 
    if priority is not None and priority != '' :
        todo_model.priority = priority 
    if complete is not None and complete != '' :
        todo_model.complete = complete
    #sehingga setelah mendapatkan value diatas maka dia bisa mengganti title,description,priority dan complete sebelumnya dengan parameter yang dimasukkan 
    db.add(todo_model)
    db.commit()

''' masih salah 
# Fungsi untuk mendapatkan data dari tabel todos
def get_todos(db: Session):
    return db.query(models.todos).all()  # Menggunakan model todos dari module models

# Rute untuk mendapatkan data todos
@router.get("/todos/", response_model=List[models.todos])
async def read_todos(db: Session = Depends(get_db)):
    todos = get_todos(db)
    return todos
'''

#DB GET ALL
@router.get('/',status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency): #Db untuk mendapatkan dari DB dependensi yang akan mengakses kedalam database
    return db.query(todos).all() #mengembalikan semua data dari daatabase

#DB GET TODOS BY USER ID 
@router.get("/todo/get_by_user_id",status_code=status.HTTP_200_OK)
async def read_all_by_user_id(user : user_dependency, db : db_dependency): #mendapatkan akses kedalam user dari db dependensi dan akses kedalam database dari db dependensi
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(todos).filter(todos.owner_id == user.get('id')).all()#mengembalikan semua todos yang difilter owner dan id dari user yang sama 

@router.post('/todo',status_code=status.HTTP_201_CREATED)
async def create_todo(user : user_dependency, db: db_dependency,todo_request : TodoRequest):
    print(f' INI ADALAH USER DALAM ROUTER LANGSUNG {user}')
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = models.todos(**todo_request.model_dump(), owner_id = user.get('id')) 
    #Todo model akan berisi sebuah request body yang nantinya akan dimasukkan kedalam todos menggunakan metode modeldump dan owner id nya akan mengambil dari user yang login
    db.add(todo_model)
    db.commit() #COBA MIX AND MATCH DENGAN VERSI AI SEHINGGA ENAK TIDAK BERISI BODY TAPI BERISI FORM 

    '''Penjelasan ** dalam model dump 
    Operator ** dalam Python digunakan untuk "unpacking" dictionary atau keyword arguments. 
    Saat digunakan sebelum nama dictionary, ini mengizinkan Anda untuk mem-pass seluruh konten dari dictionary tersebut sebagai argumen 
    ke dalam fungsi atau konstruktor.

    Dalam kasus todo_request.model_dump(), diasumsikan bahwa ini adalah sebuah dictionary yang berisi data yang ingin Anda gunakan 
    untuk membuat instance dari model todos. Dengan menggunakan ** sebelum todo_request.model_dump(), Anda mem-pass semua pasangan kunci-nilai 
    dari dictionary tersebut sebagai argumen ke dalam konstruktor models.todos(). Ini akan mengisi parameter-parameter 
    konstruktor dengan nilai-nilai yang sesuai dari dictionary tersebut.

    Misalnya, jika todo_request.model_dump() mengembalikan dictionary seperti ini:
    
    {'title': 'Membuat Presentasi', 'description': 'Menyiapkan presentasi untuk rapat besok'}
    dan user.get('id') mengembalikan ID pengguna yang sedang melakukan permintaan, menggunakan ** akan membuat konstruktor models.todos() 
    diisi dengan nilai-nilai ini:

    models.todos(title='Membuat Presentasi', description='Menyiapkan presentasi untuk rapat besok', owner_id=user.get('id'))
    Ini memudahkan Anda untuk membuat instance dari model dengan data yang ada dalam dictionary tanpa harus menulis ulang semua pasangan kunci-nilai.
    
    '''

    '''create todo diatas ini akan menghasilkan request body seperti ini walaupun masih bisa diakali menggunakan schema
    tapi saya sendiri lebih suka menggunakan form seperti yang saya buat pada route /todos lebih enak dalam mengisi di form
    dan menghasilkan data yang sama ketika di up ke database jadi masalah preferensi saja 
    {
        "title": "string",
        "description": "string",
        "priority": 0,
        "complete": true
    }
    '''

#GET BY ID
@router.get('/todo/{todo_id}',status_code=status.HTTP_200_OK)
async def read_todo_id ( user : user_dependency, db : db_dependency,todo_id : int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(models.todos).filter(models.todos.id == todo_id).filter(todos.owner_id == user.get('id')).first()
    #todo model akan berisi 1 data yang dimana id todos sama dengan todo id yang dimasukkan dalam parameter dan owner id yang sama dengan id user yang sedang login
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='TODO ID IS NOT FOUND')

@router.put('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT) #Murni dari Udemy 
async def Edit_by_id(user : user_dependency,db : db_dependency,todo_request : TodoRequest, todo_id : int = Path (gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(models.todos).filter(models.todos.id == todo_id).filter(todos.owner_id == user.get('id')).first()
    #todo model akan berisi 1 data yang berisi id yang sama dengan todo id yang dimasukkan dari parameter dan owner id dengan id user yang sedang login 
    if todo_model is None:
        raise HTTPException(status_code=404, detail='TODO NOT FOUND')
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    '''
    create todo diatas ini akan menghasilkan request body seperti ini walaupun masih bisa diakali menggunakan schema
    tapi saya sendiri lebih suka menggunakan form seperti yang saya buat pada route /todos lebih enak dalam mengisi di form
    dan menghasilkan data yang sama ketika di up ke database jadi masalah preferensi saja 
    {
        "title": "string",
        "description": "string",
        "priority": 0,
        "complete": true
    }
    '''
    db.add(todo_model)
    db.commit()

@router.delete('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def detele_todo(user : user_dependency,db:db_dependency,todo_id : int = Path(gt = 0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(models.todos).filter(models.todos.id == todo_id).filter(todos.owner_id == user.get('id')).first()
    #todo model akan berisi 1 data yang memiliki kecocokan antara id todos dan todo id yang ada di parameter serta owner id yang sama dengan user yang sedang login 
    if todo_model is None:
        raise HTTPException(status_code=404 , detail = 'TODO NOT FOUND1')
    db.query(models.todos).filter(models.todos.id == todo_id).filter(todos.owner_id == user.get('id')).delete()
    #atau juga bisa dengan db.delete(todo_model)
    db.commit()

# @router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT) #DARI CHAT GPT TINGGAL DIBANDINGKAN DENGAN YANG DIATAS
# async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
#     if user is None:
#         raise HTTPException(status_code=401, detail='Authentication Failed')

#     todo_model = db.query(todos).filter(todos.id == todo_id, todos.owner_id == user['id']).first()
    
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail='TODO NOT FOUND')

#     db.delete(todo_model)
#     db.commit()

