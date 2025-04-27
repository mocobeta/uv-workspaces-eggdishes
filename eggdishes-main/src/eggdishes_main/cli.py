import click
from eggdishes_core.fresh_egg import FreshEgg
from eggdishes_boiled.boiled_egg import BoiledEgg
from eggdishes_poached.poached_egg import PoachedEgg
from eggdishes_scrambled.scrambled_egg import ScrambledEgg
from eggdishes_sunnysideup.sunnysideup_egg import SunnysideUpEgg

@click.group()
def cli():
    pass

@cli.command(
    "recipe",
    help="Show the recipe for an egg dish."
)
@click.argument(
    "dish",
    type=click.Choice(["boiled", "poached", "scrambled", "sunnysideup", "fresh"]),
    default="fresh",
)
def show_recipe(dish: str):
    """Show the recipe for a fresh egg dish."""
    egg_dish = None
    if dish == "boiled":
        egg_dish = BoiledEgg()
    elif dish == "poached":
        egg_dish = PoachedEgg()
    elif dish == "scrambled":
        egg_dish = ScrambledEgg()
    elif dish == "sunnysideup":
        egg_dish = SunnysideUpEgg()
    else:
        egg_dish = FreshEgg()
    click.echo(f"Recipe for {egg_dish.name}:")
    click.echo(egg_dish.recipe())

