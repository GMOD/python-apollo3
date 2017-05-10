import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('get_comments')
@click.argument("feature_id", type=str)

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
def cli(ctx, feature_id, organism="", sequence=""):
    """Get a feature's comments
    """
    return ctx.gi.annotations.get_comments(feature_id, organism=organism, sequence=sequence)