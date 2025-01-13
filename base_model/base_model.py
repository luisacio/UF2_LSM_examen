from pydantic import BaseModel
from typing import Optional

class Form(BaseModel):
    nombre:str
    apellido:str
    correoelectronico:str
    descripcion:Optional[str] = None
    curso:str
    anyo:int
    direccion:str
    codigopostal:Optional[int] = None
    password:str

