import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox", "edge"])
def test_setup_and_teardown(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "Edge":
        driver = webdriver.Edge()
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
