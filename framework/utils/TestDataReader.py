# coding=utf-8
import dpath.util

from framework.utils.ConfigReader import ConfigReader
from framework.robotwrappers.RobotLogger import RobotLogger


class TestDataReader(object):
    LOCALE = 'locale'
    TEST_DATA = 'test_data'

    def __get_dict_value__(self, data_dict, dot_sep_path, separator='.', raise_key_error=True):
        try:
            return dpath.util.get(data_dict, dot_sep_path, separator)
        except KeyError as e:
            if raise_key_error:
                RobotLogger.error('Error "{}" during reading dict. Dot_sep_path: {}. Dict: {}'.format(e, dot_sep_path,
                                                                                                      data_dict))
            else:
                return None

    def read_data(self, full_data_path_string, data_type, raise_key_error=True):
        starts_with = '@'
        if not full_data_path_string.startswith(starts_with):
            RobotLogger.error('Incorrect data string: {}. Data should starts with: {}'.format(full_data_path_string,
                                                                                              starts_with))
        data_path_string = full_data_path_string.replace(starts_with, '')
        data_dict = {}

        if data_path_string.split('.')[0] == self.LOCALE:
            data_dict = ConfigReader().get_locale_dict()
        elif data_path_string.split('.')[0] == self.TEST_DATA:
            data_dict = ConfigReader().get_env_test_data()
        else:
            RobotLogger.error('Unknown data type: {}.'.format(data_path_string))

        return self.__get_dict_value__(data_dict, data_path_string.replace(data_type, ''),
                                       raise_key_error=raise_key_error)

    def read_locale_dict(self, full_data_path_string, raise_key_error=True):
        return self.read_data(full_data_path_string, self.LOCALE, raise_key_error=raise_key_error)

    def read_test_data(self, full_data_path_string, raise_key_error=True):
        return self.read_data(full_data_path_string, self.TEST_DATA, raise_key_error=raise_key_error)
