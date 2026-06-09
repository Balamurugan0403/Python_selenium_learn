import pytest
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Utilities"))

import excelReader
import pytest_check as check

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import logCreator


@pytest.mark.usefixtures("setup")
class TestLogin:
    logger = logCreator.log_generator()
    excel_path = Path(__file__).parent.parent / "TestData" / "Logindata.xlsx"

    @pytest.mark.parametrize(
        "username,password", excelReader.get_data(excel_path, "Sheet1")
    )
    def test_valid_login(self, username, password):
        self.logger.info(f"Starting login test for user: {username}")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login2"))
        ).click()
        self.logger.info("Clicked login button")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "logInModalLabel"))
        )

        self.driver.find_element(By.ID, "loginusername").clear()
        self.driver.find_element(By.ID, "loginusername").send_keys(username)

        self.driver.find_element(By.ID, "loginpassword").clear()
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.logger.info("Entered credentials")

        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        self.logger.info("Clicked Log in button")

        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        )

        check.is_true(welcome_message.is_displayed(), "Welcome message not displayed")
        check.is_in(username, welcome_message.text, "Username not in welcome message")

        self.logger.info(f"Login passed! Welcome text: {welcome_message.text}")
        print(f"Login passed! Welcome text: {welcome_message.text}")
