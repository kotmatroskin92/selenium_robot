# coding=utf-8
from framework.web.webelements.BaseWebElement import BaseWebElement


class Link(BaseWebElement):

    def __init__(self, locator_type, locator, name):
        super(Link, self).__init__(locator_type=locator_type, loc=locator, name_of=name)

    def get_href(self):
        return super(Link, self).get_attribute("href")
