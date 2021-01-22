import click
import pprint36 as pprint
import json

from atlassian import Bitbucket
from atlassian import Jira

bitbucketInstance = {}
jiraInstance = {}


@click.group()
@click.option('-n', '--product-name', default=False)
@click.option('-c', '--component-name', default=False)
@click.pass_context
def component(ctx, product_name, component_name):
    context_parent = click.get_current_context()
    ctx.ensure_object(dict)

    ctx.obj['PRODUCT_NAME'] = product_name
    ctx.obj['COMPONENT_NAME'] = component_name
    ctx.obj['BITBUCKET_URL'] = context_parent.obj['BITBUCKET_URL']
    ctx.obj['ATLASSIAN_USERNAME'] = context_parent.obj['ATLASSIAN_USERNAME']
    ctx.obj['ATLASSIAN_PASSWORD'] = context_parent.obj['ATLASSIAN_PASSWORD']


@component.group(chain=True, invoke_without_command=False)
@click.pass_context
@click.option('-v', '--version', default=False)
def release(ctx, release_name):
    bitbucketInstance = {}
    if ctx.obj['BITBUCKET_URL'] is not None:
        bitbucketInstance = Bitbucket(
            url=ctx.obj['BITBUCKET_URL'],
            username=ctx.obj['ATLASSIAN_USERNAME'],
            password=ctx.obj['ATLASSIAN_PASSWORD']
        )

        result = bitbucketInstance.get_project_tags(ctx.obj['PRODUCT_NAME'],
                                                    ctx.obj['COMPONENT_NAME'], release_name)

        tags = result["values"]
        targetTag = next(
            filter(lambda x: x["displayId"] == release_name, tags), None)
        pprint.pp(targetTag)


@release.command()
@click.pass_context
def tasks(ctx):
    print("show tasks here")
