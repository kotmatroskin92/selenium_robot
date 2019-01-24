# coding=utf-8
import os

from configuration import configuration
from configuration.configuration import ENV
from framework.utils.JSONHandler import JSONHandler


class ConfigReader:
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ENV_BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                 'configuration', 'environments', '{0}')
    LOCALE_BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                    'configuration', 'locale', '{0}', 'dictionary.json')

    def get_data(self, path_to_json):
        return JSONHandler.read_from_file(path_to_json.format(ENV))

    def get_env_variable(self, name, default=None):
        from robot.libraries.BuiltIn import BuiltIn
        prepared_name = '${' + name + '}'
        variables = BuiltIn().get_variables()
        return variables[prepared_name] if prepared_name in variables else default

    def get_env(self):
        return self.get_env_variable('ENV', configuration.ENV)

    def get_locale(self):
        return self.get_env_variable('LOCALE', configuration.LOCALE)

    def get_browser(self):
        return self.get_env_variable('BROWSER', configuration.BROWSER)

    def get_headless(self):
        return self.get_env_variable('HEADLESS', configuration.HEADLESS)

    def get_env_base_path(self):
        return self.ENV_BASE_PATH.format(self.get_env())

    def get_locale_dict(self):
        dict_path = self.LOCALE_BASE_PATH.format(self.get_locale())
        return self.get_data(dict_path)

    def get_env_config(self):
        config_path = os.path.join(self.get_env_base_path(), "config.json")
        return self.get_data(config_path)

    def get_env_test_data(self):
        config_path = os.path.join(self.get_env_base_path(), "test_data.json")
        return self.get_data(config_path)
