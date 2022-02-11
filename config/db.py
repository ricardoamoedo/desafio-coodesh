import mysql.connector

db_ = mysql.connector.connect(
  host="us-cdbr-east-05.cleardb.net",
  user="b6d5367ae4563a",
  password="d3fd5ed9",
  database="heroku_f831c411194bbea"
)

cursor_ = db_.cursor(prepared=True)



def create_article(id: int, featured: str=" ", title: str=" ", url:str=" ", imageUrl:str=" ", newsSite:str=" ", summary:str=" ", 
publishedAt:str=" ", launches:str=" ", events:str=" "):
    query = "SELECT db_id FROM articles WHERE db_id = " + str(id)
    cursor_.execute(query)
    records = cursor.fetchall()
    

    if records == []:
        sql = "INSERT INTO articles (db_id, db_featured, db_title, db_url, db_imageUrl, db_newsSite, db_summary, db_publishedAt, db_launches, db_events) VALUES (?,?,?,?,?,?,?,?,?,?)"
        var = (id, featured, title, url, imageUrl, newsSite, summary, publishedAt, str(launches), str(events))

        cursor_.execute(sql, var)
        db_.commit()

        return {"status": 200, "Message": "done!"}
