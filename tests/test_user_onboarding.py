import logging
from config.config import Config
from pages.onboarding_page import OnboardingPage
from pages.login_page import LoginPage
from pages.otp_page import OtpPage
from pages.pin_setup_page import PinSetupPage
from pages.home_page import HomePage

logger = logging.getLogger(__name__)

def test_user_onboarding_and_login(driver):
    logger.info("Initializing Page Objects...")
    onboarding_page = OnboardingPage(driver)
    login_page = LoginPage(driver)
    otp_page = OtpPage(driver)
    pin_setup_page = PinSetupPage(driver)
    home_page = HomePage(driver)

    logger.info("Step 1: Clicking Sign In")
    onboarding_page.click_sign_in()

    logger.info("Step 2: Entering Phone Number & Continuing")
    login_page.enter_phone_number(Config.DEFAULT_PHONE)
    login_page.click_continue()

    logger.info("Step 3: Submitting OTP")
    otp_page.enter_otp(Config.DEFAULT_OTP)

    logger.info("Step 4: Setting up PIN")
    pin_setup_page.click_setup_pin_if_present()
    pin_setup_page.enter_initial_pin(Config.DEFAULT_PIN)
    pin_setup_page.enter_confirm_pin(Config.DEFAULT_PIN)

    logger.info("Step 5: Dismissing optional overlays and verifying Home Screen")
    home_page.dismiss_bottom_sheet_if_present()

    assert home_page.is_home_screen_displayed(), "User failed to land on the Home Screen!"
    logger.info("Test Passed: User successfully reached the Home Screen.")