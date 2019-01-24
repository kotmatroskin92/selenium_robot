# coding=utf-8
from selenium.common.exceptions import NoSuchWindowException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait

from configuration import configuration
from framework.utils.ConfigReader import ConfigReader
from framework.robotwrappers.RobotLogger import RobotLogger
from framework.web.browser.BrowserFactory import BrowserFactory
from framework.web.waits.waitfor import WaitForReadyStateComplete
from framework.web.waits.waitfor import WaitForTrue


class Browser:
    __web_driver = None
    __main_window_handle = None

    @staticmethod
    def get_driver():
        return Browser.__web_driver

    @staticmethod
    def set_up_driver():
        RobotLogger.info('Browser initialisation for ' + ConfigReader().get_browser())
        Browser.__web_driver = BrowserFactory.get_browser_driver()
        Browser.__web_driver.implicitly_wait(configuration.IMPLICIT_WAIT_TIMEOUT)
        Browser.__web_driver.set_page_load_timeout(configuration.PAGE_LOAD_TIMEOUT)
        Browser.__web_driver.set_script_timeout(configuration.SCRIPT_TIMEOUT)
        Browser.__main_window_handle = Browser.__web_driver.current_window_handle

    @staticmethod
    def quit():
        if Browser.get_driver() is not None:
            RobotLogger.info("Quit browser")
            Browser.get_driver().quit()
            Browser.__web_driver = None
        else:
            RobotLogger.info("Browser is not exist")

    @staticmethod
    def close(page_name=""):
        if Browser.get_driver() is not None:
            RobotLogger.info("Close %s browser tab" % page_name)
            Browser.get_driver().close()

    @staticmethod
    def refresh_page():
        RobotLogger.info("Page refresh")
        Browser.get_driver().refresh()

    @staticmethod
    def maximize():
        RobotLogger.info("Maximize window")
        Browser.get_driver().maximize_window()

    @staticmethod
    def set_url(url):
        RobotLogger.info("Change page url to %s" % url)
        Browser.get_driver().get(url)

    @staticmethod
    def execute_script(script, arguments=None):
        if arguments is None:
            arguments = []
        return Browser.get_driver().execute_script(script, arguments)

    @staticmethod
    def get_current_url():
        return Browser.get_driver().current_url

    @staticmethod
    def back_page():
        Browser.get_driver().back()

    @staticmethod
    def switch_to_window(window_handle):
        RobotLogger.info("Switch to window with name %s" % window_handle)
        try:
            Browser.get_driver().switch_to_window(window_handle)
        except NoSuchWindowException:
            RobotLogger.error("No matching window %s found" % window_handle)

    @staticmethod
    def switch_main_window():
        RobotLogger.info("Switch to main window")
        try:
            Browser.get_driver().switch_to_window(Browser.__main_window_handle)
        except NoSuchWindowException:
            RobotLogger.error("Main window not found")

    @staticmethod
    def switch_new_window(page_name=""):
        RobotLogger.info("Switch to new window %s" % page_name)
        handles = Browser.get_driver().window_handles
        if len(handles) <= 1:
            raise NoSuchWindowException("New window is absent. Windows amount = %s" % len(handles))
        Browser.get_driver().switch_to_window(handles[-1])

    @staticmethod
    def switch_to_frame(frame_name):
        RobotLogger.info("Switch to frame with name %s" % frame_name)
        Browser.get_driver().switch_to_frame(frame_name)

    @staticmethod
    def get_alert():
        RobotLogger.info("Switch to alert")
        try:
            return Browser.get_driver().switch_to_alert()
        except NoAlertPresentException:
            RobotLogger.info("Alert window not found")
            return None

    @staticmethod
    def accept_alert_if_exist():
        RobotLogger.info("Accept alert if exist")
        alert = Browser.get_alert()
        if alert is not None:
            alert.accept()
            RobotLogger.info("Alert accepted")

    @staticmethod
    def get_alert_text():
        RobotLogger.info("Get alert text")
        alert = Browser.wait_for_true(Browser.get_alert)
        return alert.text

    @staticmethod
    def switch_to_default_content():
        RobotLogger.info("Switch to default frame")
        Browser.get_driver().switch_to_default_content()

    @staticmethod
    def wait_for_page_is_load():
        WebDriverWait(Browser.get_driver(), configuration.PAGE_LOAD_TIMEOUT).until(WaitForReadyStateComplete(Browser))

    @staticmethod
    def disable_implicit_wait():
        Browser.set_implicit_wait(0)

    @staticmethod
    def set_implicit_wait(wait_time_sec=configuration.IMPLICIT_WAIT_TIMEOUT):
        Browser.__web_driver.implicitly_wait(wait_time_sec)

    @staticmethod
    def wait_for_true(expression, time_in_seconds=configuration.IMPLICIT_WAIT_TIMEOUT, msg=""):
        try:
            return WebDriverWait(Browser.get_driver(), time_in_seconds).until(WaitForTrue(Browser, expression))
        except TimeoutException:
            error_msg = "During {time} seconds action was not made: {msg}".format(time=time_in_seconds,
                                                                                  msg=msg)
            RobotLogger.error(error_msg)
            raise TimeoutException(error_msg)
