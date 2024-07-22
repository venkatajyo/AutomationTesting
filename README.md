
This project is designed to automate interactions with the Flipkart website using Selenium and Python.

## Test Cases

The following test cases are implemented to verify the functionality of the Flipkart website:

### 1. `test_open_flipkart(driver)`
- **Objective:** Verify that the Flipkart website loads correctly and check the page title.
- **Details:** Opens the Flipkart homepage and asserts that the title contains a specific substring.

### 2. `test_close_login_popup(driver)`
- **Objective:** Ensure that the login popup (if it appears) is closed properly.
- **Details:** Waits for the login popup close button to be clickable and clicks it.

### 3. `test_search_product(driver)`
- **Objective:** Test the search functionality on the Flipkart homepage.
- **Details:** Locates the search input box, enters a search term (`"selenium book"`), and submits the search.

### 4. `test_click_product_link(driver)`
- **Objective:** Click on the first product link in the search results.
- **Details:** Clicks on the product link and switches to the new tab that opens.

### 5. `test_enter_pincode(driver)`
- **Objective:** Enter a delivery pincode on the product page.
- **Details:** Waits for the pincode input field to be present and enters a sample pincode (`"524132"`).

### 6. `test_check_pincode_button(driver)`
- **Objective:** Click the "Check" button after entering the pincode.
- **Details:** Waits for the "Check" button to be clickable and then clicks it.

### 7. `test_scroll_to_add_to_cart_button(driver)`
- **Objective:** Scroll to the "Add to Cart" button to ensure it is visible.
- **Details:** Locates the "Add to Cart" button, scrolls it into view, and verifies its visibility.

### 8. `test_click_add_to_cart_button(driver)`
- **Objective:** Click the "Add to Cart" button.
- **Details:** Clicks the "Add to Cart" button to add the product to the cart.

### 9. `test_checkout_page(driver)`
- **Objective:** Verify that the checkout page loads after adding the product to the cart.
- **Details:** Waits for a specific element on the checkout page to be present.

### 10. `test_scroll_to_place_order_button(driver)`
- **Objective:** Scroll to the "Place Order" button to ensure it is visible.
- **Details:** Locates the "Place Order" button, scrolls it into view, and verifies its visibility.

### 11. `test_click_place_order_button(driver)`
- **Objective:** Click the "Place Order" button.
- **Details:** Clicks the "Place Order" button to proceed with the order.

### 12. `test_observe_results(driver)`
- **Objective:** (Optional) Wait to observe the results of the actions performed in the previous tests.
- **Details:** Introduces a delay to allow observation of the results.

## How to Run Tests

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

