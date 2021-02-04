import click
import json
from services import ConfluenceService

skipssl = False


@click.group()
@click.pass_context
def changelog(ctx):
    """Creates a changelog page on Confluence"""
    context_parent = click.get_current_context(silent=True)
    ctx.ensure_object(dict)
    skipssl = context_parent.obj["skipssl"]
    pass
