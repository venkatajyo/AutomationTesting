from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://profile.w3schools.com/login?redirect_url=https%3A%2F%2Fwww.w3schools.com%2Fhtml%2F")
ele = driver.find_element(By.NAME, "email")
pw = driver.find_element(By.NAME, "password")

print(ele.is_displayed())
print(ele.is_enabled())
print(pw.is_displayed())
print(pw.is_enabled())
ele.send_keys("aravavenkatajyothi@gmail.com")
pw.send_keys("Jyothi@5")
login_ele = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[3]/button[2]').click()
time.sleep(15)


