from pages.home_page import HomePage
from actions.mouse import Mouse

class HomeTasks(object):
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)

    def click_on_right_color(self):
        elements = self.home_page.get_clickable_color()
        Mouse.click(elements[0])

    def get_score(self):
        element = self.home_page.game_score()
        return int(element.text)

    def get_time(self):
        element = self.home_page.game_time()
        return int(element.text)

    def get_result(self):
        element = self.home_page.game_result()
        return int(element.text)