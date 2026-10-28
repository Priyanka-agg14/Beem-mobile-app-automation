from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config


class DriverFactory:
    @staticmethod
    def create_driver():
        desired_caps = {
            "platformName": Config.PLATFORM_NAME,
            "deviceName": Config.DEVICE_NAME,
            "automationName": "UiAutomator2",
            "platformVersion": Config.PLATFORM_VERSION,
            "app": Config.APP_PATH,
            "appPackage": Config.APP_PACKAGE,
            "appActivity": Config.APP_ACTIVITY,
            "appWaitActivity": Config.APP_WAIT_ACTIVITY,
            "appium:autoGrantPermissions": True,
            "noReset": False,
            "newCommandTimeout": 300,
        }

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote(
            command_executor=Config.APPIUM_SERVER_URL,
            options=capabilities_options
        )

        if driver.current_package != Config.APP_PACKAGE:
            driver.activate_app(Config.APP_PACKAGE)

        return driver