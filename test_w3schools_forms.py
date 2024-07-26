import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = r'C:\Users\hp\OneDrive\Documents\amazonCredentials.env'
print(f"Attempting to load .env file from: {dotenv_path}")

# Load the .env file
load_dotenv(dotenv_path)

# Retrieve environment variables
VALID_EMAIL = os.getenv('VALID_EMAIL')
VALID_PASSWORD = os.getenv('VALID_PASSWORD')

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get('https://www.w3schools.com/')
    assert "W3Schools" in driver.title

def test_invalid_email_format(driver):
    driver.get('https://profile.w3schools.com/login')
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys('invalid_email_format')
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('VALID_PASSWORD')
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[3]/button[2]')
    submit_button.click()
    # Replace with actual selector and error message
    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[2]')
    assert "Please enter a valid email address" in error_message.text,"Assertion 1: The error message for invalid email format is incorrect."

def test_invalid_password(driver):
    driver.get('https://profile.w3schools.com/login')
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys('VALID_EMAIL')
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('Jyothi@3')
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[3]/button[2]')
    submit_button.click()
    # Replace with actual selector and error message
    error_message1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[2]')
    assert "Please enter a valid email address" in error_message1.text



def test_boundary_value_password(driver):
    # Step 1: Open the W3Schools login page
    driver.get('https://profile.w3schools.com/login')

    # Step 2: Locate the email input field by its name attribute and enter an invalid email (empty string in this case)
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys('')

    # Step 3: Locate the password input field by its name attribute and enter a valid password
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('P@ssw0rd')

    # Step 4: Locate the submit button using its XPath and click it
    submit_button = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[3]/button[2]')
    submit_button.click()

    # Step 5: Locate the error message element using its XPath
    error_message4 = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[2]')

    # Step 6: Assert that the expected error message is displayed
    assert "Please enter your email and password" in error_message4.text


def test_empty_email(driver):
    driver.get('https://profile.w3schools.com/login')
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys('')
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('VALID_PASSWORD')
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[3]/button[2]')
    submit_button.click()
    # Replace with actual selector and error message
    error_message3 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[2]')
    assert "Please enter your email and password" in error_message3.text

def test_empty_password(driver):
    driver.get('https://profile.w3schools.com/login')
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys('VALID_EMAIL')
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('')
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[3]/button[2]')
    submit_button.click()
    # Replace with actual selector and error message
    error_message2 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[2]')
    assert "Please enter your email and password" in error_message2.text

def test_valid_email_and_password(driver):
    driver.get('https://profile.w3schools.com/login')
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys(VALID_EMAIL)
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(VALID_PASSWORD)
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[5]/div/form/div[3]/button[2]')
    submit_button.click()
    # Replace with actual selector and success verification
    #assert "Welcome" in driver.page_source

if __name__ == "__main__":
    pytest.main()
