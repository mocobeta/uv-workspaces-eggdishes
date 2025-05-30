from eggdishes_core.lib import EggDish
import eggdishes_core

class SunnysideUpEgg(EggDish):
    name = "Sunny Side Up Egg"

    def recipe(self):
        return """
1. フライパンを温める
    中火でフライパンを軽く温め、油かバターを入れて広げます。
2. 卵をそっと割り入れる
    黄身が割れないように優しく！できれば小さい器に一度割ってからフライパンへ流し込むと安心。
3. 弱火にして水を加える
    卵の白身が広がったら、すぐに火を弱火にしてフライパンの端から水を加えます。
4. すぐふたをする
    加えた水が蒸気になって卵を包み込みます。ふたをして、約1〜2分蒸し焼きに。
5. 様子を見ながら火を止める
    白身が固まって、黄身がまだぷるんぷるんしていたらOK！
    早めに火を止めて余熱で少しだけ火を通すと、絶妙な半熟に仕上がります。
6. 塩・こしょうで味付けする
完成！
"""

@eggdishes_core.hookimpl
def register_eggdish(recipes):
    def create():
        return SunnysideUpEgg()
    recipes["sunnysideup"] = create