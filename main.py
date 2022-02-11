import config.db
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import mysql.connector



app = FastAPI()


db_ = mysql.connector.connect(
        host="us-cdbr-east-05.cleardb.net",
        user="b6d5367ae4563a",
        password="d3fd5ed9",
        database="heroku_f831c411194bbea"
    )

cursor_ = db_.cursor(prepared=True)

@app.get("/")
def raiz():
    return {"status": 200, "Message": "Back-end Challenge 2021 🏅 - Space Flight News"}



@app.get("/articles")
def get_articles():
    

    cursor_.execute("SELECT * FROM articles")
    new = cursor_.fetchall()
    lista = []

    for article_ in new:
        lista.append('id: '+ str(article_[0]))
        lista.append('feacture: '+ str(bool(article_[1])))
        lista.append('title: '+ str(article_[2]))
        lista.append('imageUrl: '+ str(article_[3]))
        lista.append('newsSite: '+ str(article_[4]))
        lista.append('summary: '+ str(article_[5]))
        lista.append('publishedAt: '+ str(article_[6]))
        lista.append('launches: '+ str(article_[7]))
        lista.append('events: '+ str(article_[8]))
    articles_ = tuple(lista)
    return jsonable_encoder(articles_)





@app.get("/articles/{id_articles}")
def get_articles_id(id_articles: int):
    query = "SELECT * FROM articles WHERE db_id = " +  str(id_articles)
    cursor_.execute(query)
    search = cursor_.fetchall()
    if search ==[]:
        return {"status": 404, "Message": "not found!"}
    articles_= search[0]
    return jsonable_encoder(articles_)



@app.post("/articles")
def post_articles_id(id_articles: int,featured: bool, title:str, url:str, imageUrl:str, newsSite:str, summary:str, 
publishedAt:str, launches:str, events:str):
    lista = []
    lista.append(str(id_articles))
    query = "SELECT db_id FROM articles WHERE db_id = " +  str(id_articles)
    cursor_.execute(query)
    search_id = cursor_.fetchall()
    if (search_id != []):
        list_id = search_id[0]
        lista.append(str(featured))
        lista.append(title)
        lista.append(url)
        lista.append(imageUrl)
        lista.append(newsSite)
        lista.append(summary)
        lista.append(publishedAt)
        lista.append(launches)
        lista.append(events)
    else:
        return {"Status": 404}
        
    return {"status": 200, "Message": "new article is post!"}
