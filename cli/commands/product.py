import click
import pprint36 as pprint
from prettytable import PrettyTable
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
@click.option('--confluence/--no-confluence', required=False, default=False)
def tickets(ctx, product_version, changes, confluence):
    """Lists all components of a product"""

    versionInfo = jiraInstance.get_project_version_infos(product_version)

    if confluence:
        confMarkup = jiraInstance.printConfluenceMarkup(versionInfo["id"])
        print(confMarkup)
    else:
        output = "\nId: {0}\nName: {1}\nDescription: {2}\nReleased: {3}\nStart date: {4}\nRelease date: {5}\n"
        if versionInfo is not None:
            print(output.format(
                versionInfo["id"],
                versionInfo["name"],
                versionInfo["description"],
                versionInfo["released"],
                versionInfo["startDate"],
                versionInfo["releaseDate"]))

        if changes:
            issues = jiraInstance.get_project_version_issues(versionInfo["id"])
            printIssues(issues)


@product.command()
@click.pass_context
def info(ctx):
    """Displays info about a product"""

    print("product info here")


def printIssues(issues):
    table = PrettyTable()
    table.field_names = ["Key", "Repositories", "Status"]
    for x in issues:
        repositories = jiraInstance.get_repositories_from_issue(x["id"])
        concatRepos = ""
        # for r in repositories:
        #     concatRepos + r["name"] + " "
        if len(repositories) > 0:
            table.add_row([x["key"], repositories[0]["name"],
                           x["fields"]["status"]["name"]])
        else:
            table.add_row([x["key"], "None",
                           x["fields"]["status"]["name"]])
    print("----------Issues----------")
    print(table)
