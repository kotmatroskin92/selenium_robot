# -*- coding: utf-8 -*-
from appium.webdriver import Remote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class MobileDriver:
    """
    Class wrapper for web driver (appium or selenium)
    """

    driver = None

    def __init__(self, driver=Remote, dr_mobile=None):
        self.driver = driver(**dr_mobile)
        self.action_chains = ActionChains(self.driver)
        self.driver_wait = WebDriverWait

    def __getattr__(self, name):
        return getattr(self.driver, name)
