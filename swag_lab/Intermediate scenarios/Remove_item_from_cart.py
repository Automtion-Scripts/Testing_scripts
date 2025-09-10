import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Setup driver ---
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# --- Functions ---
def login(user, pwd):
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(user)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(pwd)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    print("Login successful")

def add_items(items):
    for item in items:
        xpath = f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        print(f"Added {item}")

def navigate_to_cart():
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
    print("Navigated to cart")

def remove_items(items):
    """Remove multiple items from the cart"""
    for item in items:
        xpath = f"//div[text()='{item}']/ancestor::div[@class='cart_item']//button"
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        print(f"Removed {item}")

def verify_cart_empty():
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    if not cart_items:
        print("Cart is empty")
    else:
        print("Cart is not empty, remaining items:")
        for item in cart_items:
            print("-", item.text)

# --- Test Flow ---
try:
    login("standard_user", "secret_sauce")
    
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Onesie"]
    add_items(products_to_add)
    
    navigate_to_cart()
    
    products_to_remove = ["Sauce Labs Backpack"]
    remove_items(products_to_remove)
    
    verify_cart_empty()

except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(3)
    driver.quit()
    print("Browser closed")
