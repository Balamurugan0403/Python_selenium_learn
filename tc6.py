from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick')       ||
                    src.includes('googleads')         ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')             ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")


def scroll_to_element(driver, element):
    """Scrolls the page until the given WebElement is in view."""
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        element
    )
    print(f"Scrolled to element: <{element.tag_name}>")


def scroll_by_amount(driver, x=0, y=500):
    """Scrolls the page by the given pixel amount (x = horizontal, y = vertical)."""
    driver.execute_script(f"window.scrollBy({x}, {y});")
    print(f"Scrolled by x={x}px, y={y}px")

service = Service(GeckoDriverManager().install())
driver  = webdriver.Firefox(service=service, options=options)
driver.set_page_load_timeout(30)

wait = WebDriverWait(
    driver, 15, poll_frequency=2, ignored_exceptions=[NoSuchElementException]
)
try:
    driver.get("https://automationexercise.com/")
    dismiss_ads(driver)

    contact_link = driver.find_element(By.XPATH, "//a[normalize-space()='Contact us']")
    scroll_to_element(driver, contact_link)
    contact_link.click()

    name_field = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']"))
    )
    scroll_to_element(driver, name_field)
    name_field.send_keys("Prasanna")

    email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    scroll_to_element(driver, email_field)
    email_field.send_keys("venkatesh@gmail.com")

    subject_field = driver.find_element(By.XPATH, "//input[@placeholder='Subject']")
    scroll_to_element(driver, subject_field)
    subject_field.send_keys("Related to not working website")

    scroll_by_amount(driver, y=300)
    message_field = driver.find_element(By.XPATH, "//textarea[@id='message']")
    scroll_to_element(driver, message_field)
    message_field.send_keys("Related to not working of the website")

    upload_field = driver.find_element(By.XPATH, "//input[@name='upload_file']")
    scroll_to_element(driver, upload_field)
    upload_field.send_keys(r"C:\Users\prasa\Downloads\cybershield_report_updated.docx")

    dismiss_ads(driver)

    submit_btn = driver.find_element(By.XPATH, "//input[@name='submit']")
    scroll_to_element(driver, submit_btn)
    submit_btn.click()

    alert = wait.until(EC.alert_is_present())
    alert.accept()

    msg = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='status alert alert-success']")
        )
    ).text

    print(f"Result: {msg}")
    assert msg == "Success! Your details have been submitted successfully.", \
        f"Unexpected message: '{msg}'"
    print("Test Passed")

except Exception as e:
    print(f"Test Failed: {e}")
    raise

finally:
    driver.quit()
    print("Browser closed")