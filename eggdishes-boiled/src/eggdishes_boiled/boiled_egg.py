from eggdishes_core.lib import EggDish
import eggdishes_core


class BoiledEgg(EggDish):
    name = "Boiled Egg"

    def recipe(self):
        return """
1. 卵を常温に戻す
    冷蔵庫から出したばかりの卵はヒビが入りやすいので、10〜20分ほど室温に置きます。
2. 鍋に卵を並べる
    卵同士がぶつからないように注意しながら鍋に並べます。
3. 水を入れる
    卵がしっかり浸るくらいまで水を注ぎます。
4. 火にかける
    中火で加熱し、沸騰させます。
5. 茹で時間を調整する
    沸騰したらタイマーをセット！お好みの仕上がりに合わせて茹で時間を変えます。
    - 半熟（とろとろ）：6〜7分
    - 半熟（ねっとり）：8〜9分
    - 固ゆで（しっかり）：10〜12分
6. 冷水にとる
    茹で上がったらすぐに冷水（または氷水）に移して冷やします。殻がむきやすくなります。
完成！
"""

@eggdishes_core.hookimpl
def register_eggdish(recipes):
    def create():
        return BoiledEgg()
    recipes["boiled"] = create