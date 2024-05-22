from TodoApp.FastApiPsql.database import Base
from sqlalchemy import Column, Integer,String,Boolean,ForeignKey
from TodoApp.FastApiPsql.database import conn


class users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True)
    username = Column(String,unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)
    role = Column(String)


class todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean,default=False)
    owner_id = Column(Integer, ForeignKey('users.id'))



def create_barang(title : str, description : str, priority : int, complete : bool,owner_id : int):
    connection = conn.cursor()
    try:
        connection.execute('INSERT INTO todos (title,description,priority,complete) VALUES (%s,%s,%s,%s,%s)',(title,description,priority,complete,owner_id))
        conn.commit()
    except Exception as e :
        conn.rollback()
        raise e
    finally:
        connection.close()


def login_user (username : str):
    connection = conn.cursor()
    try:
        connection.execute('SELECT username,hashed_password,role,id from users WHERE username = %s',(username,))
        ambil_satu = connection.fetchone()
        if ambil_satu is None:
            return None
        return{'username':ambil_satu[0],'hashed_password':ambil_satu[1],'role':ambil_satu[2],'id':ambil_satu[3]}
    except Exception as e :
        conn.rollback()
        raise e 
    finally:
        connection.close()

def buat_users (email : str , username : str , first_name : str , last_name : str, hashed_password : str, is_active : bool, role : str):
    connection = conn.cursor()
    try:
        connection.execute('INSERT INTO users (email,username,first_name,last_name,hashed_password,is_active,role) VALUES(%s,%s,%s,%s,%s,%s,%s)',(email,username,first_name,last_name,hashed_password,is_active,role))
        conn.commit()
    except Exception as e :
        conn.rollback()
        raise e 
    finally:
        connection.close()

def check_password (password : str):
    connection = conn.cursor()
    try : 
        connection.execute ('SELECT from users where hashed_password = %s',(password,))
        fetch = connection.fetchone()
        if fetch is None:
            return None
        return{'hashed_password':fetch[0]}
    except Exception as e :
        conn.rollback()
        raise e 
    finally:
        connection.close()

def change_password (password : str, user_id : int):
    connection = conn.cursor()
    try : 
        connection.execute ('UPDATE users SET hashed_password = %s where id = %s',(password,user_id))
        conn.commit()
    except Exception as e :
        conn.rollback()
        raise e 
    finally:
        connection.close()