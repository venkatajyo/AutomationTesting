import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Click the radio button using JavaScript
radio_button = driver.find_element(By.ID, 'RESULT_RadioButton-7_0')
driver.execute_script("arguments[0].click();", radio_button)

time.sleep(3)  # Optional sleep for demonstration purposes

# Check if the radio button is selected
radio_selected = driver.find_element(By.ID, 'RESULT_RadioButton-7_0').is_selected()
print(f"Is radio button selected? {radio_selected}")

# Click the checkboxes
checkbox1 = driver.find_element(By.ID, 'RESULT_CheckBox-8_0')
checkbox2 = driver.find_element(By.ID, 'RESULT_CheckBox-8_6')

# Click checkboxes using JavaScript
driver.execute_script("arguments[0].click();", checkbox1)
driver.execute_script("arguments[0].click();", checkbox2)

time.sleep(3)  # Optional sleep for demonstration purposes

driver.quit()
