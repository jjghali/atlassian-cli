import click
import json
from atlassian import Bitbucket
from atlassian import Jira
from atlassian import Confluence

bitbucketInstance = {}
jiraInstance = {}


@click.group()
@click.pass_context
def releasenote(ctx):
    pass


@releasenote.command()
@click.pass_context
@click.option('-v', '--version', default=False)
def generate(ctx, version):
    pass
