import requests
from bs4 import BeautifulSoup

url = 'https://api.spaceflightnewsapi.net/v3/articles/'

page = requests.get(url) 

for n in (page.json()): print (n['id'], "    ", (n['title']))
