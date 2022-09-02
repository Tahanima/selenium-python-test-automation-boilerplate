import unittest
from abc import abstractmethod

from helper.configuration_manager import ConfigurationManager
from helper.webdriver_manager import WebDriverManager


class BaseTest(unittest.TestCase):
    @abstractmethod
    def initialize(self):
        pass

    def setUp(self):
        self.driver = WebDriverManager().get_driver()
        self.configs = ConfigurationManager()
        self.initialize()

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
