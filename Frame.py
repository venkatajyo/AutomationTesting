from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/")

# Wait until the "HTML Headings" link is clickable
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "HTML Headings"))
    )
    element.click()
    print("Clicked on HTML Headings")
except Exception as e:
    print(f"Error: {e}")

# Wait for the page to load
time.sleep(3)

# Wait until the "Python Tutorial" link is clickable
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Python Tutorial"))
    )
    element.click()
    print("Clicked on Python Tutorial")
except Exception as e:
    print(f"Error: {e}")

# Wait for the page to load
time.sleep(3)

# Quit the driver
driver.quit()
