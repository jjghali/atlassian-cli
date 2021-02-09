import click
import os
from sys import argv

from cli.commands import product
from cli.commands import component
from cli.commands import releaseNote
from cli.commands import config
from cli.commands import changelog


@click.group(help="help text here")
@click.option('--skipssl/--no-skipssl', default=False)
@click.pass_context
def cli(ctx, skipssl):
    ctx.ensure_object(dict)
    ctx.obj['skipssl'] = not skipssl
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

if __name__ == '__main__':
    cli()
