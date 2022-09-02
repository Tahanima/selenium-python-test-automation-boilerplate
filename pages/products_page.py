from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def get_title(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, 'title').text
