from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


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


def scroll_to_element(driver, element):
    """
    Scrolls until the given WebElement is in view using ActionChains.
    Requires Selenium 4.2+.
    """
    ActionChains(driver).scroll_to_element(element).perform()
    print(f"ActionChains: scrolled to element → <{element.tag_name}>")


def scroll_by_amount(driver, delta_x=0, delta_y=500):
    """
    Scrolls the page by the given pixel amount using ActionChains.
    """
    ActionChains(driver).scroll_by_amount(delta_x, delta_y).perform()
    print(f"ActionChains: scrolled by delta_x={delta_x}px, delta_y={delta_y}px")


options = Options()
options.add_argument("--headless")

service = Service(GeckoDriverManager().install())
d = webdriver.Firefox(service=service, options=options)
d.set_page_load_timeout(30)

wait = WebDriverWait(d, 10)


try:
    d.get("https://automationexercise.com")

    products_link = d.find_element(By.XPATH, "//a[@href='/products']")
    scroll_to_element(d, products_link)
    products_link.click()

    dismiss_ads(d)

    scroll_by_amount(d, delta_y=400)

    product_name_elements = d.find_elements(By.XPATH, "//img/following-sibling::p")
    product_names = [item.text for item in product_name_elements]
    count = len(product_names)

    assert count > 0, "No products found on the page"
    print(f"Product count: {count} products found")
    print("Product names:", product_names)

    first_product = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@class='productinfo text-center']/following-sibling::div//a[normalize-space()='View Product'])[1]",
            )
        )
    )
    scroll_to_element(d, first_product)
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
