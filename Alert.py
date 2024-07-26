from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://testautomationpractice.blogspot.com/")

# Find the button by its XPath and click it
button = driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button[1]')
button.click()  # Click the button to trigger the alert

# Use WebDriverWait to wait for the alert to be present
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()  # Accept the alert
    print("Alert was accepted")
except:
    print("No alert appeared")

# Optionally, you can add some wait time before closing the driver
time.sleep(2)

# Close the browser
driver.quit()
