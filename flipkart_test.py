import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    driver.maximize_window()

    # Open the Flipkart website
    driver.get("https://www.flipkart.com/")

    # Close the login popup if it appears
    try:
        close_login_popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "✕")]'))
        )
        close_login_popup.click()
    except:
        print("Login popup did not appear or could not be closed.")

    # Locate the search input box
    search_box = driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')

    # Enter the search text
    search_box.send_keys("selenium book")
    print("Name entered")

    # Submit the search
    search_box.send_keys(Keys.RETURN)  # This simulates pressing the Enter key to submit the form

    # Wait for search results to load
    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]')
        )
    )
    print("Product link found")

    # Locate and click the product link
    product_link.click()
    print("Clicked on the product link")

    # Switch to new tab if needed (Optional)
    driver.switch_to.window(driver.window_handles[1])

    # Enter pincode
    pincode_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter Delivery Pincode"]'))
    )
    pincode_input.send_keys("524132")
    print("Pincode entered")

    # Click 'Check' button
    check_pincode_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Check"]'))
    )
    check_pincode_button.click()
    print("Clicked Check button")

    # Scroll to the 'Add to Cart' button until it is visible
    add_to_cart_button_xpath = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button'
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, add_to_cart_button_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    print("Scrolled to the Add to Cart button")

    # Wait for 'Add to Cart' button to be clickable
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_to_cart_button_xpath))
    )
    print("Add to Cart button found and is visible")
    print(add_to_cart_button.is_displayed())

    # Click the 'Add to Cart' button
    add_to_cart_button.click()
    print("Clicked the Add to Cart button")

    # Wait for the checkout page to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button'))
    )
    print("Checkout page loaded")

    # Scroll to the 'Place Order' button until it is visible
    place_order_button_xpath = '//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button'
    place_order_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, place_order_button_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView();", place_order_button)
    print("Scrolled to the Place Order button")

    # Check if the 'Place Order' button is displayed
    place_order_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, place_order_button_xpath))
    )
    print("Place Order button found and is visible")
    print(place_order_button.is_displayed())

    # Click the 'Place Order' button
    place_order_button.click()
    print("Clicked the Place Order button")

    # Optional: Wait to observe results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
