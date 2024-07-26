from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/")

print(driver.title)
driver.get("https://www.w3schools.com/css/default.asp")

print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
print(driver.title)