from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_by(driver, locator):
        return BasePage.wait_for(driver, locator)

    @staticmethod
    def wait_for(driver, locator):
        # TODO: make this 5000 value a configurable value
        WebDriverWait(driver, 5000).until(
            lambda driver: driver.find_element(*locator))
        return driver.find_element(*locator)