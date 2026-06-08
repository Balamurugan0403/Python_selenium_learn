from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


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


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
wait = WebDriverWait(driver, 10)

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

password = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("balacse123")
firstName = driver.find_element(By.XPATH, value="//input[@id='first_name']")
firstName.send_keys("bala")
lastName = driver.find_element(By.XPATH, value="//input[@id='last_name']")
lastName.send_keys("murugan")

address = driver.find_element(By.XPATH, value="//input[@id='address1']")
address.send_keys("24,ragavendra street")
state = driver.find_element(By.XPATH, value="//input[@id='state']")
state.send_keys("tamilnadu")
city = driver.find_element(By.XPATH, value="//input[@id='city']")
city.send_keys("salem")
zipcode = driver.find_element(By.XPATH, value="//input[@id='zipcode']")
zipcode.send_keys("634256")
mobile = driver.find_element(By.XPATH, value="//input[@id='mobile_number']")
mobile.send_keys("1234567890")
# dismiss_ads(driver)

createAccountButton = driver.find_element(By.XPATH, value="//button[contains(text(),'Create Account')]")
createAccountButton.click()

successText = driver.find_element(By.XPATH, value='//*[@id="form"]/div/div/div/h2/b')
if successText.is_displayed:
    print("Account created")
else:
    print("Account not created")

continueBut = driver.find_element(By.XPATH, value='//div[@class="pull-right"]/a[text()="Continue"]')
continueBut.click()

loggedInElement = wait.until(
    expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="header"]//a[contains(text(),"Logged in as")]')
    )
)
loginmessage = loggedInElement.text

if "Logged in as bala" in loginmessage:
    print("Message displayed")
else:
    print("Message not displayed")

deleteButton = driver.find_element(By.XPATH, value='//*[@id="header"]//div[@class="shop-menu pull-right"]//li[5]/a[text()=" Delete Account"]')
driver.execute_script("arguments[0].click();", deleteButton)

deletemessage = driver.find_element(By.XPATH, value='//*[@id="form"]//div/h2/b')
if deletemessage.is_displayed():
    print("Account Deleted")
else:
    print("Account not deleted")

continuebutton = driver.find_element(By.XPATH, value='//*[@id="form"]/div/div/div/div/a')
continuebutton.click()

driver.close()