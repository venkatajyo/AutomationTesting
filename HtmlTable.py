import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the desired webpage
driver.get('file:///C:/Users/hp/OneDrive/Documents/AutomationTesting.html')  # Replace with your target URL
time.sleep(4)

try:
    # Find all rows and columns in the table
    rows = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr')
    cols = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[1]/th')

    # Get the number of rows and columns
    number_of_rows = len(rows)
    number_of_cols = len(cols)

    print(f"Number of rows in the table: {number_of_rows}")
    print(f"Number of columns in the table: {number_of_cols}")

    # Iterate through rows and columns to get cell values
    for r in range(1, number_of_rows + 1):
        for c in range(1, number_of_cols + 1):
            try:
                value = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[{r}]/td[{c}]').text
                print(value, end=' ')
            except NoSuchElementException:
                print( end=' ')
        print()  # Print a newline after each row

finally:
    # Ensure the WebDriver closes regardless of success or failure
    driver.quit()
