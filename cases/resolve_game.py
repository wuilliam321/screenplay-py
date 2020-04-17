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

    def test_click_on_right_color_as_many_as_possible(self):
        try:
            while(self.home_tasks.get_time() > 0):
                self.home_tasks.click_on_right_color()
        except:
            assert self.home_tasks.get_result() > 0, True
             

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
