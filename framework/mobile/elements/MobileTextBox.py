# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from framework.mobile.elements.MobileElement import MobileElement
from framework.robotwrappers.RobotLogger import RobotLogger


class MobileTextBox(MobileElement):
    def __init__(self, locator_type, locator, name=None, scroll=False):
        super().__init__(locator_type, locator, name, scroll)

    def set_text(self, text, skip_if_none=True, close_keyboard=False):
        """
        clear the text field and type new text
        catch exception if it appears (appium issue https://github.com/appium/appium/issues/7572)
        :param text: text that should be set
        :param skip_if_none: true - do nothing if text isn't specified, set text if it specified
        false - set text if it specified, error if text isn't specified
        :param close_keyboard: true - close keyboard after setting text, false - don't close keyboard
        native appium methods for closing keyboard doesn't work properly on iOS, so it's necessary to scroll page up
        """
        if self.scroll:
            self.scroll_to_element()
        try:
            self.set_textbox(text, skip_if_none)
        except WebDriverException:
            RobotLogger.info("Set Text failed the first time because of WebDriverAgent error. Trying to set text again")
            self.set_textbox(text, skip_if_none)
        if close_keyboard:
            self.driver.execute_script("mobile: scroll", {"direction": 'up'})
        return self

    def set_textbox(self, text, skip_if_none=True):
        """
        clear the text field and type new text
        :param text: text that should be set
        :param skip_if_none: true - do nothing if text isn't specified, set text if it specified
        false - set text if it specified, error if text isn't specified
        """
        def func(value):
            element = self.find_element()
            element.clear()
            element.set_value(value)
            return True
        if text is None and skip_if_none:
            return self
        RobotLogger.info("Clear text field '{0}' and set text '{1}'".format(self.get_name(), text))
        self.wait_for(func, text)
        return self

    def type_text(self, text):
        """
        type text into the text field
        :param text: text that should be typed
        """
        def func(value):
            self.find_element().send_keys(value)
            return True
        RobotLogger.info("Type text '{0}' into text field '{1}'".format(text, self.get_name()))
        self.wait_for(func, text)
        return self

    def clear_text(self):
        """
        clear text in the text field
        """
        def func():
            self.find_element().clear()
            return True
        self.wait_for(func)
        return self
