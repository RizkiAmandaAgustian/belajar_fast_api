from fastapi import FastAPI
from TodoApp import models
from TodoApp.FastApiPsql.database import engine
from TodoApp.FastApiPsql import auth,books3,admin,user




app = FastAPI() #menjadikan ini router utama 

# Membuat tabel jika belum ada
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router) #mengambil auth dari api router dalam file auth dan disini diberi include router sebagai pusat utama route
app.include_router(books3.router)#mengambil auth dari api router dalam file books3 dan disini diberi include router sebagai pusat utama route
app.include_router(admin.router)#mengambil auth dari api router dalam file admin dan disini diberi include router sebagai pusat utama route
app.include_router(user.router)#mengambil auth dari api router dalam file user dan disini diberi include router sebagai pusat utama route





































