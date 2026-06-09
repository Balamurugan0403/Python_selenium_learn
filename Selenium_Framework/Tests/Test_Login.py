import pytest
from pathlib import Path

import pytest_check as check

from Utilities import excelReader
from Utilities import logCreator

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestLogin:

    logger = logCreator.log_generator()

    excel_path = (
        Path(__file__).parent.parent
        / "TestData"
        / "Logindata.xlsx"
    )

    @pytest.mark.parametrize(
        "username,password",
        excelReader.get_data(excel_path, "Sheet1")
    )
    def test_valid_login(self, username, password):

        # DEBUG — detailed step info
        self.logger.debug(
            f"Test started with username='{username}', password='{password}'"
        )

        # INFO — normal flow
        self.logger.info(
            f"Starting login test for user: {username}"
        )

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.ID, "login2")
                )
            ).click()
            self.logger.info("Clicked login button")

        except Exception as e:
            # ERROR — something failed unexpectedly
            self.logger.error(
                f"Failed to click login button: {e}"
            )
            raise

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.ID, "logInModalLabel")
                )
            )
            self.logger.debug("Login modal is visible")

        except Exception as e:
            self.logger.error(
                f"Login modal did not appear: {e}"
            )
            raise

        self.driver.find_element(By.ID, "loginusername").clear()
        self.driver.find_element(By.ID, "loginusername").send_keys(username)

        self.driver.find_element(By.ID, "loginpassword").clear()
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)

        self.logger.info("Entered credentials")

        self.driver.find_element(
            By.XPATH,
            "//button[text()='Log in']"
        ).click()

        self.logger.info("Clicked Log in button")

        try:
            WebDriverWait(self.driver, 5).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # WARNING — login alert means invalid credentials
            self.logger.warning(
                f"Login alert appeared for user '{username}': {alert_text}"
            )

            alert.accept()

        except Exception:
            # DEBUG — no alert is normal/expected
            self.logger.debug("No alert found — proceeding normally")

        try:
            welcome_message = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(
                    (By.ID, "nameofuser")
                )
            )

        except Exception as e:
            # ERROR — login did not succeed
            self.logger.error(
                f"Welcome message not found for user '{username}': {e}"
            )
            raise

        check.is_true(
            welcome_message.is_displayed(),
            "Welcome message not displayed"
        )

        check.is_in(
            username,
            welcome_message.text,
            "Username not in welcome message"
        )

        # INFO — test passed
        self.logger.info(
            f"Login passed! Welcome text: {welcome_message.text}"
        )

        print(
            f"Login passed! Welcome text: {welcome_message.text}"
        )

        try:
            logout = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.ID, "logout2")
                )
            )
            logout.click()
            self.logger.info("Logged out successfully")

        except Exception as e:
            # WARNING — logout failed but test already passed
            self.logger.warning(
                f"Logout failed for user '{username}': {e}"
            )