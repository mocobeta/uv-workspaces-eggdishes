from .lib import EggDish

class FreshEgg(EggDish):
    name = "採れたて卵"

    def recipe(self):
        return "ご飯に新鮮な卵とかつお節をのせて、醤油をかけて召し上がれ！"