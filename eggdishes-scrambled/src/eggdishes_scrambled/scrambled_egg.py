from eggdishes_core.lib import EggDish
import eggdishes_core

class ScrambledEgg(EggDish):
    name = "Scrambled Egg"

    def recipe(self):
        return """
1. 卵をよく溶く
    ボウルに卵を割り入れ、牛乳（または生クリーム）と一緒によく混ぜます。白身と黄身がしっかりなじむように。
2. フライパンにバターを溶かす
    中火より少し弱い火で、バターをゆっくり溶かします。
3. 卵液を流し入れる
    バターが溶けたら卵液を一気に流し入れます。
4. やさしくかき混ぜる
    菜箸やゴムベラで、フライパンの外側から中心に向かってゆっくり混ぜます。
    ※焦らず、火が強すぎないよう注意！
5. 半熟状態で火を止める
    卵が半熟でとろっとしてきたら火を止め、余熱で仕上げます。ふわふわ派はここで止めるのがポイント！
6. 塩・こしょうで味付け
    最後に軽く塩・こしょうをふる
完成！
"""

@eggdishes_core.hookimpl
def register_eggdish(recipes):
    def create():
        return ScrambledEgg()
    recipes["scrambled"] = create