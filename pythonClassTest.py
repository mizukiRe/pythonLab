# pythonのクラスと関数は先に宣言してからじゃないと呼び出せない
# ついでにIFとリストの実験をする

# docstringはグーグルスタイルをずっと使う
# VsCodeのプラグイン「autoDocstring」をインストールして設定→autoDocstringで検索してGoogleスタイルに変える

# __eq__(self, other)は特殊変数らしいけど何やってるのこのクラス
# returnでTrue返してるけど、中身が__main__.Foo object at 0x0059EC10になってるし謎
# 参考：https://blog.pyq.jp/entry/Python_kaiketsu_181220_is_none
class Foo:
    """ここでクラスの説明

    Returns:
        [type] -- [description]
    """
    def __eq__(self, other):  # 同値性検査の動作をカスタマイズ
        """[summary]
        
        Returns:
            [type]: [description]
        """

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
print("//----------ここまでIFでNONEを比較する際の実験----------//")

"""
doc:リスト（配列）の実験　


"""
class List_instance:
    class_aaa = 999999
    class_bbb = "gg_wp_lol"

# 宣言
list_test_empty = [] 

# 宣言と同時に要素を入れる
list_test_in = [12,222,333,444]

# 文字列と数字を混ぜてみる
list_test_int_and_str = [1,"aaa",2,"bbb"]

# インスタンスをリストに入れてみる
list_instance = List_instance()

list_test_instance = [list_instance, "aaa",1111]

print(list_test_in)
print(list_test_int_and_str)
print(list_test_instance[0].class_aaa)

# インスタンスの値を取り出す
print(list_instance.class_bbb)

prev = ""
for animal in ["cat", "dog", "tiger", "lion", "puma", "horse"]:
    print ("value of animal :", animal)
    prev = prev + animal
    print (prev)
    
print ("This is out of for block")

print("//-------ここまでリスト練習----------//")

# クラスのドキュメントってどうやって書けば良いの？
def HelloWorld():
    """[summary]
    """

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
