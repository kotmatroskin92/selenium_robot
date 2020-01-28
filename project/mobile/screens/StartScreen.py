# -*- coding: utf-8 -*-

from appium.webdriver.common.mobileby import MobileBy

from framework.mobile.elements.MobileLabel import MobileLabel
from framework.mobile.elements.MobileTextBox import MobileTextBox
from framework.mobile.screens.MobileScreen import MobileScreen


class StartScreen(MobileScreen):

    def __init__(self):
        super().__init__(MobileBy.ID, "com.app.scr:id/rlToolbarSearch", 'App Start Screen')
        self.btn_search = MobileLabel(MobileBy.ID, 'btn1', 'Search')
        self.txb_car_search = MobileTextBox(MobileBy.ID, "com.app.scr:id/searchTest", 'Search car input field')
        self.lbl_search_msg = MobileTextBox(MobileBy.XPATH, "//searchTest", 'Search car message')

    def get_error_text(self):
        """Method get error text from form

           Returns (str): sign in error text
        """
        return self.lbl_search_msg.get_text()

    def fill_car_search(self, car_name):
        """
        fill the cars's search field
        :param car_name: name of the city
        """
        self.txb_car_search.set_text(car_name)
        return self
