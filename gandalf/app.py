import click
from sys import argv
from commands import product

@click.group(help="help text here")
@click.option('--atlassian-username')
@click.option('--atlassian-password')
@click.pass_context
def cli(ctx,atlassian_username,atlassian_password):
    ctx.ensure_object(dict)    
    ctx.obj['ATLASSIAN_USERNAME'] = atlassian_username
    ctx.obj['ATLASSIAN_PASSWORD'] = atlassian_password
   
@cli.command()
def version():
    print("app version here")

cli.add_command(product.product)

if __name__ == '__main__':
    cli()    