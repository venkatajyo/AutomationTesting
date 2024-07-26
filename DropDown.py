import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Locate the dropdown element
element = driver.find_element(By.ID, "RESULT_RadioButton-9")

# Create a Select object and select an option by value
drp = Select(element)
drp.select_by_value("Radio-2")

# Print all options from the dropdown
print(f"Number of options: {len(drp.options)}")
print("Options:")
for option in drp.options:
    print(option.text)

time.sleep(3)
driver.quit()
