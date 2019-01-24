# coding=utf-8
from robot.libraries.BuiltIn import BuiltIn

built_in = BuiltIn()


class Asserts(object):

    @staticmethod
    def should_be_true(condition, msg=None):
        built_in.should_be_true(condition, msg)

    @staticmethod
    def should_contain(container, item, values=True, ignore_case=False):
        msg = "{} not contains {}".format(container, item)
        built_in.should_contain(container, item, msg, values, ignore_case)

    @staticmethod
    def should_not_contain(container, item, values=True, ignore_case=False):
        msg = "{} contains {}".format(container, item)
        built_in.should_not_contain(container, item, msg, values, ignore_case)

    @staticmethod
    def should_be_equal(first, second, values=True, ignore_case=False):
        built_in.should_be_equal(first, second, "{} not equal {}".format(first, second), values, ignore_case)

    @staticmethod
    def should_be_equal_as_strings(first, second, values=True, ignore_case=False):
        built_in.should_be_equal_as_strings(first, second, "{} not equal {} as strings".format(first, second), values,
                                            ignore_case)
