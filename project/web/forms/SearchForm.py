# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from framework.web.pages.BaseWebForm import BaseWebForm
from framework.web.webelements.TextBox import TextBox


class SearchForm(BaseWebForm):
    """Сlass to work with elements on Search form

    Args:
        locator_type (By): Locator strategy.
        form_locator (str): Unique locator for current form.
        form_name (str): Human readable form name.
    """

    __locator_type__ = By.XPATH
    __form_locator__ = "//div[@id='searchform']"
    __form_name__ = "Search"
    _txb_query_field_ = TextBox(By.XPATH, "//input[@name='q']", "Search query field")

    def __init__(self):
        super(SearchForm, self).__init__(locator_type=self.__locator_type__,
                                         locator=self.__form_locator__,
                                         form_name=self.__form_name__)

    def type_search_query(self, value):
        """Method implements type test_data value to query field"""
        self._txb_query_field_.send_keys(value)
        self._txb_query_field_.send_keys(Keys.RETURN)

    def get_search_query(self):
        """Method implements get search query value"""
        return self._txb_query_field_.get_value()
