# coding=utf-8
from framework.robotwrappers.Asserts import Asserts
from framework.utils.TestDataReader import TestDataReader
from framework.utils.ScreenshotUtils import ScreenshotUtils
from framework.web.browser.Browser import Browser


class CommonSteps:
    @staticmethod
    def setup_driver_steps():
        """Method implements set up driver and maximize window."""
        Browser.set_up_driver()
        Browser.maximize()

    @staticmethod
    def destroy_driver_steps():
        """Method take screenshot and close browser."""
        Browser.accept_alert_if_exist()
        ScreenshotUtils.take_screenshot()
        Browser.quit()

    @staticmethod
    def alert_message_is_displayed(data_path_string):
        """Method assert alert message.

        Args:
            data_path_string(str): Path to value from locale dict"""
        expected_error_text = TestDataReader().read_locale_dict(data_path_string)
        text = Browser.get_alert_text()
        Asserts.should_be_equal(expected_error_text, text)
