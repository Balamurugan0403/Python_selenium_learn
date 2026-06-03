from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
title=  driver.title
exptitle="automation testing practice"
if(exptitle in title.lower()):
    print("title correct")
print(title)
time.sleep(5)
driver.close()

