from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/")
driver.find_element(By.XPATH,'//*[@id="post-2632"]/div[2]/div/div/div[1]/a').click()
print(driver.current_window_handle)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames And Windows - GlobalSQA":
        driver.close()
driver.quit()