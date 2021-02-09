import click
import pprint36 as pprint
from cli.services import JiraService


@click.group()
# @click.option('-n', '--product-name', default=False)
@click.pass_context
def product(ctx):
    """Get information about a product"""
    context_parent = click.get_current_context(silent=True)
    ctx.ensure_object(dict)
    ctx.obj['skipssl'] = context_parent.obj["skipssl"]

    self.jiraService = JiraService(ctx.obj['skipssl'])
    pass


@product.command()
def list():
    """Lists all the deployed versions of a product"""
    print("lists products")


@product.command()
@click.pass_context
def info():
    """Provides info about a product release"""
    pass


@product.command()
@click.pass_context
def versions(ctx):
    """Lists all the deployed versions of a product"""

    print("lists product versions")
    # print(productName)
    context_parent = click.get_current_context()


@product.command()
@click.pass_context
@click.option('-v', '--product-version', required=True, default=False)
@click.option('--changes/--no-changes', required=False, default=False)
@click.option('--confluence/--no-confluence', required=False, default=False)
def tickets(ctx, product_version, changes, confluence):
    """Lists all components of a product"""

    product_version = product_version.strip()
    versionInfo = jiraService.get_default_project_version_infos(
        product_version)

    if confluence:
        confMarkup = jiraService.get_default_issues_confluence_markup(
            versionInfo["id"])
        print(confMarkup)
    else:
        output = "\nId: {0}\nName: {1}\nDescription: {2}\nReleased: {3}\nStart date: {4}\nRelease date: {5}\n"

        if versionInfo is not None:
            print("test")
            print(output.format(
                versionInfo["id"],
                versionInfo["name"],
                versionInfo["description"],
                versionInfo["released"],
                versionInfo["startDate"],
                versionInfo["releaseDate"]))

        if changes:
            output = jiraService.get_issues_printable(versionInfo["id"])
            print(output)


@product.command()
@click.pass_context
def info(ctx):
    """Displays info about a product"""

    print("product info here")
