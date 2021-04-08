from os import remove
from os.path import expanduser
import yaml
import base64


class ConfigurationManager:
    DEFAULT_CONFIG_FILE_PATH = expanduser("~")+"/.gdlf_config.yml"

    def load_config(self):
        try:
            with open(self.DEFAULT_CONFIG_FILE_PATH) as file:
                data = yaml.safe_load(file, Loader=yaml.FullLoader)
            return data
        except IOError:
            return None

    def create_config(self, data):
        with open(self.DEFAULT_CONFIG_FILE_PATH, 'w') as file:
            yaml.dump(data, file)

    def delete_config(self):
        remove(self.DEFAULT_CONFIG_FILE_PATH)

    def is_config_valid(self):
        try:
            with open(self.DEFAULT_CONFIG_FILE_PATH) as file:
                data = yaml.load(file, Loader=yaml.FullLoader)

                return True
        except IOError:
            return False

    # TODO: Add App password retrieval if possible
