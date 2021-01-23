from os.path import expanduser
import yaml


class ConfigurationManager:
    DEFAULT_CONFIG_FILE_PATH = expanduser("~")+"/.gdlf_config.yml"

    def __init__(self):
        pass

    def load_config(self):
        with open(self.DEFAULT_CONFIG_FILE_PATH) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data

    def create_config(self, data):
        credentials = "{username}:{password}".format(username = data["credentials"]["username"],
            password = data["credentials"]["password"])
        data["credentials"]["base64"] = base64.b64encode(credentials)
        
        with open(self.DEFAULT_CONFIG_FILE_PATH, 'w') as file:
            yaml.dump(data, file)
