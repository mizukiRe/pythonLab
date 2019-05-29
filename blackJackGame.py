# プログラミング入門者からの卒業試験は『ブラックジャック』を開発すべし
# https://qiita.com/hirossyi73/items/cf8648c31898216312e5
# Pythonの練習としてこの課題をやってみる

# 初回処理、プレイヤー2枚ドロー、ディーラー2枚ドロー（2枚目は非公開）
# ターンの処理、(1)プレイヤーのドロー、(2)カードの確認、(3)ディーラーのドロー、(4)カードの確認
# プレイヤーは引いた後に、次のカードを引くか選ぶ（y / n)
# ディーラーは手札が17枚以上になるまで引き続ける
# 22以上でバースト（敗北）
# コールした場合21に近いほうが勝ち

print("Hello world")

# input()でインプットを呼び出し
yesNo = input()
print('y / n' + yesNo)

# pythonのIF文は文字列の場合は==かinを使って比較する
if yesNo in "y" or yesNo in "n":
    print ("おーけー")
else:
    print ("ng")

card_number = {1,2,3,4,5,6,7,8,9,10,11,12,13}

card_mark = {"ハート","ダイア","スペード","クローバー"}

#ここにナンバーとマークでトランプのセットを作る
#機能拡張でトランプ追加したいから、頑張って追加できるように作る
deck = []

print(deck)

for cMark in card_mark:
    # print(cNumber)

    for cNumber in card_number:

        deck.append(str(cNumber) + ":::" + cMark)


#ドローしたカードは配列から消す
# del( index )を使って消せばOK

#ドロー処理は配列の要素数を最大値とする乱数を生成して、インデックスのカードを取り出して、消去する
# 山札枚数一定以下（ルール調べて）で山札を補充する
print(deck)







