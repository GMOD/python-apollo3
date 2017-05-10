import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('set_boundaries')
@click.argument("feature_id", type=str)
@click.argument("start", type=int)
@click.argument("end", type=int)

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
def cli(ctx, feature_id, start, end, organism="", sequence=""):
    """Set the boundaries of a genomic feature
    """
    return ctx.gi.annotations.set_boundaries(feature_id, start, end, organism=organism, sequence=sequence)