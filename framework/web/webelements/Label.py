# coding=utf-8
from framework.web.webelements.BaseWebElement import BaseWebElement


class Label(BaseWebElement):

    def __init__(self, locator_type, locator, name):
        super(Label, self).__init__(locator_type=locator_type, loc=locator, name_of=name)
