import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(request):

    driver = webdriver.Chrome()

    driver.get("https://demoblaze.com")
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.quit()
