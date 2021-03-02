import os, sys
import click
import pprint36 as pprint
from services import JiraService
skipssl = False


@click.group()
@click.pass_context
def product(ctx):    
    """Displays infos about a product"""
    context_parent = click.get_current_context(silent=True)
    ctx.ensure_object(dict)    
    ctx.obj['jira_url'] = context_parent.obj["jira_url"]    
    ctx.obj['username'] = context_parent.obj["username"]
    ctx.obj['password'] = context_parent.obj["password"]
    skipssl = context_parent.obj["skipssl"]
    pass

@product.command()
@click.pass_context
@click.option('-v', '--product-version', required=True, default=False)
@click.option('-j', '--project-key', required=True, default=False)
def info(ctx, product_version, project_key):
    """Provides info about a product release"""
    pass

@product.command()
@click.pass_context
def versions(ctx):
    """Lists all the deployed versions of a product"""
    print("lists product versions")
    # print(productName)
    context_parent = click.get_current_context()
    pass

@product.command()
@click.pass_context
@click.option('-v', '--product-version', required=True, default=False)
@click.option('-j', '--project-key', required=True, default=False)
@click.option('--changes/--no-changes', required=False, default=False)
@click.option('--confluence/--no-confluence', required=False, default=False)
def tickets(ctx, product_version, project_key, changes, confluence):
    """Lists all components of a product"""
    jira_service = JiraService(
        ctx.obj['jira_url'], ctx.obj['username'], ctx.obj['password'], ctx.obj['skipssl'])

    product_version = product_version.strip()
    versionInfo = jira_service.get_project_version_infos(project_key,
                                                        product_version)

    if confluence:
        confMarkup = jira_service.get_issues_confluence_markup(project_key,
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
            output = jira_service.get_issues_printable(versionInfo["id"])
            print(output)


@product.command()
@click.pass_context
def info(ctx):
    """Displays info about a product"""

    print("product info here")

@product.command()
@click.pass_context
@click.option('-v', '--version', required=False, default="", help="Specify version if you want statistics about a version.")
@click.option('-j', '--project-key', required=True, default="", help="Project key used in your Jira project.")
@click.option('--json/--no-json', required=False, default=False, help="Provides stats in json format.")
def stats(ctx, version, project_key, json):
    """Displays statistics about a product"""
    jira_service = JiraService(
            ctx.obj['jira_url'], ctx.obj['username'], ctx.obj['password'], ctx.obj['skipssl'])
    result = jira_service.get_deploy_frequency(project_key)
    print(result)
    
    if version is not None:
        leadtime = jira_service.get_leadtime_for_changes_per_version(project_key,version)
        s_lead_time = "Version: {0}\nLead time for changes: {1}".format(version, leadtime)
        print(s_lead_time)
    

