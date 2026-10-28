from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class OtpPage(BasePage):
    OTP_BOXES = (AppiumBy.XPATH, '//*[@resource-id="otp-input"]')

    def enter_otp(self, otp_code):
        boxes = self.find_elements(self.OTP_BOXES)
        boxes[0].click()
        self.execute_mobile_type(otp_code)