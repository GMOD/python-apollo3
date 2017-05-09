import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setStatus')
@click.argument("statuses")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, statuses):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setStatus(statuses)