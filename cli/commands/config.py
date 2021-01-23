from os.path import expanduser
import click
import yaml

DEFAULT_CONFIG_FILE_PATH = expanduser("~")+"/.gdlf_config.yml"


@click.command()
def config():
    """Configure Gandalf for local use."""
    dict_file = dict()
    credentials = dict()

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
    create_config(DEFAULT_CONFIG_FILE_PATH, dict_file)
    load_config(DEFAULT_CONFIG_FILE_PATH)


def load_config(config_file):
    with open(config_file) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)


def create_config(config_file, data):
    with open(config_file, 'w') as file:
        yaml.dump(data, file)
