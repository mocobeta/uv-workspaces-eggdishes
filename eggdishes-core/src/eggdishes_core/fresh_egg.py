from .lib import EggDish
import eggdishes_core

class FreshEgg(EggDish):
    name = "採れたて卵"

    def recipe(self):
        return "ご飯に新鮮な卵とかつお節をのせて、醤油をかけて召し上がれ！"


@eggdishes_core.hookimpl
def register_eggdish(recipes):
    def create():
        return FreshEgg()
    recipes["fresh"] = create