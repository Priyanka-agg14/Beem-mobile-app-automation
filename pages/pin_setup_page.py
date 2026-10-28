from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class PinSetupPage(BasePage):
    SETUP_PIN_CARD = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Setup a 4-digit Beem PIN"]/ancestor::android.view.ViewGroup[1]'
    )
    PIN_BOXES = (AppiumBy.XPATH, '//*[@resource-id="otp-input"]')
    CONFIRM_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text, "Confirm")] | //*contains(@content-desc, "Confirm")]'
    )

    def click_setup_pin_if_present(self):
        try:
            self.click(self.SETUP_PIN_CARD)
        except Exception:
            pass

    def enter_initial_pin(self, pin_code):
        boxes = self.find_elements(self.PIN_BOXES)
        boxes[0].click()
        self.execute_mobile_type(pin_code)

    def enter_confirm_pin(self, pin_code):
        try:
            self.find_element(self.CONFIRM_HEADER)
        except Exception:
            pass

        boxes = self.find_elements(self.PIN_BOXES)
        boxes[0].click()
        self.execute_mobile_type(pin_code)