from os.path import expanduser
import pprint36 as pprint
import click
import yaml

DEFAULT_CONFIG_FILE_PATH = expanduser("~")+"/.gdlf_config.yml"


@click.command()
def config():
    """Configure Gandalf for local use."""
    dict_file = dict()
    credentials = dict()
    dict_file["bitbucket"] = "bitbucket-url"
    dict_file["jira"] = "jira-url"
    dict_file["confluence"] = "confluence-url"
    credentials["username"] = "username-atlassian"
    credentials["password"] = "password-atlassian"
    dict_file["credentials"] = credentials
    create_config(DEFAULT_CONFIG_FILE_PATH, dict_file)
    load_config(DEFAULT_CONFIG_FILE_PATH)


def load_config(config_file):
    with open(config_file) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        pprint.pp(data)


def create_config(config_file, data):
    with open(config_file, 'w') as file:
        yaml.dump(data, file)
