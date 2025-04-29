from eggdishes_core.lib import EggDish
import eggdishes_core

class PoachedEgg(EggDish):
    name = "Poached Egg"

    def recipe(self):
        return """
1. 鍋に水を張り、火にかける
    鍋にたっぷり水を入れ、中火で温めます。（グラグラ沸騰させない。80〜90℃くらいが理想）
2. 酢を加える
    水に酢を加えます。酢を入れると卵白がまとまりやすくなります。（味にはほぼ影響しません）
3. 卵を割り入れる
    別の器に卵を割っておきます。（直接割り入れると形が崩れやすいので）
4. 水をぐるぐる回して渦を作る
    スプーンや菜箸で鍋の水をぐるぐるかき混ぜ、渦を作ります。その渦の中心に卵をそっと落とします。
5. 弱火で3分ほど加熱
    白身がまとまり、黄身が半熟になったらOK。火加減は「静かにクツクツ」くらいをキープします。
6. すくい上げて水気を切る
    おたまや穴あきスプーンでそっとすくい上げ、キッチンペーパーなどで水気を取ります。
完成！
"""

@eggdishes_core.hookimpl
def register_eggdish(recipes):
    def create():
        return PoachedEgg()
    recipes["poached"] = create