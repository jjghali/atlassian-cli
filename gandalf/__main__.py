import click
from sys import argv
# from gandalf import app

@click.group()
def cli():
    pass

@cli.command()
def version():
    print("app version here")

@cli.command(name="product")
def product():    
    print("product infos")
    print()


@cli.command()
def hello():
    """Gandalf app"""

if __name__ == '__main__':
    cli()    