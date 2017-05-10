import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('set_symbol')
@click.argument("feature_id", type=str)
@click.argument("symbol", type=str)

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
def cli(ctx, feature_id, symbol, organism="", sequence=""):
    """Set a feature's description
    """
    return ctx.gi.annotations.set_symbol(feature_id, symbol, organism=organism, sequence=sequence)