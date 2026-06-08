from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads')  ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')      ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")

driver.get("http://automationexercise.com")
dismiss_ads(driver)
print("Home page loaded" if driver.title == "Automation Exercise" else "Home page not loaded")

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Signup / Login']"))).click()
dismiss_ads(driver)

loginmes = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Login to your account']")))
assert loginmes.is_displayed(), "login page message is not visible"

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-qa='login-email']"))).send_keys("bala7994@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("balacse@123")

wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="login-button"]'))).click()
dismiss_ads(driver)

signinmessage = wait.until(EC.visibility_of_element_located((By.XPATH, "//li//a[i[@class='fa fa-user']]")))
assert "Logged in as" in signinmessage.text, "not logged in"
print(f"'{signinmessage.text}'")

wait.until(EC.presence_of_element_located((By.XPATH,'//a[text()=" Logout"]'))).click()
assert "Automation Exercise - Signup / Login" in driver.title
print("moved to login page")
