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

def fetch_all_products():
    products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    for index, product in enumerate(products, start=1):
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        desc = product.find_element(By.CLASS_NAME, "inventory_item_desc").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        image = product.find_element(By.CLASS_NAME, "inventory_item_img").get_attribute("src")

        print(f"\nProduct {index}:")
        print(f" Name: {name}")
        print(f" Description: {desc}")
        print(f" Price: {price}")
        print(f" Image URL: {image}")

try:
    login("standard_user", "secret_sauce")
    fetch_all_products()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
    print("Driver closed")
    time.sleep(2)  # Wait for a moment before closing the driver
    print("Script execution completed")