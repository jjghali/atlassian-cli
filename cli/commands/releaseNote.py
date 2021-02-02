import click
import json
from services import ConfluenceService


@click.group()
@click.pass_context
def releasenote(ctx):
    """Creates a release note one on Confluence"""
    pass


@releasenote.command()
# @click.pass_context
@click.option('-v', '--version', default=False)
@click.option('-p', '--project-key', default=False)
@click.option('--storage-format/--no-storage-format', required=False, default=False)
def generate(version, project_key, storage_format):
    version = version.strip()
    project_key = project_key.strip()

    confluenceService = ConfluenceService()
    confluenceService.generate_releasenote(project_key, version)
    pass
