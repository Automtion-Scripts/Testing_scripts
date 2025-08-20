import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 10)

try:
    # Enter username
    user_name = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("standard_user")

    # Enter password
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")

    # Click login
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # ✅ Check login success (if "Products" page loads)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_label")))
    print("Login Successful")

except Exception as e:
    print("Login Unsuccessful:", e)

finally:
    time.sleep(5)  # observe result
    driver.quit()
