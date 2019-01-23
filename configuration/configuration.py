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