import click
import pprint36 as pprint
from services import JiraService

jiraInstance = JiraService()


@click.group()
# @click.option('-n', '--product-name', default=False)
@click.pass_context
def product(ctx):
    """Get information about a product"""
    context_parent = click.get_current_context()
    ctx.ensure_object(dict)


@product.command()
def list():
    """Lists all the deployed versions of a product"""
    print("lists products")


@product.command()
@click.pass_context
def versions(ctx):
    """Lists all the deployed versions of a product"""

    print("lists product versions")
    # print(productName)
    context_parent = click.get_current_context()


@product.command()
@click.pass_context
@click.option('-v', '--product-version', default=False)
@click.option('--changes/--no-changes', required=False, default=False)
def tickets(ctx, product_version, changes):
    """Lists all components of a product"""
    if product_version is not None:
        result = jiraInstance.get_project_version_issues(product_version)
        pprint.pp(result)
    else:
        pass
    print("lists products components")


@product.command()
@click.pass_context
def info(ctx):
    """Displays info about a product"""

    print("product info here")
