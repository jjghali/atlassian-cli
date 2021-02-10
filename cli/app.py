import urllib3
import click
import os, sys
from sys import argv

from utils import ConfigurationManager

from commands import product
from commands import component
from commands import releaseNote
from commands import config
from commands import changelog
from commands import stats

@click.group(help="Atlassian CLI")
@click.option('--skipssl/--no-skipssl', required=False, default=False, help="Skips ssl validation in case you have certificates issues (not recommended)")
@click.option('--bitbucket-url', required=True, default="", help="Bitbucket URL")
@click.option('--jira-url', required=True, default="", help="Jira URL")
@click.option('--confluence-url', required=True, default="", help="Confluence URL")
@click.option('--username', required=True, default="", help="Username to use for accessing Atlassian products")
@click.option('--password', required=True, default="", help="Password to use for accessing Atlassian products")
@click.pass_context
def cli(ctx, skipssl, bitbucket_url, jira_url, confluence_url, username, password):
    ctx.ensure_object(dict)
    ctx.obj['skipssl'] = not skipssl
    ctx.obj['bitbucket_url'] = bitbucket_url
    ctx.obj['jira_url'] = jira_url
    ctx.obj['confluence_url'] = confluence_url
    ctx.obj['username'] = username
    ctx.obj['password'] = password
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
