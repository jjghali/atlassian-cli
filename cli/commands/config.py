
import click
from utils import ConfigurationManager

confManager = ConfigurationManager()

@click.command()
def config():
    """Configure Gandalf for local use."""
    dict_file = dict()
    credentials = dict()
    
    dict_file["product-name"] = click.prompt(
        "Please enter the name of the product", type=str)
    dict_file["project-key"] = click.prompt(
        "Please enter the project key on Jira", type=str)
    dict_file["bitbucket-url"] = click.prompt(
        "Please enter the url for Bitbucket", type=str)
    dict_file["jira-url"] = click.prompt(
        "Please enter the url for Jira", type=str)
    dict_file["confluence-url"] = click.prompt(
        "Please enter the url for Confluence", type=str)
    credentials["username"] = click.prompt(
        "Atlassian username", type=str)
    credentials["password"] = click.prompt(
        "Atlassian password", type=str)
    dict_file["credentials"] = credentials
    
    confManager.create_config(dict_file)    