from pages.home_page import HomePage
from actions.input import Input

class HomeTasks(object):
    @staticmethod
    def search_for(driver, text):
        element = HomePage.search_input(driver)
        Input.text(element, text)
        Input.key_return(element)
        