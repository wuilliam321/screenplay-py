from pages.home_page import HomePage
from actions.input import Input

class HomeTasks(object):
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)

    def search_for(self, text):
        element = self.home_page.search_input()
        Input.text(element, text)
        Input.key_return(element)
        