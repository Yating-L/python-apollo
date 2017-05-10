import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('set_translation_start')
@click.argument("feature_id", type=str)
@click.argument("start", type=int)

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
def cli(ctx, feature_id, start, organism="", sequence=""):
    """Set the translation start of a feature
    """
    return ctx.gi.annotations.set_translation_start(feature_id, start, organism=organism, sequence=sequence)
