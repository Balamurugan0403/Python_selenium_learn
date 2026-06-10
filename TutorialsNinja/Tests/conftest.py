import pytest
from selenium import webdriver
from Utility import configReader


@pytest.fixture()
def upAndDown(request):
    browser= configReader.config_Read("basic info", "browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome()
    else:
        print("Invalid Browser")
    driver.maximize_window()
    driver.implicitly_wait(15)
    url = configReader.config_Read("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
