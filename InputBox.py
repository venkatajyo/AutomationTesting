import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Find all input boxes with the class name 'text_field'
input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')

# Print the number of input boxes found
print(len(input_boxes))
display = driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()
print(display)
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("jyothi")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("jyo")
time.sleep(7)

driver.quit()
