# -*- coding: utf-8 -*-
import os
from configuration.configuration import COMMAND_EXECUTOR, DEVICE_NAME, VERSION, PLATFORM, NEW_COMMAND_TIMEOUT_SECONDS,\
    AUTOMATION_NAME, NO_RESET
from framework.mobile.driver.MobileDriver import MobileDriver
from framework.utils.ConfigReader import ConfigReader
from framework.utils.ScreenshotUtils import ScreenshotUtils
from framework.robotwrappers.RobotLogger import RobotLogger


class BaseSteps:

    def __init__(self):
        self.driver = None

    def init_driver(self):
        env_reader = ConfigReader()
        app_name = env_reader.get_env_config()['app_name']
        RobotLogger.info("PLATFORM: {platform}\n"
                         "VERSION: {version}\n"
                         "DEVICE_NAME: {device_name}\n"
                         "APP_NAME: {app_name}".format(platform=PLATFORM,
                                                       version=VERSION,
                                                       device_name=DEVICE_NAME,
                                                       app_name=app_name))

        and_app = dict(app=os.path.join(env_reader.get_env_base_path(), env_reader.get_env_config()['app_name']),
                       platformName=PLATFORM, platformVersion=VERSION, deviceName=DEVICE_NAME, noReset=NO_RESET,
                       automationName=AUTOMATION_NAME, newCommandTimeout=NEW_COMMAND_TIMEOUT_SECONDS)
        dr_mobile = dict(command_executor=COMMAND_EXECUTOR,
                         desired_capabilities=and_app)
        self.driver = MobileDriver(dr_mobile=dr_mobile).driver
        MobileDriver.driver = self.driver

    def close_app(self):
        if self.driver is not None:
            ScreenshotUtils.take_screenshot(self.driver)
            self.driver.close_app()
