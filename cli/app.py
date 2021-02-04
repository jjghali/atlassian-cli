import click
import os
from sys import argv

from commands import product
from commands import component
from commands import releasenote
from commands import config
from commands import changelog


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


cli.add_command(config)
cli.add_command(releasenote)
cli.add_command(product)
cli.add_command(component)
cli.add_command(changelog)

if __name__ == '__main__':
    cli()
