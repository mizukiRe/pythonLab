import requests
from bs4 import BeautifulSoup
import re

# こんにちは python こんにちはpython 
print("Hello world")
 
# BeautifulSoupではURLは直接扱えないのでrequestsを使う（ほかにも選択肢があるよ）
r = requests.get("https://mainichi.jp/")
 
# 標準ライブラリのhtml.parserでHTMLパース
try:
    soup = BeautifulSoup(r.content, "lxml")

except:
    soup = BeautifulSoup(r.content, "html.parser")

# **参考サイト
# URL:http://kondou.com/BS4/
# 公式ドキュメントの日本語訳なのでここを見ればすべてがわかる

# **関数メモ
# find_all はすべての要素を取得
# find　は最初の要素を見つけた時点で終了
# .stripped_strings を使えば、空白を除く事ができる
# .parent を使えば、１つ上の親要素を取得できる
# 属性は　.get("属性名") で取得する。
# find_parents() で

# ここで欲しい要素を抽出すれば良い

get_text = soup.find_all(text = re.compile("カカオ"))

print(get_text)

for GT in get_text:
    print(GT.find_parents(true))  


