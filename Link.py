from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/")
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    print(link.text)
#driver.find_element(By.PARTIAL_LINK_TEXT,"SQL Tutorial").click()#alternativewayof clicking text
driver.find_element(By.LINK_TEXT,"SQL T").click()