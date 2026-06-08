from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads')   ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')       ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
wait = WebDriverWait(driver, 10)
dismiss_ads(driver)
assert driver.title=="Automation Exercise","not navigated to homepage."
print(driver.title)
contactUs = driver.find_element(By.XPATH, "//a[@href='/contact_us']")
driver.execute_script("arguments[0].click();", contactUs)
verifycontactpage = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="contact-form"]/h2')))
assert verifycontactpage.text=="GET IN TOUCH"
print("verified the text")
name=wait.until(EC.visibility_of_element_located((By.NAME,"name"))).send_keys("guru")
email=wait.until(EC.visibility_of_element_located((By.NAME,"email"))).send_keys("bala7994@gmail.com")
subjectbox=wait.until(EC.visibility_of_element_located((By.NAME,"subject"))).send_keys("Test Automation Query")
messagebox=wait.until(EC.visibility_of_element_located((By.NAME,"message"))).send_keys("This is a test message sent via Selenium automation for testing purpose.")
