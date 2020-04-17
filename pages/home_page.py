from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def game_board(self):
        locator = (By.ID, 'grid')
        return self.get_by(locator)

    def numbers_list(self):
        locator = (By.CSS_SELECTOR, '#grid > div')
        return self.get_all_by(locator)
