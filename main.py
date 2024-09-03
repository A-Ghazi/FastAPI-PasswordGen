from fastapi import FastAPI
import string
import random


app = FastAPI()

@app.get("/generate/{item_length}")
async def gen_password(item_length: int):
    scope = string.ascii_letters + string.digits
    generate_pass = ''.join([random.choice(scope) for n in range(item_length)])

    return{"Generated Password": generate_pass}