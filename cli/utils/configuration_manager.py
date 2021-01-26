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
        with open(self.DEFAULT_CONFIG_FILE_PATH, 'w') as file:
            yaml.dump(data, file)
