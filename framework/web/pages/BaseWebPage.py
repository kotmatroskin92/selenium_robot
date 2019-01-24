from framework.web.browser.Browser import Browser
from framework.web.webelements.Label import Label


class BaseWebPage:
    def __init__(self, locator_type, locator, page_name):
        self.locator = locator
        self.page_name = page_name
        self.locator_type = locator_type

    def wait_page_is_load(self):
        Browser.wait_for_page_is_load()

    def is_opened(self):
        self.wait_page_is_load()
        return Label(self.locator_type, self.locator, self.page_name).is_present_with_wait()

    def wait_for_page_closed(self):
        self.wait_page_is_load()
        Label(self.locator_type, self.locator, self.page_name).wait_for_is_absent()

    def wait_for_page_opened(self):
        self.wait_page_is_load()
        Label(self.locator_type, self.locator, self.page_name).wait_for_is_present()
