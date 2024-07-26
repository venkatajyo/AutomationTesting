import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the webpage
driver.get("https://jqueryui.com/droppable/")

# Wait for the iframe to be available and switch to it
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'demo-frame'))
)

# Wait for the draggable and droppable elements to be present
source_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'draggable'))
)
target_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'droppable'))
)

# Perform drag-and-drop action
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()

# Optional: Wait to see the effect
WebDriverWait(driver, 2).until(
    EC.text_to_be_present_in_element((By.ID, 'droppable'), 'Dropped!')
)
time.sleep(3)
# Close the WebDriver
driver.quit()
