from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from helper.configuration_manager import ConfigurationManager


class WebDriverManager:
    @staticmethod
    def set_chrome_options() -> webdriver.ChromeOptions:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_insecure_certs = True
        chrome_options.headless = ConfigurationManager().headless()

        return chrome_options

    def get_driver(self) -> webdriver:
        driver = webdriver.Chrome(options=self.set_chrome_options(),
                                  service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(ConfigurationManager().timeout())
        driver.maximize_window()

        return driver
