from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def dismiss_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll(
                "iframe, .adsbygoogle, [id*='google_ads'], [id*='aswift']"
            ).forEach(el => el.remove());
        """)
        print("Ads removed")
    except Exception as e:
        print("No ads found:", e)


options = Options()
options.add_argument("--headless")
service = Service(ChromeDriverManager().install())
d = webdriver.Chrome(service=service, options=options)
d.set_page_load_timeout(30)

wait = WebDriverWait(d, 10)

try:
    d.get("https://automationexercise.com/")
    dismiss_ads(d)

    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='item active']//button[@type='button'][normalize-space()='Test Cases']",
            )
        )
    ).click()

    testCaseMessage = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[normalize-space()='Test Cases']")
        )
    ).text

    print("Test Case heading:", testCaseMessage)
    assert testCaseMessage == "Test Cases", f"Unexpected heading: '{testCaseMessage}'"
    print("Test Passed")

except AssertionError as ae:
    print(f"Assertion Failed: {ae}")
    raise

except Exception as e:
    print(f"Test Error: {e}")
    raise

finally:
    d.quit()
    print("Browser closed")
