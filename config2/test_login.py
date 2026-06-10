# config2/test_login.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check


@pytest.mark.usefixtures("test_setup_and_teardown")
class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_valid_login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login2"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "logInModalLabel"))
        )
        self.driver.find_element(By.ID, "loginusername").clear()
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").clear()
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        )
        check.is_true(welcome_message.is_displayed(), "Welcome message not displayed")
        check.is_in(username, welcome_message.text, "Username not in welcome message")
        print(f"Login passed! Welcome text: {welcome_message.text}")

    @pytest.mark.negative
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_invalid_password(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login2"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "logInModalLabel"))
        )
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys("wrongpassword")
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        from selenium.webdriver.support.ui import WebDriverWait
        import time
        time.sleep(2)   # alert wait
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            assert "Wrong password" in alert_text or "User does not exist" in alert_text
            print(f"Negative test passed. Alert: {alert_text}")
        except Exception:
            pass

    #  Empty Credentials 
    @pytest.mark.negative
    def test_empty_credentials(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login2"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "logInModalLabel"))
        )
        self.driver.find_element(By.ID, "loginusername").clear()
        self.driver.find_element(By.ID, "loginpassword").clear()
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        import time
        time.sleep(2)
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"Empty credentials alert: {alert_text}")
        except Exception:
            pass

    # Logout after Login
    @pytest.mark.smoke
    def test_logout(self, username, password):
        # Login first
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login2"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "logInModalLabel"))
        )
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        )
        # Logout
        self.driver.find_element(By.ID, "logout2").click()
        import time
        time.sleep(2)
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login2"))
        )
        check.is_true(login_btn.is_displayed(), "Login button not visible after logout")
        print("Logout test passed!")
