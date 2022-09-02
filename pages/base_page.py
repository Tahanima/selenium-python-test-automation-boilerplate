from selenium import webdriver
from helper.configuration_manager import ConfigurationManager


class BasePage:
    def __init__(self, driver: webdriver, configs: ConfigurationManager):
        self.driver = driver
        self.configs = configs
