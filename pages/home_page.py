from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class HomePage(BasePage):
    BOTTOM_SHEET_BACKDROP = (
        AppiumBy.XPATH,
        '//*[@content-desc="Bottom sheet backdrop"] | //*[@resource-id="backdrop"]'
    )
    WELCOME_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Welcome")]')
    HOME_TAB = (AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')

    def dismiss_bottom_sheet_if_present(self):
        try:
            self.click(self.BOTTOM_SHEET_BACKDROP)
        except Exception:
            pass

    def is_home_screen_displayed(self):
        welcome_visible = self.find_element(self.WELCOME_HEADER).is_displayed()
        tab_visible = self.find_element(self.HOME_TAB).is_displayed()
        return welcome_visible and tab_visible