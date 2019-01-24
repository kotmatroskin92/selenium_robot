from framework.web.browser.Browser import Browser
from framework.web.elements.Label import Label


class BaseWebPage:
    def __init__(self, search_condition, locator, page_name):
        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition

    def wait_page_is_load(self):
        Browser.wait_for_page_is_load()

    def is_opened(self):
        self.wait_page_is_load()
        return Label(self.search_condition, self.locator, self.page_name).is_present_with_wait()

    def wait_for_page_closed(self):
        self.wait_page_is_load()
        Label(self.search_condition, self.locator, self.page_name).wait_for_is_absent()

    def wait_for_page_opened(self):
        self.wait_page_is_load()
        Label(self.search_condition, self.locator, self.page_name).wait_for_is_present()
