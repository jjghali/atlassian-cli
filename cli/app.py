import click
import os
from sys import argv

from commands import product
from commands import component
from commands import releasenote
from commands import config
from commands import changelog


@click.group(help="help text here")
@click.option('--proxy', required=False, default=None)
@click.pass_context
def cli(ctx, proxy):
    if proxy:
        os.environ['http_proxy'] = proxy
        os.environ['HTTP_PROXY'] = proxy
        os.environ['https_proxy'] = proxy
        os.environ['HTTPS_PROXY'] = proxy

    ctx.ensure_object(dict)


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
