# -*- coding: utf-8 -*-
from framework.mobile.elements.MobileElement import MobileElement


class MobileLabel(MobileElement):
    def __init__(self, locator_type, locator, name=None):
        super().__init__(locator_type, locator, name)
