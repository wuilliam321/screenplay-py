from config import BASE_PATH
from pages.base_page import BasePage

class HomePage(BasePage):
    @staticmethod
    def search_input(driver):
        return driver.find_element_by_name('q')
