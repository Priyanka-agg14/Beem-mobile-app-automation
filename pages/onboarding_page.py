from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class OnboardingPage(BasePage):
    SIGN_IN_BTN = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Sign in"]')

    def click_sign_in(self):
        self.click(self.SIGN_IN_BTN)