# pythonのクラスと関数は先に宣言してからじゃないと呼び出せない
# ついでにIFとリストの実験をする

"""
doc:ここからNoneの比較実験



"""
# __eq__(self, other)は特殊変数らしいけど何やってるのこのクラス
# returnでTrue返してるけど、中身が__main__.Foo object at 0x0059EC10になってるし謎
# 参考：https://blog.pyq.jp/entry/Python_kaiketsu_181220_is_none
class Foo:
    def __eq__(self, other):  # 同値性検査の動作をカスタマイズ
        return True

name = Foo()

# isで比較するとFALSEになる（正常な動作）
if name is None:
    print("TRUE :isNONE")
else:
    print("FALSE:isNONE")

# ==で比較するとTRUEになる（異常な動作）
if name == None:
    print("TRUE :==NONE")
else:
    print("FALSE:==NONE")

# 通常の使い方なら=（同値性）で比較しても問題はないが、想定外の結果になる可能性もあるので
# 必ずNoneの比較はis（同一性）で行う

prev = ""
for animal in ["cat", "dog", "tiger", "lion", "puma", "horse"]:
    print ("value of animal :", animal)
    prev = prev + animal
    print (prev)
    
print ("This is out of for block")



"""
doc:クラスについての実験


"""
# クラスのドキュメントってどうやって書けば良いの？
def HelloWorld():

    print("ハローワールド関数３")

class Test:

    def test_print(self):
        print('This is test')

"""
doc



"""
HelloWorld()

test = Test()      #インスタンス生成
test.test_print()  #メソッド呼び出し
