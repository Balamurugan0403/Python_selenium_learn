from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import Select
import time
options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

textbox = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
driver.execute_script("arguments[0].value='Selenium';",textbox)
driver.execute_script("arguments[0].click();",button)
driver.execute_script("return document.URL;")
driver.execute_script("return document.title;")

driver.execute_script("window.scrollTo(0,500);")

simple_alert = driver.find_element(By.ID, "alertBtn")
driver.execute_script("arguments[0].scrollIntoView(true);",simple_alert)
time.sleep(2)
driver.execute_script("arguments[0].click();",simple_alert)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
button = driver.find_element(By.ID, "alertBtn")
text = driver.execute_script("return arguments[0].innerText;",button)
print(text)
driver.quit()