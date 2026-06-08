import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_validproduct(test_setup_and_teardown):
    driver.find_element(By.NAME,"search").send_keys("iPhone")
    driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT,value="iPhone").is_displayed()

def test_invalidproduct(test_setup_and_teardown):
    driver.find_element(By.NAME,"search").send_keys("pulsar")
    driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
    expected_text="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,value="//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_text)

def test_no_of_product(test_setup_and_teardown):
    driver.find_element(By.NAME,"search").send_keys("nx100")
    driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
    expected_text="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,value="//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_text)