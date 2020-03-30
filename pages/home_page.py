from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    
    @staticmethod
    def search_input(driver):
        return driver.find_element(By.NAME, 'q')
