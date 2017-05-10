import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('addValue')
@click.argument("value")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, value, metadata=""):
    """TODO: Undocumented
    """
    return ctx.gi.cannedvalues.addValue(value, metadata=metadata)
