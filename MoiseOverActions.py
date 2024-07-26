import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/html/default.asp")
python = driver.find_element(By.XPATH,'//*[@id="subtopnav"]/a[5]')
actions = ActionChains(driver)

actions.move_to_element(python).click().perform()
driver.quit()