from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'Hello, mr': 'Roman'}


@app.get("/book/{book_id}")
async def info(book_id: int):
    return {'Hello, it book unique number': book_id}




