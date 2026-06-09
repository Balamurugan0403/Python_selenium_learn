import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from read_config import get_config


@pytest.fixture()
def test_setup_and_teardown(request):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    url = get_config("Basic info", "url")
    browser = get_config("Basic info", "browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()

    else:
        raise Exception("Invalid browser")

    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.quit()


@pytest.fixture()
def username():
    return get_config("login", "username")


@pytest.fixture()
def password():
    return get_config("login", "password")