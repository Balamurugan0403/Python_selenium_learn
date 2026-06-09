from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import Select
options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
country=driver.find_element(By.ID,"country")
dropdown=Select(country)
dropdown.select_by_value("usa")
print("country selected")
dropdown.select_by_index(3)
print(dropdown.first_selected_option.text)
dropdown.select_by_visible_text("China")
print(dropdown.first_selected_option.text)
# cannot use the all_selected_option in this dropdwon because it is single select dropdown


print("performing select on mutiple selectable options")
colors=driver.find_element(By.ID,"colors")
dropdown=Select(colors)
optionlist=dropdown.options
for option in optionlist:
    print(option.text)
dropdown.select_by_index(1)
dropdown.select_by_value("green")
#there is multiple option of "green"
print("Is multiple:",dropdown.is_multiple)
selected_options = dropdown.all_selected_options
# can store the value in set and prints only one time
result = set()

for option in selected_options:
    if option.text not in result:
        print(option.text)
        result.add(option.text)
