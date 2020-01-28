# coding=utf-8
import os
import allure
from PIL import Image
from allure_commons.types import AttachmentType
from vlogging import VisualRecord
from framework.constant import ScreenshotConst
from framework.robotwrappers.RobotLogger import RobotLogger
from framework.web.browser.Browser import Browser
from robot.api import logger


class ScreenshotUtils:
    __screen_number = ScreenshotConst.NUMBER_OF_FIRST_SCREEN
    __screen_dir = os.path.join(os.getcwd(), ScreenshotConst.PATH_TO_SCREENSHOTS)

    @staticmethod
    def get_screen_file_name(file_format=ScreenshotConst.FILE_FORMAT_PNG):
        scr_number = str(ScreenshotUtils.__screen_number)
        ScreenshotUtils.__screen_number += 1
        return "Screenshot_" + scr_number + file_format

    @staticmethod
    def save_screenshot(driver=Browser.get_driver()):
        screen_name = ScreenshotUtils.get_screen_file_name()
        save_screen_path = os.path.join(ScreenshotUtils.__screen_dir, screen_name)
        RobotLogger.info("Save screenshot to file " + screen_name)
        if not os.path.exists(ScreenshotUtils.__screen_dir):
            os.mkdir(ScreenshotUtils.__screen_dir)
        driver.save_screenshot(save_screen_path)
        result_image = Image.open(save_screen_path)
        RobotLogger.info(VisualRecord(screen_name, result_image))

    @staticmethod
    def take_screenshot(driver=Browser.get_driver(), width=ScreenshotConst.IMG_WIDTH_MEDIUM):
        result_image = driver.get_screenshot_as_base64()
        logger.info('<img src="data:image/png;base64,{0}" width="{1}">'.format(result_image, width), html=True)
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
