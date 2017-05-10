import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('delete_organism')
@click.argument("organism_id", type=str)


@pass_context
@apollo_exception
@list_output
def cli(ctx, organism_id):
    """Delete an organim
    """
    return ctx.gi.organisms.delete_organism(organism_id)
