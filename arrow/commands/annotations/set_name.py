import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('set_name')
@click.argument("feature_id", type=str)
@click.argument("name", type=str)

@click.option(
    "--organism",
    help="Organism Common Name",
    type=str
)
@click.option(
    "--sequence",
    help="Sequence Name",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, feature_id, name, organism="", sequence=""):
    """Set a feature's name
    """
    return ctx.gi.annotations.set_name(feature_id, name, organism=organism, sequence=sequence)