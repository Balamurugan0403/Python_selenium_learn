import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup_and_teardown")
class TestSearch:

    def test_validproduct(self):

        self.driver.find_element(
            By.NAME,
            "search"
        ).send_keys("iPhone")

        self.driver.find_element(
            By.XPATH,
            "//button[@class='btn btn-default btn-lg']"
        ).click()

        assert self.driver.find_element(
            By.LINK_TEXT,
            "iPhone"
        ).is_displayed()

    def test_invalidproduct(self):

        self.driver.find_element(
            By.NAME,
            "search"
        ).send_keys("pulsar")

        self.driver.find_element(
            By.XPATH,
            "//button[@class='btn btn-default btn-lg']"
        ).click()

        expected_text = (
            "There is no product that matches the search criteria."
        )

        actual_text = self.driver.find_element(
            By.XPATH,
            "//p[contains(text(),'There is no product that matches the search criter')]"
        ).text

        assert actual_text == expected_text

    def test_no_of_product(self):

        self.driver.find_element(
            By.NAME,
            "search"
        ).send_keys("nx100")

        self.driver.find_element(
            By.XPATH,
            "//button[@class='btn btn-default btn-lg']"
        ).click()

        expected_text = (
            "There is no product that matches the search criteria."
        )

        actual_text = self.driver.find_element(
            By.XPATH,
            "//p[contains(text(),'There is no product that matches the search criter')]"
        ).text

        assert actual_text == expected_text