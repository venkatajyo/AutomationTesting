import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
element = driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
actions = ActionChains(driver)
actions.context_click(element).perform()
time.sleep(3)
