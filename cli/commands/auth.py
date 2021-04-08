from click_help_colors import HelpColorsGroup, HelpColorsCommand
from utils import ConfigurationManager
import click

confManager = ConfigurationManager()


@click.group(cls=HelpColorsGroup,
             help_headers_color='yellow',
             help_options_color='green')
def auth():
    pass


@auth.command()
def login():
    """Login to your Atlassian products."""
    dict_file = dict()
    credentials = dict()
    bitbucket_url = ""
    jira_url = ""
    confluence_url = ""

    click.echo("This is the initial setup for Atlassian CLI")
    click.echo("We will ask you a bunch of questions in order to setup your CLI.")

    is_cloud = click.confirm(
        'Are you using a Cloud instance? Cloud instances contains *.atlassian.net in the URL', abort=True)

    if not is_cloud:
        click.echo("We will now ask you for ")
        is_bitbucket = click.confirm('Do you have a Bitbucket instance?')
        is_jira = click.confirm('Do you have a Jira instance?')
        is_confluence = click.confirm('Do you have a Confluence instance?')

        if is_bitbucket:
            bitbucket_url = click.prompt('Please enter the URL for Bitbucket')

        if is_jira:
            jira_url = click.prompt('Please enter the URL for Bitbucket')

        if is_confluence:
            confluence_url = click.prompt('Please enter the URL for Bitbucket')

        if not is_confluence and not is_jira and not is_bitbucket:
            click.echo("Setup aborted. You need to enter at least one URL")
    else:
        atlassian_url = click.prompt(
            'Please enter the URL for your Atlassian product (companyname.atlassian.net):')

    username = click.prompt('Please enter the username:')
    password = click.prompt('Please enter the password:', hide_input=True)

    skipssl = click.confirm(
        'Do you wish to skip SSL validation? It is recommended to not skip it for security reasons', default=False)

    dict_file["cloud"] = is_cloud

    if not is_cloud:
        dict_file["bitbucket-url"] = bitbucket_url.strip()
        dict_file["jira-url"] = jira_url.strip()
        dict_file["confluence-url"] = confluence_url.strip()
    else:
        dict_file["atlassian-url"] = atlassian_url

    credentials["username"] = username.strip()
    credentials["password"] = password.strip()
    dict_file["credentials"] = credentials
    dict_file["verifyssl"] = skipssl

    confManager.create_config(dict_file)
    confManager.is_config_valid()


@auth.command()
def logout():
    """Logout from your Atlassian products."""
    click.echo("Logging you out...")
    confManager.delete_config()
    click.echo("You are now logged out.")
