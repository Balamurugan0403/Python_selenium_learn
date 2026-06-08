from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://automationexercise.com")
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
                    src.includes('googleads')   ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')       ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")


if driver.title == "Automation Exercise":
    print("Homepage loaded")
else:
    print("Homepage not loaded")

signupButton = driver.find_element(By.XPATH, '//*[@id="header"]//div[@class="shop-menu pull-right"]/ul/li[4]/a[text()=" Signup / Login"]')
signupButton.click()

signupText = driver.find_element(By.XPATH, value='//div[@class="signup-form"]/h2')
if signupText.is_displayed():
    print("new signup Text is visible")
else:
    print("new signupText is not visible")

name = driver.find_element(By.XPATH, "//input[@name='name']")
name.send_keys("bala")
email = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
email.send_keys("bala7994@gmail.com")
signupbutton = driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]")
signupbutton.click()
errormes=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-qa='signup-email']/following-sibling::p[text()='Email Address already exist!']")))
errormes=errormes.text
assert "Email Address already exist!" in errormes
print("the email id already exist")