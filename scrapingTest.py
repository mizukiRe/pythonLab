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
# find_parents() を使えば見つけた要素から上の要素を取得することができる。

# print(soup.get_text()・・・ページからタグを除去して全テキストを抽出

# for link in soup.find_all('a'):・・・ページの<a>タグ内にあるURLを全て抽出
#       print(link.get('href'))

# **やりたいこと
# 特定の文字列を取得して、そのリンクを取得したい

# シカと含まれている要素をすべて取得
get_text = soup.find_all(text = re.compile("シカ"))

print(get_text)

for GT in get_text:

    # 文字列だけ取得してみる
    # print(GT.find_parent('a').string)

    # find_parent("a")で親要素のaを取得してhrefを取り出す
    print(GT.find_parent('a').get("href") + "END")
   
# めっちゃ忘れてる…。家かえって復習しないと忘れる