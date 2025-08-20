import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

def login(username, password):
    """Perform login with given credentials"""
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_label")))
    print("Login successful")

def sort_products():
    """sort products by price(A to Z)"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"product_sort_container"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inventory_filter_container']/select/option[1]"))).click()
    print("Products sorted by price (A to Z)")

def sort_products():
    """sort products by price(Z to A)"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"product_sort_container"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inventory_filter_container']/select/option[2]"))).click()
    print("Products sorted by price (Z to A)")

def sort_products():
    """sort products by price(low to high)"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"product_sort_container"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inventory_filter_container']/select/option[3]"))).click()
    print("Products sorted by price (low to high)")

def sort_products():
    """sort products by price(high to low)"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"product_sort_container"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inventory_filter_container']/select/option[4]"))).click()
    print("Products sorted by price (high to low)")

try:
    login ('standard_user','secret_sauce')
    sort_products()

except Exception as e:
    print("Test Failed:", e)    
finally:
    time.sleep(3)
    driver.quit()