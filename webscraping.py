from config.db import open_db, create_article
import requests
import mysql.connector
from sqlalchemy import create_engine

url = 'https://api.spaceflightnewsapi.net/v3/articles/'

page = requests.get(url) 

db_ = mysql.connector.connect(
  host="us-cdbr-east-05.cleardb.net",
  user="b6d5367ae4563a",
  password="d3fd5ed9",
  database="heroku_f831c411194bbea"
)

for n in (page.json()): 
  create_article(int(n['id']),n['featured'], n['title'], n['url'], n['imageUrl'], n['newsSite'], n['summary'], n['publishedAt'], n['launches'], n['events'])
