import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

def login(username, password):
    """Perform login with given credentials"""
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_label")))
    print("Login successful")

def logout():
    """Open menu and logout"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bm-burger-button"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    print("Logout successful and verified")

try:
    login("standard_user", "secret_sauce")
    logout()
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    time.sleep(3)
    driver.quit()
