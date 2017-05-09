import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('loadGroup')
@click.argument("group")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, group):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.loadGroup(group)