from typing import List
from pydantic import BaseModel

class UserInDB(BaseModel):
    id_usuario: int = 0
    nombres: str
    apellidos: str
    documento: str
    email: str
    password: str
   
    
database_users = {}
#generator = {"id_usuario":0}

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.id_habitacion] = user_in_db
    return user_in_db

def get_user(documento: str):
    #documento = int (documento)
    print(documento)
    print(database_users)
    print(database_users.values())
    if documento in database_users.keys():
        print("Entré")
        return database_users[documento]
    else:
        return None