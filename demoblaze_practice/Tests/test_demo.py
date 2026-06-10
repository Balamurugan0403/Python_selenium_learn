import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.smoke
@pytest.mark.order(1)
@pytest.mark.dependency(name="login")
def test_login(setup):

    driver = setup

    driver.find_element(By.ID, "login2").click()
    time.sleep(2)

    driver.find_element(By.ID, "loginusername").send_keys("karthiksiva")
    driver.find_element(By.ID, "loginpassword").send_keys("karthik@123")

    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    time.sleep(3)

    welcome = driver.find_element(By.ID, "nameofuser").text

    assert "Welcome" in welcome


@pytest.mark.regression
@pytest.mark.order(2)
@pytest.mark.dependency(depends=["login"])
def test_add_to_cart(setup):

    driver = setup

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))).click()

    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Add to cart").click()

    time.sleep(2)

    alert = Alert(driver)
    alert.accept()

    assert True


@pytest.mark.regression
@pytest.mark.order(3)
@pytest.mark.dependency(depends=["login"])
def test_place_order(setup):

    driver = setup

    driver.find_element(By.ID, "cartur").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

    time.sleep(2)

    assert driver.find_element(By.ID, "name").is_displayed()
