import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check


@pytest.mark.usefixtures("test_setup_and_teardown")
class TestLogin:

    def test_valid_login(self,username,password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logInModalLabel")))
        self.driver.find_element(By.ID, "loginusername").clear()
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").clear()
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        welcome_message= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser")))

        check.is_true(welcome_message.is_displayed(),              "Welcome message not displayed")
        check.is_in(username,welcome_message.text,              "Username not in welcome message")
        print(f"Login passed! Welcome text: {welcome_message.text}")
