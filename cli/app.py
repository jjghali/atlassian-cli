import urllib3
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import os
import sys
import inspect
from sys import argv
from utils import ConfigurationManager
from commands import product, component, releaseNote, auth, changelog, repo


currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


confManager = ConfigurationManager()


@click.group(help="Atlassian CLI",
             cls=HelpColorsGroup,
             help_headers_color='yellow',
             help_options_color='green')
@click.pass_context
# TODO: add url validation under commands when they are needed
def cli(ctx):
    ctx.ensure_object(dict)

    # if not confManager.is_config_valid():
    #     sys.exit("ERROR: You have not configured the CLI. run atlcli auth login first.")
    pass


@cli.command()
def version():
    """App version"""
    print("app version here")


cli.add_command(auth)
cli.add_command(product)
cli.add_command(component)
cli.add_command(repo)

if __name__ == '__main__':
    cli()
