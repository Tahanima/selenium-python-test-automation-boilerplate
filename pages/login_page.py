from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def go_to(self):
        self.driver.get(self.configs.base_url())

        return self

    def enter_username(self, username: str):
        _username = self.driver.find_element(By.ID, 'user-name')

        _username.clear()
        _username.send_keys(username)

        return self

    def enter_password(self, password: str):
        _password = self.driver.find_element(By.ID, 'password')

        _password.clear()
        _password.send_keys(password)

        return self

    def click_login(self):
        self.driver.find_element(By.ID, 'login-button').click()

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, 'error-message-container').find_element(By.TAG_NAME, 'h3').text
