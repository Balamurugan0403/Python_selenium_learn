import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check


@pytest.mark.usefixtures("test_setup_and_teardown")
class TestProduct:

    def test_valid_product(self, valid_term):
        self.driver.find_element(By.NAME, "search").send_keys(valid_term)
        self.driver.find_element(
            By.XPATH, "//button[@class='btn btn-default btn-lg']"
        ).click()

        result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='content']/h1"))
        )

        check.is_in(valid_term.lower(), result.text.lower(), f"{valid_term} not found in results")
        check.is_in(valid_term.lower(), self.driver.title.lower(), f"{valid_term} not in title")
        print(f"Valid search '{valid_term}' passed!")

    def test_invalid_product(self, invalid_term):
        self.driver.find_element(By.NAME, "search").send_keys(invalid_term)
        self.driver.find_element(
            By.XPATH, "//button[@class='btn btn-default btn-lg']"
        ).click()

        expected_text = "There is no product that matches the search criteria."
        actual_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(),'There is no product')]")
            )
        ).text

        check.is_in(expected_text, actual_text, "No product message not shown")
        print(f"Invalid search '{invalid_term}' passed!")