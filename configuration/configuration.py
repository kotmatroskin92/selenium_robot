# coding=utf-8

# Default test environment
ENV = "dev"

# Browser Settings
# Supported browsers: "chrome", "firefox", "ie", "remote"
BROWSER = "chrome"

# Geckodriver version. Use last if None.
GECKODRIVER_VERSION = "v0.23.0"

# Headless Settings
# Supported values: "y", "n"
HEADLESS = "n"

# Localization
# Supported locale: "en"
LOCALE = "en"

# Selenoid Settings (remote browser)
SELENOID_HOST = "host"
SELENOID_PORT = "4444"
SELENOID_URL = "http://{host}:{port}/wd/hub".format(host=SELENOID_HOST, port=SELENOID_PORT)

# Waiting settings (seconds)
IS_PRESENT_IMPLICIT_TIMEOUT = 1
IMPLICIT_WAIT_TIMEOUT = 20
EXPLICIT_WAIT_TIMEOUT = 20
PAGE_LOAD_TIMEOUT = 50
SCRIPT_TIMEOUT = 20
IS_EXIST_TIMEOUT = 20

# Appium Settings
DEVICE_NAME = 'Nexus_6_API_26'
APPIUM_HOST = '127.0.0.1'
APPIUM_PORT = '4723'
COMMAND_EXECUTOR = 'http://{ip}:{port}/wd/hub'.format(ip=APPIUM_HOST, port=APPIUM_PORT)
WAIT_ELEMENT_SECONDS = 15
NEW_COMMAND_TIMEOUT_SECONDS = 40
PLATFORM = 'Android'
VERSION = '8.0'
AUTOMATION_NAME = "UiAutomator2"
NO_RESET = True
