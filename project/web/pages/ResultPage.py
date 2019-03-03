# coding=utf-8
from selenium.webdriver.common.by import By
from framework.web.pages.BaseWebPage import BaseWebPage


class ResultPage(BaseWebPage):
    """Сlass to work with elements on Result page

    Args:
        locator_type (By): Locator strategy.
        page_locator (str): Unique locator for current page.
        page_name (str): Human readable page name.
    """
    __locator_type__ = By.XPATH
    __page_locator__ = "//div[@id='hdtbSum']"
    __page_name__ = "Search results"

    def __init__(self):
        super(ResultPage, self).__init__(locator_type=self.__locator_type__,
                                         locator=self.__page_locator__,
                                         page_name=self.__page_name__)
