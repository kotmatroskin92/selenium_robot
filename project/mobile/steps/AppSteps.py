# -*- coding: utf-8 -*-
from framework.utils.TestDataReader import TestDataReader
from project.mobile.screens.StartScreen import StartScreen
from framework.robotwrappers.Asserts import Asserts


class AppSteps:

    @staticmethod
    def search_car(data_path_string):
        car = TestDataReader().read_test_data(data_path_string)
        StartScreen().fill_car_search(car)
        StartScreen().btn_search.click()

    @staticmethod
    def message_is_displayed(data_path_string):
        """Method assert message."""
        expected_error_text = TestDataReader().read_locale_dict(data_path_string)
        actual_error_text = StartScreen().get_error_text()
        Asserts.should_be_equal(expected_error_text, actual_error_text)
