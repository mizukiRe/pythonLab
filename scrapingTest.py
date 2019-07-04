import requests
from bs4 import BeautifulSoup
import re

print("Hello world")
 
# BeautifulSoupではURLは直接扱えないのでrequestsを使う（ほかにも選択肢があるよ）
r = requests.get("https://news.yahoo.co.jp/")
 
# 標準ライブラリのhtml.parserでHTMLパース
soup = BeautifulSoup(r.content, "html.parser")

# ここで欲しい要素を抽出すれば良い

# div class:newsFeed_item_title の要素をすべて取得して並べる
# div 要素をすべて取ってからクラスでフィルターして、テキストで取ろう（提案）
soup.find_all("div")

for a in soup.find_all(class_="newsFeed_item_title"):
    print(a.text)  


# print(soup.find_all("a", text=re.compile("札幌")))

# <div class="newsFeed_item_title">

# print(soup.find_all(text="エンタメ"))

# print(soup.select_one("div").get_text())

# print(soup.select_one("newsFeed > ul > li:nth-child(1) > a > div.newsFeed_item_text > div.newsFeed_item_title"))

# for a in soup.find_all('a'):
    # print(a.get('href'))  

