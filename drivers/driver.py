from selenium import webdriver
import config as cfg

def create_driver():
    def create_driver_instance():
        if (cfg.ENV_DRIVER == "firefox"):
            from selenium.webdriver.firefox.options import Options
            options = Options()
            if cfg.HEADLESS:
                options.headless = True
            return webdriver.Firefox(options=options)
        else:
            from selenium.webdriver.chrome.options import Options
            options = Options()
            if cfg.HEADLESS:
                options.add_argument('--headless')
            return webdriver.Chrome(cfg.DRIVER_PATH, options=options)
    return create_driver_instance()
