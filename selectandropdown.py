from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
wait = WebDriverWait(driver, 10)

dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, "dropdown")))
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Option 1")
print("Selected by text:", driver.find_element(By.ID, "dropdown").get_attribute("value"))
dropdown.select_by_value("2")
print("Selected by value:", driver.find_element(By.ID, "dropdown").get_attribute("value"))
dropdown.select_by_index(1)
print("Selected by index:", driver.find_element(By.ID, "dropdown").get_attribute("value"))
dropdown.select_by_index(2)
print("Selected by index:",driver.find_element(By.ID,"dropdown").get_attribute("value"))