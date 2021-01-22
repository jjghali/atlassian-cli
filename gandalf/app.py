import click
from sys import argv
from commands import product
from commands import component

@click.group(help="help text here")
@click.option('--bitbucket-url')
@click.option('--jira-url')
@click.option('--atlassian-username')
@click.option('--atlassian-password')
@click.pass_context
def cli(ctx,bitbucket_url, jira_url, atlassian_username,atlassian_password):
    ctx.ensure_object(dict)    
    ctx.obj['BITBUCKET_URL'] = bitbucket_url
    ctx.obj['JIRA_URL'] = jira_url
    ctx.obj['ATLASSIAN_USERNAME'] = atlassian_username
    ctx.obj['ATLASSIAN_PASSWORD'] = atlassian_password
   
@cli.command()
def version():
    print("app version here")

cli.add_command(product.product)
cli.add_command(component.component)

if __name__ == '__main__':
    cli()    