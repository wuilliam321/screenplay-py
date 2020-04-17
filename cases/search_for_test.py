import unittest
from drivers.driver import create_driver
from config import BASE_PATH
from tasks.home_tasks import HomeTasks
from tasks.window_tasks import WindowTasks

class SearchForTest(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()
        self.driver.get(BASE_PATH)
        self.home_tasks = HomeTasks(self.driver)
        self.window_tasks = WindowTasks(self.driver)

    def test_home_search_input_should_change_window_title(self):
        self.home_tasks.search_for('pycon')
        title = self.window_tasks.get_title()
        assert title, 'Python'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
