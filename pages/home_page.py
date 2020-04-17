from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def search_input(self):
        locator = (By.NAME, 'q')
        return self.get_by(locator)
