import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand


@click.group(cls=HelpColorsGroup,
             help_headers_color='yellow',
             help_options_color='green')
@click.pass_context
def repo(ctx):
    pass


@repo.command()
@click.pass_context
@click.argument('reponame')
def create(ctx, reponame):
    """Create a repository"""
    click.echo("Name of the repo to create: {0}".format(reponame))


@repo.command()
@click.pass_context
@click.argument('reponame')
def clone(ctx, reponame):
    """Clone a repository"""
    click.echo("Name of the repo {0}".format(reponame))


@repo.command()
@click.pass_context
@click.option('-p', '--project', required=False, default="", help="")
def list(ctx, reponame):
    """List repositories owned by a user or a project"""
    click.echo("Name of the repo {0}".format(reponame))


@repo.command()
@click.pass_context
@click.argument('reponame')
def info(ctx, reponame):
    """Info for a repository"""
    click.echo("Name of the repo {0}".format(reponame))
