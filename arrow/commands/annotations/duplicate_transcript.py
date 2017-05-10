import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('duplicate_transcript')
@click.argument("transcript_id", type=str)

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
def cli(ctx, transcript_id, organism="", sequence=""):
    """Duplicate a transcripte
    """
    return ctx.gi.annotations.duplicate_transcript(transcript_id, organism=organism, sequence=sequence)
