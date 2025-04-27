import click
from eggdishes_core.fresh_egg import FreshEgg

@click.group()
def cli():
    pass

@cli.command(
    "recipe",
    help="Show the recipe for an egg dish."
)
def show_recipe():
    """Show the recipe for a fresh egg dish."""
    egg_dish = FreshEgg()
    click.echo(f"Recipe for {egg_dish.name}:")
    click.echo(egg_dish.recipe())

