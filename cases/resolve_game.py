import unittest
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
        assert True, True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
