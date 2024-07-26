import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(18)
driver.maximize_window()
time.sleep(4)
"""
#first approach
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)

flag=driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]')
driver.execute_script("arguments[0].scrollIntoView();", flag)
time.sleep(2)
"""
#thirdApproach
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)