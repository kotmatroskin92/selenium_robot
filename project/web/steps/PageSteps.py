# coding=utf-8
from framework.robotwrappers.Asserts import Asserts
from project.web.pages.ResultPage import ResultPage
from project.web.pages.MainPage import MainPage


class PageSteps:

    @staticmethod
    def main_page_is_opened():
        """Method assert is Main page opened"""
        is_page_opened = MainPage().is_opened()
        Asserts.should_be_true(is_page_opened, 'Main page has not been opened')

    @staticmethod
    def result_page_is_opened():
        """Method assert is Result page opened"""
        is_page_opened = ResultPage().is_opened()
        Asserts.should_be_true(is_page_opened, 'Result page has not been opened')
