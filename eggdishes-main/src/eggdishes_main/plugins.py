from eggdishes_core.lib import EggDish
from eggdishes_core import hookspecs
from eggdishes_core import fresh_egg

import pluggy

__recipes = {}  # Registry of egg dish recipes

def __get_plugin_manager():
    # プラグインマネージャーを取得
    pm = pluggy.PluginManager("eggdishes")
    # hookspec(プラグインのインターフェース)を登録
    pm.add_hookspecs(hookspecs)
    # 環境内のプラグインをロード
    pm.load_setuptools_entrypoints("eggdishes")
    # fresh_eggはeggdishes_core内で定義されているので，明示的に登録する
    pm.register(fresh_egg)
    return pm


def register_eggdishes():
    """Register available recipes to the registry."""
    pm = __get_plugin_manager()
    # 環境内のすべてのプラグインフックを呼び出す
    for recipe in pm.hook.register_eggdish(recipes=__recipes):
        if recipe:
            __recipes[recipe.name] = recipe


def get_available_recipes():
    """Return a list of available egg dish recipes."""
    return __recipes.keys()


def get_recipe(name) -> EggDish | None:
    """Return the recipe for the given egg dish name."""
    recipe = __recipes.get(name)
    if recipe:
        return recipe()
    return None

