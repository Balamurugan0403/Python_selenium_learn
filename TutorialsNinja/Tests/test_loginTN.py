import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Utility.excelDP import get_Excel_Data
from Utility import logCreators


@pytest.mark.parametrize(
    "username,password",
    get_Excel_Data(
        "TutorialsNinja/DataProviders/loginTestTN",
        "loginTestTN",
    ),
)
@pytest.mark.usefixtures("upAndDown")
class TestLoginTN:

    def test_ValidLogin(self, username, password):

        log = logCreators.log_generator()
        wait = WebDriverWait(self.driver, 15)

        my_account = wait.until(
            ec.element_to_be_clickable((By.XPATH, "//a[@title='My Account']"))
        )
        my_account.click()

        wait.until(
            ec.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[@class='dropdown open']/child::ul/li/a[text()='Login']",
                )
            )
        ).click()

        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//input[@name='email']"))
        ).send_keys(username)

        log.info("Username Entered")

        self.driver.find_element(By.XPATH, value="//input[@name='password']").send_keys(
            password
        )

        log.info("Password Entered")

        wait.until(
            ec.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        ).click()

        log.info("Clicked Login Button")

        try:
            actual = wait.until(
                ec.visibility_of_element_located(
                    (By.XPATH, "//div[@id='content']/child::h2[text()='My Account']")
                )
            ).text

            assert actual.__contains__("My Account")
            log.info("Login Successful")

        except Exception as e:

            log.info("Login Failed")

            try:
                error = wait.until(
                    ec.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//div[@id='account-login']/child::ul/following::div[@class='alert alert-danger alert-dismissible']",
                        )
                    )
                ).text

                log.info(error)

            except:
                log.info(e)
