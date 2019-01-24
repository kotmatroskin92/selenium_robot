# coding=utf-8
from robot.libraries.BuiltIn import BuiltIn

built_in = BuiltIn()


class CommonMethods(object):

    @staticmethod
    def set_test_variable(name, *values):
        prepared_name = '${' + name + '}'
        built_in.set_test_variable(prepared_name, *values)

    @staticmethod
    def get_variable_value(name):
        prepared_name = '${' + name + '}'
        return built_in.get_variable_value(prepared_name)
