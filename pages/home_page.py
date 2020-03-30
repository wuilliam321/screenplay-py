from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    
    @staticmethod
    def search_input(driver):
        locator = (By.NAME, 'q')
        return BasePage.get_by(driver, locator)
