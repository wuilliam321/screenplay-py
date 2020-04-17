from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def get_by(self, locator):
        return self.wait_for(locator)

    def wait_for(self, locator):
        # TODO: make this 3 value a configurable value
        WebDriverWait(self.driver, 5).until(
            lambda driver: self.driver.find_element(*locator))
        return self.driver.find_element(*locator)


    def get_all_by(self, locator):
        return self.wait_for_all(locator)

    def wait_for_all(self, locator):
        # TODO: make this 5000 value a configurable value
        WebDriverWait(self.driver, 5000).until(
            lambda driver: self.driver.find_elements(*locator))
        return self.driver.find_elements(*locator)