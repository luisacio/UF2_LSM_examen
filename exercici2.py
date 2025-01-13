from fastapi import FastAPI
from base_model.base_model import Form
from crud.crud import insert_user,select_users
from schema.format_form import format_form
from typing import List

app = FastAPI()

#insertar usuari nou
@app.post("/formulari")
async def add_user(formulari:Form):
    msg = insert_user(formulari)
    return msg

#mostrar tots els usuaris
@app.get("/users/",response_model=List[dict])
async def show_users():
    return format_form(select_users())