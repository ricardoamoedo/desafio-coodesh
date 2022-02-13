from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import mysql.connector
from pydantic import BaseModel



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
        lista.append('url: '+ str(article_[3]))
        lista.append('imageUrl: '+ str(article_[4]))
        lista.append('newsSite: '+ str(article_[5]))
        lista.append('summary: '+ str(article_[6]))
        lista.append('publishedAt: '+ str(article_[7]))
        lista.append('launches: '+ str(article_[8]))
        lista.append('events: '+ str(article_[9]))
    articles_ = tuple(lista)
    
    return jsonable_encoder(articles_)





@app.get("/articles/{id_articles}")
def get_articles_id(id_articles: int):
    
    query = "SELECT * FROM articles WHERE db_id = " +  str(id_articles)
    cursor_.execute(query)
    search = cursor_.fetchall()
    articles_= search[0]
    
    return jsonable_encoder(articles_)



@app.post("/articles")
def post_articles_id(id_articles: int,featured: bool, title:str, url:str, imageUrl:str, newsSite:str, summary:str, 
publishedAt:str, launches:str, events:str):
    lista = []
    lista.append(str(id_articles))
    lista.append(str(featured))
    lista.append(title)
    lista.append(url)
    lista.append(imageUrl)
    lista.append(newsSite)
    lista.append(summary)
    lista.append(publishedAt)
    lista.append(launches)
    query = "INSERT INTO articles (db_id, db_featured, db_title, db_url, db_imageUrl, db_newsSite, db_summary, db_publishedAt, db_launches, db_events) VALUES (?,?,?,?,?,?,?,?,?,?)"
    cursor_.execute(query, lista)

    db_.commit()

    return {"status": 200, "Message": "new article is post!"}




@app.delete("/articles/{id_articles}")
def del_articles_id(id_articles: int):
    
    query = "DELETE FROM articles WHERE db_id = " +  str(id_articles)
    cursor_.execute(query)
    db_.commit()

    return {"status": 204, "Message": "article is deleted!"}




@app.put("/articles/{id_articles}")
def put_articles_id(id_articles: int):
    query = "UPDATE articles SET db_featured = 1 WHERE db_id = " +  str(id_articles)
    cursor_.execute(query)

    db_.commit()

    return {"status": 200, "Message": "article is updated!"}


def create_article(id: int, featured: str=" ", title: str=" ", url:str=" ", imageUrl:str=" ", newsSite:str=" ", summary:str=" ", 
publishedAt:str=" ", launches:str=" ", events:str=" "):
    query = "SELECT db_id FROM articles WHERE db_id = " + str(id)
    cursor_.execute(query)
    records = cursor_.fetchall()
    

    if records == []:
        sql = "INSERT INTO articles (db_id, db_featured, db_title, db_url, db_imageUrl, db_newsSite, db_summary, db_publishedAt, db_launches, db_events) VALUES (?,?,?,?,?,?,?,?,?,?)"
        var = (id, featured, title, url, imageUrl, newsSite, summary, publishedAt, str(launches), str(events))

        cursor_.execute(sql, var)
        db_.commit()

        return {"status": 200, "Message": "done!"}
