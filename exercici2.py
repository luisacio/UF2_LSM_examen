from fastapi import FastAPI
from base_model.base_model import Form
from crud.crud import insert_user

app = FastAPI()

@app.post("/formulari")
async def add_user(formulari:Form):
    msg = insert_user(formulari)
    return msg