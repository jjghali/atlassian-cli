import click
import json
import re
import semantic_version
from pretty_tables import PrettyTables
from atlassian import Bitbucket
from atlassian import Jira

bitbucketInstance = {}
jiraInstance = {}


@click.group()
@click.option('-n', '--product-name', default=False)
@click.option('-c', '--component-name', default=False)
@click.pass_context
def component(ctx, product_name, component_name):
    """Get information about a component"""
    context_parent = click.get_current_context()
    ctx.ensure_object(dict)

    ctx.obj['PRODUCT_NAME'] = product_name
    ctx.obj['COMPONENT_NAME'] = component_name
    ctx.obj['BITBUCKET_URL'] = context_parent.obj['BITBUCKET_URL']
    ctx.obj['ATLASSIAN_USERNAME'] = context_parent.obj['ATLASSIAN_USERNAME']
    ctx.obj['ATLASSIAN_PASSWORD'] = context_parent.obj['ATLASSIAN_PASSWORD']


@component.group(chain=True, invoke_without_command=False)
@click.pass_context
@click.option('-v', '--version', default="")
@click.option('--include-unstable/--only-stable', required=False, default=False)
def release(ctx, version, include_unstable):
    bitbucketInstance = {}

    if include_unstable:
        print("")
    else:
        print("")

    ctx.obj['VERSION'] = version
    filterMajorReleases([])
    if False and ctx.obj['BITBUCKET_URL'] is not None:
        bitbucketInstance = Bitbucket(
            url=ctx.obj['BITBUCKET_URL'],
            username=ctx.obj['ATLASSIAN_USERNAME'],
            password=ctx.obj['ATLASSIAN_PASSWORD']
        )

        result = bitbucketInstance.get_project_tags(ctx.obj['PRODUCT_NAME'],
                                                    ctx.obj['COMPONENT_NAME'], version)

        tags = result["values"]
        target_tag = next(
            filter(lambda x: x["displayId"] == version, tags), None)

        previous_tag = getPreviousMajorRelease(tags, target_tag)

        changelog = bitbucketInstance.get_changelog(ctx.obj['PRODUCT_NAME'],
                                                    ctx.obj['COMPONENT_NAME'],
                                                    previous_tag, target_tag, limit=1000)


@release.command()
@click.pass_context
def tasks(ctx):
    headers = ["TASK", "Description", "Status"]
    rows = [
        ["DD-1234", "Description de la tache", "En cours"],
        ["DD-1235", "Description de la tache", "En cours"],
        ["DD-1236", "Description de la tache", "En cours"],
    ]

    table = PrettyTables.generate_table(
        headers=headers,
        rows=rows,
        empty_cell_placeholder="No Data"
    )
    print("Tasks for {product}/{component} {version}\n".format(
        product=ctx.obj["PRODUCT_NAME"],
        component=ctx.obj["COMPONENT_NAME"],
        version=ctx.obj["VERSION"]
    ))

    print(table)


def getPreviousMajorRelease(tags, version):
    filtered_tags = filterMajorReleases(tags)
    previous_release = None
    position = filtered_tags.index(version)

    if position > 0:
        previous_release = filtered_tags[position]
    return previous_release


def filterMajorReleases(tags):
    filtered_tags = []
    pattern = re.compile(
        r"^([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$")
    filtered_tags = list(filter(lambda x: pattern.match(x) is not None, tags))

    return filtered_tags
