import pytest
from selenium import webdriver

@pytest.fixture()
def test_setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()