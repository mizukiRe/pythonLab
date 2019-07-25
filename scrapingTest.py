import requests
from bs4 import BeautifulSoup
import re

def HelloWorld():

    print("ハローワールドクラス")

class Test:

    def test_print(self):
        print('This is test')

"""
doc



"""
HelloWorld()

test = Test()      #インスタンス生成
test.test_print()  #メソッド呼び出し



# 変数名は小文字のみで、単語間をアンダースコアで区切る
# 検索ワード
search_word = "司法"

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
# find_all はすべての要素を取得（見つからない場合の戻り値は空のリスト？）
# find　は最初の要素を見つけた時点で終了(見つからない場合の戻り値はNON)
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
get_text = soup.find_all(text = re.compile(search_word))

print(get_text)

for GT in get_text:

    # 文字列だけ取得してみる
    # print(GT.find_parent('a').string)

    # find_parent("a")で親要素のaを取得してhrefを取り出す
    print(GT.find_parent('a').get("href"))
   
# めっちゃ忘れてる…。家かえって復習しないと忘れる


