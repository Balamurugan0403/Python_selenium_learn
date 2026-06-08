from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
wait = WebDriverWait(driver, 10)
alertButton = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alertButton.click()
alert = driver.switch_to.alert       
print(alert.text)              
alert.accept()    
                    
print("Alert accepted")
confirmButton = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirmButton.click()
confirm = driver.switch_to.alert
print(confirm.text)
confirm.accept()                     

promptButton = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
promptButton.click()
prompt = driver.switch_to.alert
prompt.send_keys("Balamurugan")       
prompt.accept()                    

driver.quit()