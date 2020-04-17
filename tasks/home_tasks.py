from pages.home_page import HomePage
from actions.mouse import Mouse

class HomeTasks(object):
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)

    def click_on_numbers(self):
        elements = self.home_page.numbers_list()

        def sortSecond(val): 
            return val[1] 

        numbers = []
        for i, element in enumerate(elements):
            if element.text != '':
                numbers.append((i, int(element.text)))
        numbers.sort(key = sortSecond)
        for number in numbers:
            print("clicking on number", elements[number[0]].text)
            Mouse.click(elements[number[0]])

    def check_score(self):
        return self.home_page.game_score() == "50"