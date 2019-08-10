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

class Player:

    def __init__(self,player_name): 
        # インスタンス変数
        self.name = ""
        self.hund = []
        self.point = 0
        self.win_flg = False

class Dealer:

    def _init_(self):
        self.name = ""
        self.hund = []
        self.point = 0
        self.result = ""

class GameControler:

    resurt_text = ""

    def __init__(self,player,dealer,cards): 

        # 初回の山札を作成
        cards.create_card_deck()

        # 初回ドロー
        cards.drow_card_for_deck(2,player)
        cards.drow_card_for_deck(2,player)

        cards.drow_card_for_deck(2,dealer)
        cards.drow_card_for_deck(2,dealer)

        print("プレイヤー手札" + str(player.hund) + "ポイント" + str(player.point))
        print("ディーラー手札" + str(dealer.hund) + "ポイント" + str(dealer.point))

    def burst_check(self,user):

        BERST_POINT = 21
        GAME_OVER_POINT = 99

        if(user.point > BERST_POINT):

            print("ゲームオーバー")

            user.point = GAME_OVER_POINT

            self.resurt_text = "あなたの負け"
            # バースト = true
            return True

        return False

    def resurt_process(self,user,dealer):

        pass






    def yes_no_select(self):
        yesNo = input()
        print('y / n' + yesNo)

        # self.gamestatus.hund.append(yesNo)

        # pythonのIF文は文字列の場合は==かinを使って比較する
        if yesNo in "y":
            print ("y")
            return True

        elif yesNo in "n":
            print ("n")
            return False

        return False

    def turn_process(self,player,dealer,cards):

        # プレイヤーが1枚引く
        cards.drow_card_for_deck(2,player)

        # バースト判定
        if(self.burst_check(player)):

            print("結果を記入")


        # ディーラーが17点以上になるまで引く
        if(dealer.point < 17):

            cards.drow_card_for_deck(2,dealer)

        # バースト判定
        self.burst_check(dealer)

        print("現在の得点を表示")
        print("プレイヤー手札" + str(player.hund) + "ポイント" + str(player.point))
        print("ディーラー手札" + str(dealer.hund) + "ポイント" + str(dealer.point))

        # プレイヤーがコールするか引くかを聞く
        print("もう1枚ドローしますか？")
        if(self.yes_no_select()):

            print("")
            # コールなら結果を発表
            return True

        return False

        

    def game_over(self,player):
        pass


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

            Player.hund.append(draw_card)

            print(Player.hund)
            
            print("ここまでドロー処理")

            card_point = draw_card.split((","))

            Player.point += int(card_point[0])

            return random_number

    def point_calc(self):

        print("ここに例外ポイントを計算する")


# プレイヤーとディーラーを作成
player = Player("あなた")
dealer = Player("ディーラー")
# トランプを用意
cards = Cards()
# 山札を作成
cards.create_card_deck()

# ゲームをセットアップ
gc = GameControler(player,dealer,cards)

# ターンをゲームが終わるまで繰り返す
while gc.turn_process(player,dealer,cards):
    pass

print("ここで結果発表")
# 結果発表の処理をまとめる
print("あなたのポイント：" + str(player.point) + "ディーラーのポイント" + str(dealer.point))

# クラス作って処理を分ける？コントローラーにずらす？
if(player.point == 99 or dealer.point == 99):
    print("バーストしたので負け")

if(player.point > dealer.point):
    print("プレイヤーの勝ち")
else:
    print("ディーラーの勝ち")










