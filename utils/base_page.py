# Appium Base Page wrapper with explicit wait methods for click and type
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def execute_mobile_type(self, text):
        self.driver.execute_script("mobile: type", {"text": text})

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass