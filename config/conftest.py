import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from read_config import get_config


@pytest.fixture()
def test_setup_and_teardown(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def valid_term():
    return get_config("Search term", "validterm")  


@pytest.fixture()
def invalid_term():
    return get_config("Search term", "invalidterm")