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

def add_items_to_cart(items):
    """Add multiple items to the cart by their button text"""
    for item in items:
        # Locate each button using product name
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"))
        )
        button.click()
        print(f"Added {item} to cart")

def view_cart():
    """Click cart and verify"""
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    print("Opened cart")

try:
    login("standard_user", "secret_sauce")
    
    # List of products to add
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    
    add_items_to_cart(products)
    view_cart()
    
    # Verify items inside cart
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print("Items in cart:")
    for item in cart_items:
        print("-", item.text)

except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(5)
    driver.quit()
