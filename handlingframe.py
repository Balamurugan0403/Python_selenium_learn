from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://letcode.in/frame")
driver.maximize_window()

action = ActionChains(driver)
driver.switch_to.frame("firstFr")

print("switched to frame")
driver.find_element(By.NAME, "fname").send_keys("micheal")
driver.find_element(By.NAME, "lname").send_keys("johnson")
print("filled the first and last name")

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
print("find the innerframe")
driver.find_element(By.NAME, "email").send_keys("mike422@gmail.com")
print("all fields filled")
driver.switch_to.parent_frame()
print("Switched back to parent frame (firstFr)")
driver.switch_to.default_content()
print("Switched back to main page (defaultContent)")

action.pause(5).perform()
driver.quit()