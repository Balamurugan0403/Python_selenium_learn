from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
options = ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
simplealert=wait.until(ec.visibility_of_element_located((By.ID,"alertBtn"))).click()
alert=driver.switch_to.alert
print("simple alert:",alert.text)
alert.accept()

confirmationalert=wait.until(ec.visibility_of_element_located((By.ID,"confirmBtn"))).click()
confirmalert=driver.switch_to.alert
print("confirmation alert:",confirmalert.text)
confirmalert.accept()

promptalert=wait.until(ec.visibility_of_element_located((By.ID,"promptBtn"))).click()
prompt=driver.switch_to.alert
print("the prompt alert:",prompt.text)
prompt.send_keys("the user entered their name")
prompt.accept()


