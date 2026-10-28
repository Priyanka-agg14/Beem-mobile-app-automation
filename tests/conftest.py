import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver():
    driver_instance = DriverFactory.create_driver()
    yield driver_instance
    driver_instance.quit()