from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class LoginPage(BasePage):
    PHONE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="text-input-flat"]')
    CONTINUE_BTN = (
        AppiumBy.XPATH,
        '//android.widget.Button[@text="Continue"] | //android.widget.TextView[@text="Continue"] | //*[@content-desc="Continue"]'
    )

    def enter_phone_number(self, phone_number):
        self.send_keys(self.PHONE_INPUT, phone_number)
        self.hide_keyboard()

    def click_continue(self):
        self.click(self.CONTINUE_BTN)