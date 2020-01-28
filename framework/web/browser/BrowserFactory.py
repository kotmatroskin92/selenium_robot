# coding=utf-8
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from configuration import configuration as config
from framework.constant import Browsers
from framework.utils.ConfigReader import ConfigReader


class BrowserFactory:

    @staticmethod
    def get_browser_driver():
        browser = ConfigReader().get_browser()
        is_headless = ConfigReader().get_headless()
        locale = ConfigReader().get_locale()
        if browser == Browsers.BROWSER_REMOTE:
            pass
        else:
            if browser == Browsers.BROWSER_CHROME:
                chrome_options = ChromeOptions()
                chrome_options.add_argument("--lang={}".format(locale))
                if is_headless == 'true':
                    chrome_options.add_argument("--headless")
                return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
            elif browser == Browsers.BROWSER_FIREFOX:
                firefox_profile = FirefoxProfile()
                firefox_profile.set_preference("intl.accept_languages", locale)
                return webdriver.Firefox(executable_path=GeckoDriverManager(config.GECKODRIVER_VERSION).install(),
                                         firefox_profile=firefox_profile)
            elif browser == Browsers.IE:
                return webdriver.Ie(IEDriverManager().install())

    @staticmethod
    def get_remote_driver(browser_name, browser_version):
        capabilities = {
            "browserName": browser_name,
            "version": browser_version,
            # "enableVNC": configuration.IS_VNC_ENABLED,
            # "enableVideo": configuration.IS_VIDEO_ENABLED
        }
        return webdriver.Remote(command_executor=config.SELENOID_URL,
                                desired_capabilities=capabilities)
