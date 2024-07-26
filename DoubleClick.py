import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
element = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
actions = ActionChains(driver)
actions.double_click(element).perform()
time.sleep(3)
