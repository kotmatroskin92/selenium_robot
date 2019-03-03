# coding=utf-8
from framework.utils.ConfigReader import ConfigReader
from framework.web.browser.Browser import Browser


class NavigateSteps:

    @staticmethod
    def navigate_to_main_page():
        """Method opens start url"""
        return Browser.set_url(ConfigReader().get_env_config()['start_url'])
