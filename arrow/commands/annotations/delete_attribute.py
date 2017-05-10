import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('delete_attribute')
@click.argument("feature_id", type=str)
@click.argument("attribute_key", type=str)
@click.argument("attribute_value", type=str)

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
def cli(ctx, feature_id, attribute_key, attribute_value, organism="", sequence=""):
    """Delete an attribute from a feature
    """
    return ctx.gi.annotations.delete_attribute(feature_id, attribute_key, attribute_value, organism=organism, sequence=sequence)
