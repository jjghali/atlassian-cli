import click
import json
from services import ConfluenceService


@click.group()
@click.pass_context
def releasenote(ctx):
    """Creates a release note one on Confluence"""
    pass


@releasenote.command()
@click.option('-v', '--version', required=True, default="")
@click.option('-s', '--space-key', required=True, default="")
@click.option('-p', '--project-key', required=True, default="")
@click.option('-i', '--parent-page-id', required=True, default="")
@click.option('-t', '--template-file', required=True, default="")
@click.option('--create-page/--no-create-page', required=False, default=True)
def generate(version, space_key, project_key, parent_page_id, template_file, create_page):
    version = version.strip()
    project_key = project_key.strip()
    space_key = space_key.strip()
    parent_page_id = parent_page_id.strip()

    confluence_service = ConfluenceService()
    releasenote = confluence_service.generate_releasenote(project_key, version)

    if create_page:
        if space_key is not None or parent_page_id is not None:
            confluence_service.push_releasenote(
                space_key, version, parent_page_id, releasenote)

        else:
            print("ERROR: Missing space-key or parent-page-id options.")
    else:
        print(releasenote)
