import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('delete_sequence_alteration')
@click.argument("feature_id")

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
    """[UNTESTED] Delete a specific feature alteration
    """
    return ctx.gi.annotations.delete_sequence_alteration(feature_id, organism=organism, sequence=sequence)