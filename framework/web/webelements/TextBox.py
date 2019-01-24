# coding=utf-8
from selenium.webdriver.common.keys import Keys
from framework.web.webelements.BaseWebElement import BaseWebElement


class TextBox(BaseWebElement):
    def __init__(self, locator_type, locator, name):
        super(TextBox, self).__init__(locator_type=locator_type, loc=locator, name_of=name)

    def get_value(self):
        return super(TextBox, self).get_attribute("value")

    def clear_field(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)
