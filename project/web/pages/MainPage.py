# coding=utf-8
from selenium.webdriver.common.by import By
from framework.web.pages.BaseWebPage import BaseWebPage
from framework.web.webelements.Button import Button


class MainPage(BaseWebPage):
    """Сlass to work with elements on Main page

    Args:
        locator_type (By): Locator strategy.
        page_locator (str): Unique locator for current page.
        page_name (str): Human readable page name.
    """
    __locator_type__ = By.XPATH
    __page_locator__ = "//div[@id='viewport']"
    __page_name__ = "Main"

    _btn_search_ = Button(By.XPATH, "//div[contains(@class, 'FPdoLc')]//input[@name='btnK']", "Search")
    _btn_lucky_ = Button(By.XPATH, "//div[contains(@class, 'FPdoLc')]//input[@name='btnI']", "I'm lucky")

    def __init__(self):
        super(MainPage, self).__init__(locator_type=self.__locator_type__,
                                       locator=self.__page_locator__,
                                       page_name=self.__page_name__)

    def click_search_button(self):
        """Method click on search  button"""
        self._btn_search_.click()
