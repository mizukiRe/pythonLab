import random

# プログラミング入門者からの卒業試験は『ブラックジャック』を開発すべし
# https://qiita.com/hirossyi73/items/cf8648c31898216312e5
# Pythonの練習としてこの課題をやってみる

# ルール
    # 初期カードは52枚。引く際にカードの重複は無いようにする
    # プレイヤーとディーラーの2人対戦。プレイヤーは実行者、ディーラーは自動的に実行
    # 実行開始時、プレイヤーとディーラーはそれぞれ、カードを2枚引く。引いたカードは画面に表示する。ただし、ディーラーの2枚目のカードは分からないようにする
    # その後、先にプレイヤーがカードを引く。プレイヤーが21を超えていたらバースト、その時点でゲーム終了
    # プレイヤーは、カードを引くたびに、次のカードを引くか選択できる
    # プレイヤーが引き終えたら、その後ディーラーは、自分の手札が17以上になるまで引き続ける
    # プレイヤーとディーラーが引き終えたら勝負。より21に近い方の勝ち
    # JとQとKは10として扱う
    # Aはとりあえず「1」としてだけ扱う。「11」にはしない
    # ダブルダウンなし、スプリットなし、サレンダーなし、その他特殊そうなルールなし


# 初回処理、プレイヤー2枚ドロー、ディーラー2枚ドロー（2枚目は非公開）
# ターンの処理、(1)プレイヤーのドロー、(2)カードの確認、(3)ディーラーのドロー、(4)カードの確認
# プレイヤーは引いた後に、次のカードを引くか選ぶ（y / n)
# ディーラーは手札が17枚以上になるまで引き続ける
# 22以上でバースト（敗北）
# コールした場合21に近いほうが勝ち

print("Hello world")

# input()でインプットを呼び出し
class GameStatus:

    def __init__(self): 
        self.name = ""
        self.hund = []
        self.point = 0

class Player:

    def __init__(self,player_name): 
        # インスタンス変数
        self.gamestatus = GameStatus()

class Dealer:

    def _init_(self):
        self.gamestatus = GameStatus()

class Game:

    # コンストラクタでゲームのセットアップを行う
    # プレイヤー2枚ドロー、ディーラー2枚ドロー
    def __init__(self): 
        # インスタンス変数
        player = Player("あなた")
        dealer = Player("ディーラー")
        cards = Cards()

        # 初回の山札を作成
        cards.create_card_deck()

        # 初回ドロー
        cards.drow_card_for_deck(2,player)
        cards.drow_card_for_deck(2,player)

        cards.drow_card_for_deck(2,dealer)
        cards.drow_card_for_deck(2,dealer)

        print("プレイヤー手札" + str(player.gamestatus.hund) + "ポイント" + str(player.gamestatus.point))
        print("ディーラー手札" + str(dealer.gamestatus.hund) + "ポイント" + str(dealer.gamestatus.point))

    def turn_process(self):

        print("現在の得点を表示")
 
        # プレイヤーが1枚引く

        # バースト判定

        # ディーラーが17点以上になるまで引く

        # バースト判定

        # プレイヤーがコールするか引くかを聞く

        # コールなら結果を発表

    def add_mul(self,x, y):
        return (x + y, x * y)

    def berst_check(self,point):
        BURST_POINT = 21

        if(BURST_POINT < point):
            print("【★バースト★】")
            return False

        return True

    def yes_no_select(self):
        yesNo = input()
        print('y / n' + yesNo)

        # self.gamestatus.hund.append(yesNo)

        # pythonのIF文は文字列の場合は==かinを使って比較する
        if yesNo in "y" or yesNo in "n":
            print ("おーけー")
        else:
            print ("ダメダメじゃん")



class Cards:
    """トランプの管理を行う
    """

    CARD_NUMBER_LIST = {1,2,3,4,5,6,7,8,9,10,11,12,13}

    CARD_MARK_LIST = {"ハート","ダイア","スペード","クローバー"}

    # 山札
    deck = []

    def create_card_deck(self):
        """カードナンバーとカードマークから山札を作成する
        """
        for cMark in self.CARD_MARK_LIST:

            for cNumber in self.CARD_NUMBER_LIST:

                self.deck.append(str(cNumber) + "," + cMark)

    def drow_card_for_deck(self, number, Player):

        for i in range(1,number):

            print("ここからドロー処理")

            print(len(self.deck))

            random_number = random.randrange(len(self.deck))

            print(list(range(len(self.deck))))

            print(random.randrange(len(self.deck)))
            
            draw_card = self.deck.pop(random_number)

            print("引いたカード→" + draw_card)

            Player.gamestatus.hund.append(draw_card)

            print(Player.gamestatus.hund)
            
            print("ここまでドロー処理")

            card_point = draw_card.split((","))

            Player.gamestatus.point += int(card_point[0])

            return random_number

    def point_calc(self):

        print("ここに例外ポイントを計算する")

#ここにナンバーとマークでトランプのセットを作る
#機能拡張でトランプ追加したいから、頑張って追加できるように作る

# ドロー処理は、デッキの最大数を引数にランダムで数字生成してデッキからPOPで取得する
game = Game()

# print(game.Player.gamestatus.hand)



# ターンの進行


#ドローしたカードは配列から消す
# del( index )を使って消せばOK

# 試しに消してみる
# del deck[1]

# # popを使えば、削除と値の保持を同時にできる
# # 指定したインデックスの要素を削除して、要素を返します。
# # 引数を指定しない場合、リストの末尾の要素を削除します。
# print(deck.pop(3))

# #ドロー処理は配列の要素数を最大値とする乱数を生成して、インデックスのカードを取り出して、消去する
# # 山札枚数一定以下（ルール調べて）で山札を補充する
# print(deck)







