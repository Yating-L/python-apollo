import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('update_attribute')
@click.argument("feature_id", type=str)
@click.argument("attribute_key", type=str)
@click.argument("old_value", type=str)
@click.argument("new_value", type=str)

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
def cli(ctx, feature_id, attribute_key, old_value, new_value, organism="", sequence=""):
    """Delete an attribute from a feature
    """
    return ctx.gi.annotations.update_attribute(feature_id, attribute_key, old_value, new_value, organism=organism, sequence=sequence)
