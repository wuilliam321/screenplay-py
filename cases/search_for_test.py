import unittest
from drivers.driver import create_driver
from config import BASE_PATH
from tasks.home_tasks import HomeTasks
from tasks.window_tasks import WindowTasks

class SearchForTest(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()
        self.driver.get(BASE_PATH)

    def test_home_search_input_should_change_window_title(self):
        HomeTasks.search_for(self.driver, 'pycon')
        title = WindowTasks.get_title(self.driver)
        assert title, 'Python'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
