from typing import Union

from fastapi import FastAPI

app = FastAPI(
        title="Test-Service",
        version="1.0.0",
        description="Тестовый сервис для проверки пайчарм и гитхаба камунити едишн",
    )

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/githubadd")
def read_root():
    return {"Hello": "World"}

@app.get("/statutes")
def read_root():
    return {"Statuses": "Abobuses"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}