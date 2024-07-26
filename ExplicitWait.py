"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#Bengaluru, Karnataka, India
#Kochi, Kerala, India
try:
    # Initialize the WebDriver (e.g., using Chrome)
    driver = webdriver.Chrome()

    # Set the implicit wait time to a higher value (e.g., 10 seconds)
    driver.implicitly_wait(10)

    # Maximize the browser window
    driver.maximize_window()

    # Open the desired web page
    driver.get("https://www.expedia.com/")

    # Wait until the "Flights" tab is present and clickable
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Flights']"))
    )

    # Click the "Flights" tab
    element.click()

    # Wait for a couple of seconds to see the effect
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="FlightSearchForm_ROUND_TRIP"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/button').send_keys("Bengaluru, Karnataka, India")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="FlightSearchForm_ROUND_TRIP"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/button').send_keys("Kochi, Kerala, India")
    time.sleep(2)
    element = driver.find_element(By.ID, 'date_form_field-btn')
    element.send_keys("Aug 4 - Aug 5")
    time.sleep(3)

   driver.find_element(By.ID, 'search_button').click()


except selenium.common.exceptions.TimeoutException:
    print("Page took too long to load")

except selenium.common.exceptions.InvalidSelectorException:
    print("Invalid XPath selector")
finally:
    # Close the browser
    driver.quit()
"""