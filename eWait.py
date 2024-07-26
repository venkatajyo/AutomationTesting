import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()

try:
    # Set the implicit wait time to a higher value (e.g., 10 seconds)
    driver.implicitly_wait(10)

    # Maximize the browser window
    driver.maximize_window()

    # Open the desired web page
    driver.get("https://www.expedia.co.in")
    print("Opened Expedia website")

    # Wait until the "Flights" tab is present and clickable
    flights_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="multi-product-search-form-1"]/div/div[1]/ul/li[2]/a/span'))
    )
    flights_tab.click()
    print("Clicked on Flights tab")

    # Wait until the "Leaving from" input is present and interactable
    from_input_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Flights']"))
    )
    from_input_button.click()
    print("Clicked on Leaving from button")

    from_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="location-field-leg1-origin"]'))
    )
    from_input.send_keys("Bengaluru, Karnataka, India")
    print("Entered Leaving from location")

    # Wait until the "Going to" input is present and interactable
    to_input_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="location-field-leg1-destination-menu"]/div[1]/button'))
    )
    to_input_button.click()
    print("Clicked on Going to button")

    to_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="location-field-leg1-destination"]'))
    )
    to_input.send_keys("Kochi, Kerala, India")
    print("Entered Going to location")

    # Wait until the date input is present and interactable
    date_input_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'd1-btn'))
    )
    date_input_button.click()
    print("Clicked on date input button")

    # Interact with the date picker (adjust according to the actual implementation)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='30 Jul 2024']"))
    ).click()
    print("Selected start date")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='5 Aug 2024']"))
    ).click()
    print("Selected end date")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Done']"))
    ).click()
    print("Clicked on Done button")

    # Wait until the search button is present and interactable
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button'))
    )
    search_button.click()
    print("Clicked on search button")

except selenium.common.exceptions.TimeoutException as e:
    print(f"TimeoutException: {e}")
except selenium.common.exceptions.NoSuchElementException as e:
    print(f"NoSuchElementException: {e}")
except selenium.common.exceptions.ElementClickInterceptedException as e:
    print(f"ElementClickInterceptedException: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
