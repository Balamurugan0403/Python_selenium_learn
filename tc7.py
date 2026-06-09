from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    d.get("https://automationexercise.com")

    products = d.find_element(By.XPATH, "//a[@href='/products']")
    products.click()

    dismiss_ads(d)
    items = d.find_elements(By.XPATH, "//img/following-sibling::p")
    product_names = [i.text for i in items]
    count = len(product_names)
    assert count > 0, "No products found on page"
    print(f"Product count: {count} products found")

    first_product = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='productinfo text-center']/following-sibling::div//a[normalize-space()='View Product'])[1]",
            )
        )
    )
    first_product.click()

    title = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='product-information']//h2")
        )
    ).text

    assert title == "Blue Top", f"Unexpected title: '{title}'"
    print(f"Product title verified: '{title}'")
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
