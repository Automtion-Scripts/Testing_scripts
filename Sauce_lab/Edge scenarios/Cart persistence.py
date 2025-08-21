import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

def login(username, password):
    """Perform login with given credentials"""
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_label")))
    print("Login successful")

def add_to_cart(product_name):
    """Add a product to the cart by its name"""
    product = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")))
    product.click()
    print("added to cart")

def logout():
    """Open menu and logout"""
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu_button_container > div > div:nth-child(3) > div"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    print("Logout successful and verified")

def login(username, password):
    """Perform login with given credentials"""
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_label")))
    print("Login successful")

def navigate_to_cart():
    """Navigate to the cart page"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    print("Navigated to cart page")
    # Verify cart is empty
    cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
    if not cart_items:
        print("Cart is empty")
    else:
        print(f"Cart contains {len(cart_items)} items")

try:
    login("standard_user", "secret_sauce")
    add_to_cart("Sauce Labs Backpack")
    logout()
    login("standard_user", "secret_sauce")
    navigate_to_cart()
    
except Exception as e:
    print(f"Test Failed: {e}")
finally:
    time.sleep(3)
    driver.quit()
