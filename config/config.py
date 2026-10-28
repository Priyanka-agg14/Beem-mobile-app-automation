import os


class Config:
    # Appium Server & Device Settings
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4724")
    PLATFORM_NAME = os.getenv("PLATFORM_NAME", "Android")
    DEVICE_NAME = os.getenv("DEVICE_NAME", "Android")
    PLATFORM_VERSION = os.getenv("PLATFORM_VERSION", "16")

    # App Package & Paths
    APP_PATH = os.getenv("APP_PATH", "/Users/blank/Downloads/app-release_new.apk")
    APP_PACKAGE = "com.useline.line"
    APP_ACTIVITY = "com.useline.line.MainActivity"
    APP_WAIT_ACTIVITY = "com.useline.line.*"

    # Test Data
    DEFAULT_PHONE = "7100000450"
    DEFAULT_OTP = "9191"
    DEFAULT_PIN = "1234"

    # Wait Times
    EXPLICIT_WAIT = 20