# coding=utf-8
from framework.utils.TestDataReader import TestDataReader
from framework.robotwrappers.Asserts import Asserts
from project.web.forms.SearchForm import SearchForm
from project.web.pages.MainPage import MainPage


class SearchSteps:
    @staticmethod
    def click_search():
        """Method click search button."""
        MainPage().click_search_button()

    @staticmethod
    def type_in_query_field(data_path_string):
        """Method type in search query field from test_data."""
        query_value = TestDataReader().read_test_data(data_path_string)
        SearchForm().type_search_query(query_value)

    @staticmethod
    def search_query_is_displayed(data_path_string):
        """Method type in search query field from test_data."""
        expected_search_result = TestDataReader().read_test_data(data_path_string)
        actual_search_result = SearchForm().get_search_query()
        Asserts.should_be_equal(expected_search_result, actual_search_result)
