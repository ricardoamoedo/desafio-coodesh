import mysql.connector

mydb = mysql.connector.connect(
  host="us-cdbr-east-05.cleardb.net",
  user="b6d5367ae4563a",
  password="d3fd5ed9",
  database="heroku_f831c411194bbea"
)

mycursor = mydb.cursor()

def create_article():
    sql = "INSERT INTO articles (db_title, db_url) VALUES (%s, %s)"
