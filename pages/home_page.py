from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def game_time(self):
        locator = (By.ID, 'time')
        return self.get_by(locator)

    def game_score(self):
        locator = (By.ID, 'score')
        return self.get_by(locator)

    def game_result(self):
        locator = (By.CSS_SELECTOR, '.resultContent .level')
        return self.get_by(locator)

    def get_clickable_color(self):
        locator = (By.CSS_SELECTOR, '.grid > .main')
        return self.get_all_by(locator)
