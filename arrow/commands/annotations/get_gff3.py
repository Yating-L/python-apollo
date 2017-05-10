import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('get_gff3')
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
    """Get the GFF3 associated with a feature
    """
    return ctx.gi.annotations.get_gff3(feature_id, organism=organism, sequence=sequence)