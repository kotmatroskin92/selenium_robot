# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from framework.mobile.driver.MobileDriver import MobileDriver
from framework.mobile.elements.MobileElement import MobileElement
from framework.robotwrappers.RobotLogger import RobotLogger


class MobileScreen:
    DIV_HEIGHT_FOR_RIGHT_SWIPE = 2
    SUB_WIDTH_FOR_RIGHT_SWIPE = 1
    Y_OFFSET_FOR_RIGHT_SWIPE = 0
    DIV_WIDTH_FOR_UP_SWIPE = 2
    DIV_HEIGHT_FOR_UP_SWIPE = 2
    SUB_HEIGHT_FOR_UP_SWIPE = 1
    Y_OFFSET_FOR_UP_SWIPE = 0
    DIV_WIDTH_FOR_DOWN_SWIPE = 2
    DIV_HEIGHT_FOR_DOWN_SWIPE = 2
    SUB_HEIGHT_FOR_DOWN_SWIPE = 100
    Y_OFFSET_FOR_DOWN_SWIPE = 0
    START_X_FOR_SWIPE_DOWN_TO_ELEMENT = 700
    START_Y_FOR_SWIPE_DOWN_TO_ELEMENT = 2000
    X_OFFSET_FOR_SWIPE_DOWN_TO_ELEMENT = 0
    Y_OFFSET_FOR_SWIPE_DOWN_TO_ELEMENT = 700

    def __init__(self, locator_type, locator, name=None):
        self.driver = MobileDriver.driver
        self.locator_type = locator_type
        self.locator = locator
        self.name = name if name else locator
        MobileElement(self.locator_type, self.locator, self.name).find_element()
        RobotLogger.info("Page '{0}' was opened".format(self.name))

    def get_page_width(self):
        """
        :return: width of the page
        """
        return self.driver.get_window_size()['width']

    def get_page_height(self):
        """
        :return: height of the page
        """
        return self.driver.get_window_size()['height']

    def scroll_page_down(self):
        """
        scroll page down to the bottom
        :return:
        """
        self.driver.execute_script("mobile: scroll", {"direction": 'down'})
        return self

    def scroll_page_up(self):
        """
        scroll page up to the bottom
        :return:
        """
        self.driver.execute_script("mobile: scroll", {"direction": 'up'})
        return self

    def swipe_right(self, coordinate_y=None):
        """
        swipe from the right side to the left
        """
        RobotLogger.info('Swiping from the right side to the left')
        start_x = self.get_page_width() - self.SUB_WIDTH_FOR_RIGHT_SWIPE
        if not coordinate_y:
            coordinate_y = round(self.get_page_height() / self.DIV_HEIGHT_FOR_RIGHT_SWIPE)
        self.swipe(start_x, coordinate_y, -start_x, self.Y_OFFSET_FOR_RIGHT_SWIPE)
        return self

    def swipe_up(self, silent=False):
        """
        swipe from bottom to up
        :param silent: true - log message isn't displayed, false - log message is displayed
        """
        if not silent:
            RobotLogger.info('Swiping from bottom to up')
        horizontal_middle = round(self.get_page_width() / self.DIV_WIDTH_FOR_UP_SWIPE)
        start_y, finish_y = self.get_srart_y_finish_y(self.DIV_HEIGHT_FOR_UP_SWIPE, self.SUB_HEIGHT_FOR_UP_SWIPE)
        return self.swipe(horizontal_middle, start_y, self.Y_OFFSET_FOR_UP_SWIPE, finish_y)

    def swipe_down(self, silent=False):
        """
        swipe from up to bottom
        :param silent: true - log message isn't displayed, false - log message is displayed
        """
        if not silent:
            RobotLogger.info('Swiping from up to bottom')
        horizontal_middle = round(self.get_page_width() / self.DIV_WIDTH_FOR_DOWN_SWIPE)
        start_y, finish_y = self.get_srart_y_finish_y(self.DIV_HEIGHT_FOR_DOWN_SWIPE, self.SUB_HEIGHT_FOR_DOWN_SWIPE)

        return self.swipe(horizontal_middle, start_y, self.Y_OFFSET_FOR_DOWN_SWIPE, finish_y)

    def get_srart_y_finish_y(self, div_param, sum_param):
        return round(self.get_page_height() / div_param), \
               self.get_page_height() - sum_param

    def swipe(self, start_x, start_y, x_offset, y_offset):
        """
        swipe page and catch exception if it appears.
        appium issue https://github.com/appium/appium/issues/7572
        :param start_x: x coordinate to start swipe
        :param start_y: y coordinate to start swipe
        :param x_offset: x coordinate to swipe right (>0) or left (<0) from start_x
        :param y_offset: y coordinate to swipe down (>0) or up (<0) from start_y
        """
        try:
            self.driver.swipe(start_x, start_y, x_offset, y_offset)
        except WebDriverException:
            RobotLogger.info("Swipe failed the first time because of WebDriverAgent error. Trying to swipe again")
            self.driver.swipe(start_x, start_y, x_offset, y_offset)
        return self

    def swipe_down_to_element(self, element):
        while not element.is_present():
            try:
                self.swipe(self.START_X_FOR_SWIPE_DOWN_TO_ELEMENT,
                           self.START_Y_FOR_SWIPE_DOWN_TO_ELEMENT,
                           self.X_OFFSET_FOR_SWIPE_DOWN_TO_ELEMENT,
                           self.Y_OFFSET_FOR_SWIPE_DOWN_TO_ELEMENT)
            except WebDriverException:
                RobotLogger.info("Swipe failed the first time because of WebDriverAgent error. Trying to swipe again")
        return element
