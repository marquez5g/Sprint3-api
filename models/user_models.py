from pydantic import BaseModel


class UserIn(BaseModel):
    """ id_usuario: int = 0
    
    apellidos: str
    documento: int
    email: str
    """
    documento: str
    password: str 
    
class UserOut(BaseModel):
    id_usuario: int
    nombres: str
    apellidos: str