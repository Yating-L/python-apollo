import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('update_user')
@click.argument("email", type=str)
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
@click.argument("password", type=str)

@click.option(
    "--metadata",
    help="User metadata",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, email, first_name, last_name, password, metadata={}):
    """Update an existing user
    """
    return ctx.gi.users.update_user(email, first_name, last_name, password, metadata=metadata)
