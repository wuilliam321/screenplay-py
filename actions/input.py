from selenium.webdriver.common.keys import Keys

class Input(object):
    @staticmethod
    def text(element, value):
        element.send_keys(value)

    @staticmethod
    def key_return(element):
        element.send_keys(Keys.RETURN)