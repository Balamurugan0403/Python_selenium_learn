import pytest
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")

def teardown_function(function):
    driver.quit()


def test_adidas():                                         # ❌ should fail
    driver.find_element(By.NAME, "search").send_keys("adidas")
    driver.find_element(
        By.XPATH, "//button[@class='btn btn-default btn-lg']"
    ).click()

    # ✅ This WILL fail — adidas product link won't exist
    check.equal(
        driver.find_elements(By.LINK_TEXT, "adidas") != [],
        True,
        "No adidas product found"                          # ❌ FAIL — no product!
    )


def test_iphone():                                         # ✅ should pass
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys("iPhone")
    driver.find_element(
        By.XPATH, "//button[@class='btn btn-default btn-lg']"
    ).click()

    iphone_element = driver.find_element(By.LINK_TEXT, "iPhone")
    check.is_true(iphone_element.is_displayed(), "iPhone link not displayed")  # ✅ PASS
    check.is_in("iPhone", driver.title,          "iPhone not in title")        # ✅ PASS