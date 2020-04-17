from selenium.webdriver.common.keys import Keys

class Mouse(object):
    @staticmethod
    def click(element):
        element.click()