import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('delete_features')
@click.argument("organism_id", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, organism_id):
    """Remove features of an organism
    """
    return ctx.gi.organisms.delete_features(organism_id)