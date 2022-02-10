#from config.db import conn
from fastapi import FastAPI
from pydantic import BaseModel #retirar o basemodel

app = FastAPI()

@app.get("/")
def raiz():
    return {"status": 200, "Message": "Back-end Challenge 2021 🏅 - Space Flight News"}



class Usuario(BaseModel):
    id: int
    email: str
    senha: str



base_de_dados = [
    Usuario(id=1, email="teste@teste.com.br", senha="teste123"),
    Usuario(id=2, email="ricardo@ricardo.org.br", senha="ricardo456")
]



@app.get("/articles")
def get_articles():
    return base_de_dados



@app.get("/articles/{id_articles}")
def get_articles_id(id_articles: int):
    for article in base_de_dados:
        if (article.id == id_articles):
            return article
    
    return {"status": 404, "Message": "article not found"}



@app.post("/articles/{id_articles}")
def put_articles_id(id_articles: int):
        
    return id_articles
