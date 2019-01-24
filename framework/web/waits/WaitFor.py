# coding=utf-8
from selenium.common.exceptions import StaleElementReferenceException
from framework.web.scripts import ScriptsJs

COMPLETE = 'complete'


class WaitForReadyStateComplete(object):

    def __init__(self, browser):
        self.browser = browser

    def __call__(self, driver):
        try:
            return self.browser.execute_script(ScriptsJs.GET_PAGE_READY_STATE) == COMPLETE
        except StaleElementReferenceException:
            return False


class WaitForTrue(object):
    def __init__(self, browser, expression):
        self.browser = browser
        self.expression = expression

    def __call__(self, driver):
        try:
            return self.expression()
        except Exception:
            return False
