import click
import json
from atlassian import Bitbucket
from atlassian import Jira
from atlassian import Confluence

@click.group()
@click.pass_context
def changelog(ctx):
    """Creates a changelog page on Confluence"""
    pass