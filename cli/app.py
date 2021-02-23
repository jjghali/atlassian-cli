import urllib3
import click
import os, sys
from sys import argv

from utils import ConfigurationManager

<<<<<<< HEAD
from commands import product
from commands import component
from commands import releaseNote
from commands import config
from commands import changelog
from commands import stats
=======
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
>>>>>>> 95f2d1b... added better error and warning handling

@click.group(help="Atlassian CLI")
@click.option('--skipssl/--no-skipssl', required=False, default=False, help="Skips ssl validation in case you have certificates issues (not recommended)")
@click.option('--bitbucket-url', required=False, default="", help="Bitbucket URL")
@click.option('--jira-url', required=False, default="", help="Jira URL")
@click.option('--confluence-url', required=False, default="", help="Confluence URL")
@click.option('--username', required=True, default="", help="Username to use for accessing Atlassian products")
@click.option('--password', required=True, default="", help="Password to use for accessing Atlassian products")
@click.pass_context
# TODO: add url validation under commands when they are needed
def cli(ctx, skipssl, bitbucket_url, jira_url, confluence_url, username, password):
    ctx.ensure_object(dict)
    ctx.obj['skipssl'] = not skipssl
    ctx.obj['bitbucket_url'] = bitbucket_url.strip()
    ctx.obj['jira_url'] = jira_url.strip()
    ctx.obj['confluence_url'] = confluence_url.strip()
    ctx.obj['username'] = username.strip()
    ctx.obj['password'] = password.strip()
    pass

@cli.command()
def version():
    """App version"""
    print("app version here")


cli.add_command(changelog)
cli.add_command(config)
cli.add_command(releaseNote)
cli.add_command(product)
cli.add_command(component)
cli.add_command(stats)

if __name__ == '__main__':
    cli()
