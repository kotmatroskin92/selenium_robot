from framework.web.webelements.Label import Label


class BaseWebForm:
    def __init__(self, locator_type, locator, form_name):
        self.locator = locator
        self.form_name = form_name
        self.locator_type = locator_type

    def is_opened(self):
        return Label(self.locator_type, self.locator, self.form_name).is_present_with_wait()

    def wait_for_form_closed(self):
        Label(self.locator_type, self.locator, self.form_name).wait_for_is_absent()

    def wait_for_form_opened(self):
        Label(self.locator_type, self.locator, self.form_name).wait_for_is_present()
