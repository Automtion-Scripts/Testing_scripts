import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get ("https://www.saucedemo.com/v1/")
driver.maximize_window()

#explicit wait
wait = WebDriverWait(driver, 50)

try:
    # Enter username
    user_name = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("locked_out_user")

    # Enter password
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")

    # Click login
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # ❌ Verify login failed (check error message)
    error_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
    print("Login Unsuccessful as expected. Error:", error_msg.text)

except Exception as e:
    print("Test Failed - Unexpected behavior:", e)

finally:
    time.sleep(5)
    driver.quit()

