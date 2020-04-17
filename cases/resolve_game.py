import unittest
import time 
from drivers.driver import create_driver
from config import BASE_PATH
from tasks.home_tasks import HomeTasks

class ResolveGameTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = create_driver()
        self.driver.get(BASE_PATH)
        self.home_tasks = HomeTasks(self.driver)

    def test_click_on_all_numbers_asap(self):
        self.home_tasks.click_on_numbers()
        self.home_tasks.click_on_numbers()
        # assert self.home_tasks.check_score(), "50"
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
