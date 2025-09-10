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

def add_items_to_cart(items):
    """Add multiple items to the cart by their button text"""
    for item in items:
        # Locate each button using product name
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"))
        )
        button.click()
        print(f"Added {item} to cart")

def Checkout():
    """Click cart and verify and click checkout button"""
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a"))).click()
    print("Opened cart")
    
    # Click checkout button
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button"))).click()
    print("Clicked checkout button")  

    #enter user details
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Muskaan")
    last_name = wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("Sahu")
    Postal_code = wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("")
    print("Entered user details")

    # Click continue button
    continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn_primary.cart_button")))
    continue_button.click()
    print("Checkout process continued")


    # Capture and print confirmation text
    Error_text = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout_info_container']/div/form/h3"))
    ).text
    print("Checkout flow completed successfully")
    print("Confirmation message:", Error_text)



# --- Main Execution ---
try:
    login("standard_user","secret_sauce")
    # List of products to add
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    add_items_to_cart(products)
    Checkout()  

except Exception as e:
    print("Test Failed:", e)
finally:
    time.sleep(5)
    driver.quit()

