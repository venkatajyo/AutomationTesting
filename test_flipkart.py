import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown WebDriver
    driver.quit()


"""def test_open_flipkart(driver):
    driver.get("https://www.flipkart.com/")
    assert "Flipkart" in driver.title"""
import re

def test_open_flipkart(driver):
    driver.get("https://www.flipkart.com/")
    title = driver.title
    assert re.search(r'Online Shopping Site for Mobiles|Electronics|Furniture|Grocery', title)


def test_close_login_popup(driver):
    try:
        close_login_popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "✕")]'))
        )
        close_login_popup.click()
    except:
        print("Login popup did not appear or could not be closed.")

def test_search_product(driver):
    search_box = driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
    search_box.send_keys("selenium book")
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]')
        )
    )

def test_click_product_link(driver):
    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]')
        )
    )
    product_link.click()
    driver.switch_to.window(driver.window_handles[1])

def test_enter_pincode(driver):
    pincode_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter Delivery Pincode"]'))
    )
    pincode_input.send_keys("524132")

def test_check_pincode_button(driver):
    check_pincode_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Check"]'))
    )
    check_pincode_button.click()

def test_scroll_to_add_to_cart_button(driver):
    add_to_cart_button_xpath = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button'
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, add_to_cart_button_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    assert add_to_cart_button.is_displayed()

def test_click_add_to_cart_button(driver):
    add_to_cart_button_xpath = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button'
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_to_cart_button_xpath))
    )
    add_to_cart_button.click()

def test_checkout_page(driver):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button'))
    )

def test_scroll_to_place_order_button(driver):
    place_order_button_xpath = '//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button'
    place_order_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, place_order_button_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView();", place_order_button)
    assert place_order_button.is_displayed()

def test_click_place_order_button(driver):
    place_order_button_xpath = '//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button'
    place_order_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, place_order_button_xpath))
    )
    place_order_button.click()

def test_observe_results(driver):
    time.sleep(5)  # Optional: Wait to observe results
