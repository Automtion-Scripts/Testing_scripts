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
wait = WebDriverWait(driver, 15)


def login(username, password):
    """Perform login with given credentials"""
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_label")))
    print("Login successful")

def add_to_cart():
    """View first item and add to cart"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_img"))).click()
    
    # Wait for the item details page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_desc")))
    
    # Click the "Add to cart" button
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_primary.btn_inventory")))
    add_to_cart_button.click()
    print("Item added to cart")

    # Navigate to inventory page to verify item is added
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_details_back_button"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    
    # # Check if the cart badge is updated
    # cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    # if cart_badge.text == "1":
    #     print("Item successfully added to cart")
    # else:
    #     print("Item not added to cart as expected") 

def logout():
    """Open menu and logout"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bm-burger-button"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    print("Logout successful and verified")


try:
    login("standard_user", "secret_sauce")
    add_to_cart()
    logout()
    # Verify item added to cart
    
except Exception as e:
    print("Login Unsuccessful or Add to cart is failed", e)

finally:
    time.sleep(10)  # observe result
    driver.quit()
