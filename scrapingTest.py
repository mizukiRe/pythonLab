print("Hello world")

import requests
from bs4 import BeautifulSoup
 
r = requests.get("https://news.yahoo.co.jp/")
 
soup = BeautifulSoup(r.content, "html.parser")
 
# "主要"ニュースのタイトルを取ってくる 
print(soup.find("div",id="tpc_maj").get_text())

