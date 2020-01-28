# coding=utf-8
import random
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration import configuration
from configuration.configuration import EXPLICIT_WAIT_TIMEOUT, IS_EXIST_TIMEOUT
from framework.robotwrappers.RobotLogger import RobotLogger
from framework.web.browser.Browser import Browser
from framework.web.scripts import ScriptsJs


class BaseWebElement(object):
    coordinate_x = 'x'
    coordinate_y = 'y'

    def __init__(self, locator_type, loc, name_of):
        self.__locator_type = locator_type
        self.__locator = loc
        self.__name = name_of

    def __getitem__(self, key):
        if self.__locator_type != By.XPATH:
            raise TypeError("__getitem__ for BaseElement possible only when __search_condition == By.XPATH")
        else:
            return BaseWebElement(By.XPATH, self.__locator + "[" + str(key) + "]", self.__name)

    def get_locator(self):
        return self.__locator

    def get_locator_type(self):
        return self.__locator_type

    def get_name(self):
        return self.__name

    def find_element(self):
        element = self.wait_for_check_by_condition(method_to_check=EC.presence_of_element_located,
                                                   message=" was not found")
        return element

    @staticmethod
    def get_displayed_elements(condition, locator):
        element_size = len(Browser.get_driver().find_elements(condition, locator))
        result_elements = []
        try:
            for ele_number in range(1, element_size + 1):
                element_locator = "({locator})[{number}]".format(locator=locator, number=ele_number)
                RobotLogger.info("Searching element with locator %s" % element_locator)
                element = WebDriverWait(Browser.get_driver(), EXPLICIT_WAIT_TIMEOUT).until(
                    EC.visibility_of_element_located((condition, element_locator)))
                result_elements.append(element)
        except TimeoutException:
            error_msg = "element was not found"
            RobotLogger.error(error_msg)
            raise TimeoutException(error_msg)
        return result_elements

    def is_enabled(self):
        def func():
            return self.find_element().is_enabled()
        RobotLogger.info("Element %s is_enabled()" % self.get_name())
        return self.wait_for(func)

    def is_disabled(self):
        def func():
            return self.find_element().is_disabled()
        RobotLogger.info("Element %s is_disabled()" % self.get_name())
        return self.wait_for(func)

    def is_selected(self):
        def func():
            return self.find_element().is_selected()
        RobotLogger.info("Element %s is_selected()" % self.get_name())
        return self.wait_for(func)

    def is_displayed(self):
        def func():
            return self.find_element().is_displayed()
        RobotLogger.info("Element %s is_displayed()" % self.get_name())
        return self.wait_for(func)

    def is_present(self):
        RobotLogger.info("Element %s is_present()" % self.get_name())
        return self.get_elements_count() > 0

    def is_visible(self):
        RobotLogger.info("Element %s is_visible()" % self.get_name())
        return self.is_displayed()

    def get_elements_count(self):
        elements_count = len(self.get_elements())
        return elements_count

    def get_elements(self):
        def func():
            return Browser.get_driver().find_elements(self.__locator_type, self.__locator)
        Browser.wait_for_page_is_load()
        Browser.set_implicit_wait(configuration.IS_PRESENT_IMPLICIT_TIMEOUT)
        elements = self.wait_for(func)
        Browser.set_implicit_wait()
        return elements

    def get_rnd_element(self):
        elements = self.get_elements()
        element = elements[random.randint(0, len(elements) - 1)]
        return element

    def get_elements_text(self):
        return [elem.text for elem in self.get_elements()]

    def get_element_contains_text(self, text):
        return next((elem for elem in self.get_elements() if text in elem.text), None)

    def get_displayed_element(self):
        elements = self.get_elements()
        return next((elem for elem in elements if elem.is_displayed()), None)

    def send_keys(self, keys):
        def func(key):
            self.find_element().send_keys(key)
            return True
        RobotLogger.info("Element %s send_keys('%s')" % (self.get_name(), keys))
        self.wait_for(func, keys)

    def click(self):
        def func():
            self.wait_for_check_by_condition(method_to_check=EC.element_to_be_clickable,
                                             message=" doesn't exist or clickable")
            self.find_element().click()
            return True
        RobotLogger.info("Element %s click()" % self.get_name())
        self.wait_for(func)

    def get_text(self):
        def func():
            return self.find_element().text
        RobotLogger.info("Element %s get_text()" % self.get_name())
        return self.wait_for(func)

    def get_text_content(self):
        def func():
            return Browser.get_driver().execute_script("return arguments[0].textContent;", self.find_element())
        return self.wait_for(func)

    def get_attribute(self, attr):
        def func(value):
            return self.find_element().get_attribute(name=value)
        RobotLogger.info("Element %s get_attribute('%s')" % (self.get_name(), attr))
        return self.wait_for(func, attr)

    def get_attribute_class(self):
        return self.get_attribute("class")

    def scroll_by_script(self):
        self.wait_for_is_present()
        RobotLogger.info("Scroll to element '" + self.get_name() + "'")
        Browser.execute_script(ScriptsJs.SCROLL_INTO_VIEW, self.find_element())

    def double_click(self):
        def func():
            ActionChains(Browser.get_driver()).double_click(self.find_element()).perform()
        self.wait_for_is_present()
        RobotLogger.info("Element %s double_click()" % self.get_name())
        self.wait_for(func)

    def move_to_element(self):
        self.wait_for_is_present()
        RobotLogger.info("move_to_element: Move to element '" + self.get_name() + "'")
        ActionChains(Browser.get_driver()).move_to_element(self.find_element()).perform()

    def wait_for_is_present(self):
        self.wait_for_check_by_condition(method_to_check=EC.visibility_of_element_located,
                                         message=" doesn't exist")

    def is_present_with_wait(self):
        try:
            self.wait_for_is_present()
        except TimeoutException:
            return False
        return True

    def wait_for_is_displayed(self):
        Browser.wait_for_true(self.is_displayed)

    def wait_for_is_absent(self):
        Browser.disable_implicit_wait()
        self.wait_for_check_by_condition(method_to_check=EC.invisibility_of_element_located,
                                         message=" already exists", wait_time_sec=IS_EXIST_TIMEOUT)
        Browser.set_implicit_wait()

    def wait_for_element_disappear(self):
        def func():
            return len(self.find_element()) == 0
        self.wait_for(func)

    def wait_for_text(self, text):
        def func(value):
            return value in self.find_element().text
        self.wait_for(func, text)

    def wait_for_value(self, text):
        def func(value):
            return value in self.get_attribute("value")
        self.wait_for(func, text)

    def wait_for_visibility(self):
        self.wait_for(self.is_visible())

    def wait_for_check_by_condition(self, method_to_check, message, wait_time_sec=EXPLICIT_WAIT_TIMEOUT,
                                    use_default_msg=True):
        try:
            element = WebDriverWait(Browser.get_driver(),
                                    wait_time_sec,
                                    ignored_exceptions=[StaleElementReferenceException]).\
                until(method=method_to_check((self.get_locator_type(), self.get_locator())))
        except TimeoutException:
            result_message = ("Element '" + self.get_name() + "' with locator" + self.get_locator() + message
                              if use_default_msg else message)
            RobotLogger.warning(result_message)
            raise TimeoutException(result_message)
        return element

    def get_location(self):
        def func():
            return self.find_element().location
        return self.wait_for(func)

    def get_location_vertical(self):
        def func():
            return self.find_element().location[BaseWebElement.coordinate_y]
        return self.wait_for(func)

    def get_location_horizontal(self):
        def func():
            return self.find_element().location[BaseWebElement.coordinate_x]
        return self.wait_for(func)

    @staticmethod
    def get_list_of_elements_vertical_locations(condition, locator):
        other_elements = BaseWebElement.get_displayed_elements(condition, locator)
        return [element.location[BaseWebElement.coordinate_y] for element in other_elements]

    @staticmethod
    def get_dict_of_elements_vertical_locations_and_text(condition, locator):
        events_time_elements = BaseWebElement.get_displayed_elements(condition, locator)
        events_info = {}
        for element in events_time_elements:
            events_info[element.location[BaseWebElement.coordinate_y]] = element.text
        return events_info

    def wait_for(self, condition, *args, **kwargs):
        def func(driver):
            try:
                value = condition(*args, **kwargs)
                return value
            except StaleElementReferenceException:
                return False
        return WebDriverWait(Browser.get_driver(),
                             EXPLICIT_WAIT_TIMEOUT,
                             ignored_exceptions=[StaleElementReferenceException]).until(func)
