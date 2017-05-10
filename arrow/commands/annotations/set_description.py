import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('set_description')
@click.argument("feature_id", type=str)
@click.argument("description", type=str)

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
def cli(ctx, feature_id, description, organism="", sequence=""):
    """Set a feature's description
    """
    return ctx.gi.annotations.set_description(feature_id, description, organism=organism, sequence=sequence)