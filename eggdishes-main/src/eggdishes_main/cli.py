import click
from eggdishes_core.plugins import register_eggdishes, get_available_recipes, get_recipe

@click.group()
def cli():
    pass

@cli.command(
    "list",
    help="List available egg dish recipes."
)
def list_recipes():
    register_eggdishes()
    available_recipes = get_available_recipes()
    click.echo("Available egg dish recipes:")
    for recipe in available_recipes:
        click.echo(f"- {recipe}")


@cli.command(
    "recipe",
    help="Show the recipe for an egg dish."
)
@click.argument(
    "dish",
    type=str,
    default="fresh",
)
def show_recipe(dish: str):
    register_eggdishes()
    recipe = get_recipe(dish)
    if recipe:
        click.echo(f"Recipe for {recipe.name}:")
        click.echo(recipe.recipe())
    else:
        click.echo(f"No recipe found for {dish}.")