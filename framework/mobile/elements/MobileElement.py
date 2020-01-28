# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.configuration import WAIT_ELEMENT_SECONDS
from framework.mobile.driver.MobileDriver import MobileDriver
from framework.robotwrappers.RobotLogger import RobotLogger


class MobileElement:

    def __init__(self, locator_type, locator, name=None, scroll=False):
        self.__driver = MobileDriver.driver
        self.scroll = scroll
        self.__locator_type = locator_type
        self.__locator = locator
        self.__name = name or locator

    def get_locator(self):
        return self.__locator

    def get_locator_type(self):
        return self.__locator_type

    def get_name(self):
        return self.__name

    def get_driver(self):
        return self.__driver

    def click(self, visible=False):
        """
        scroll page to element and click it
        :param visible: true - click only visible element that is currently on the screen,
        false - click any found element;
        visible=True can be used if there are several elements with identical locators, but not all of them are visible,
        if visible=True method takes more time
        """
        def func():
            element = self.get_first_visible_element() if visible else self.find_element()
            element.click()
            return True
        if self.scroll:
            self.scroll_to_element()
        RobotLogger.info("Click '{0}'".format(self.get_name()))
        self.wait_for(func)

    def scroll_to_element(self):
        """
        scroll page to element
        check that element location is within screen height
        and is_displayed work correctly (case when element located on screen but is_displayed return false)
        """
        element = self.find_element()
        if not (self.get_driver().get_window_size()['height'] > element.location['y'] > 0
                and not element.is_displayed()) or element.is_displayed():
            RobotLogger.info("scroll to element '{0}''".format(self.get_name()))
            self.get_driver().execute_script("mobile: scroll", {"element": element, "toVisible": True})

    def get_rect(self, visible=False):
        """
        get size (x and y) of the element
        :param visible: true - click only visible element that is currently on the screen,
        false - click any found element;
        visible=True can be used if there are several elements with identical locators, but not all of them are visible,
        if visible=True method takes more time
        """
        def func():
            element = self.get_first_visible_element() if visible else self.find_element()
            return element.rect
        return self.wait_for(func)

    def swipe_element_right(self, silent=False, start_x_offset=-1):
        """
        swipe from right border of element to left.
        :param silent: true - log message isn't displayed, false - log message is displayed
        :param start_x_offset: offset from start_x coordinate
        """
        if not silent:
            RobotLogger.info('Swiping element {0} from right to left'.format(self.get_name()))
        rect = self.get_rect()
        vertical_middle = round(rect['y'] + rect['height'] / 2)
        start_x = rect['x'] + rect['width'] + start_x_offset
        self.get_driver().swipe(start_x, vertical_middle, -rect['width'], 0)
        return self

    def swipe_element_up(self, silent=False, start_y_offset=1):
        if not silent:
            RobotLogger.info('Swiping element {0} from upper border to the lower border'.format(self.get_name()))
        rect = self.get_rect()
        horizontal_middle = round(rect['x'] + rect['width'] / 2)
        start_y = rect['y'] + start_y_offset
        self.get_driver().swipe(horizontal_middle, start_y, 0, rect['height'])
        return self

    def swipe_element_down(self, silent=False, start_y_offset=-1):
        if not silent:
            RobotLogger.info('Swiping element {0} from lower border to the upper border'.format(self.get_name()))
        rect = self.get_rect()
        horizontal_middle = round(rect['x'] + rect['width'] / 2)
        start_y = rect['y'] + rect['height'] + start_y_offset
        self.get_driver().swipe(horizontal_middle, start_y, 0, - rect['height'])
        return self

    def get_value(self):
        """
        get element attribute "value"
        :return attribute "value"
        """
        def func():
            return self.find_element().get_attribute("value")
        return self.wait_for(func)

    def get_text(self):
        """
        get element attribute "text"
        :return attribute "text"
        """
        def func():
            return self.find_element().get_attribute("text")
        return self.wait_for(func)

    def get_label(self):
        """
        get element attribute "label"
        """
        def func():
            return self.find_element().get_attribute("label")
        return self.wait_for(func)

    def get_count(self):
        """
        get count of elements with specified locator
        """
        return len(self.get_all_elements())

    def get_first_visible_element(self):
        """
        get fist visible element that is't outside of the screen
        """
        page_size = self.get_driver().get_window_size()
        elements = self.get_all_elements()
        for element in elements:
            if 0 < element.location['x'] < page_size['width'] and 0 < element.location['y'] < page_size['height']:
                return element
        return None

    def get_all_elements(self):
        """
        get list of elements by locator
        """
        def func():
            elements = self.get_driver().find_elements(self.get_locator_type(), self.get_locator())
            if len(elements) > 0:
                return elements
            return None
        return self.wait_for(func)

    def click_first_element(self):
        """
        wait for element present and click it
        Fix for appium bug when find_element not found element but find_elements return correct result
        """
        RobotLogger.info("Click '{0}'".format(self.get_name()))
        element = self.get_all_elements()[0]
        element.click()

    def is_enabled(self):
        """
        :return: true if element enabled, false if element disabled
        """
        def funс():
            return self.find_element().is_enabled()
        return self.wait_for(funс)

    def is_present(self):
        """
        :return: true if element is present, false if element is absent
        """
        try:
            return self.get_count() > 0
        except TimeoutException:
            return False

    def is_visible(self):
        """
        :return: true if at least one visible element with specified locator is present on the page,
         false if there are not visible elements
        """
        return self.get_first_visible_element() is not None

    def wait_element_without_error(self, silent=False, second=10):
        """
        wait for element present
        method doesn't throw error if element absent after specified timeout, test continues
        method is necessary for elements that appear and disappear unpredictably (e.g. loader)
        :param silent: true - log message isn't displayed, false - log message is displayed
        :param second: number of seconds to wait till element appears
        """
        if not silent:
            RobotLogger.info("Wait for '{0}' present".format(self.get_name()))
        end_time = time.time() + second
        while time.time() < end_time and not self.is_present():
            pass
        return self

    def wait_element_absent(self, silent=False, second=WAIT_ELEMENT_SECONDS):
        """
        wait for element absent
        :param silent: true - log message isn't displayed, false - log message is displayed
        :param second: number of seconds after which test will wail if element is absent
        """
        if not silent:
            RobotLogger.info("Wait for '{0}' absent".format(self.get_name()))
        self.wait_for_check_by_condition(method_to_check=EC.invisibility_of_element_located,
                                         message=" already exists", wait_time_sec=second)

    def find_element(self):
        element = self.wait_for_check_by_condition(method_to_check=EC.presence_of_element_located,
                                                   message=" was not found")
        return element

    def wait_for_check_by_condition(self, method_to_check, message, wait_time_sec=WAIT_ELEMENT_SECONDS,
                                    use_default_msg=True):
        try:
            element = WebDriverWait(self.get_driver(), wait_time_sec).\
                until(method=method_to_check((self.get_locator_type(), self.get_locator())))
        except TimeoutException:
            result_message = ("Element '" + self.get_name() + "' with locator " + self.get_locator() + message
                              if use_default_msg else message)
            RobotLogger.warning(result_message)
            raise TimeoutException(result_message)
        return element

    def wait_for(self, condition, *args, **kwargs):
        def func(driver):
            value = condition(*args, **kwargs)
            return value
        return WebDriverWait(self.get_driver(), WAIT_ELEMENT_SECONDS).until(func)
