import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Setup driver ---
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# --- Functions ---
def login(user, pwd):
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(user)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(pwd)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    print("Login successful")

def verify_details_page():
    #verify the details page of the product
    click_button= wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='item_4_title_link']/div")))
    click_button.click()
    print("Clicked on the product details page")

    #verify the product details
    product_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name"))).text
    product_description = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_desc"))).text
    product_price = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_price"))).text   
    print(f"Product Name: {product_name}")
    print(f"Product Description: {product_description}")
    print(f"Product Price: {product_price}")    

    # back to inventory
    Back_button= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_details_back_button"))) 
    Back_button.click()
    print("Back to inventory page")
# --- Main Execution ---
try:
    login("standard_user", "secret_sauce")
    verify_details_page()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
    print("Driver closed")
    time.sleep(2)  # Wait for a moment before closing the driver
    print("Script execution completed")