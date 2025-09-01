import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 25)

def check_home_checkbox():
    """Function to check the 'Home' checkbox and validate the selection."""
    # Click the expand button to reveal all checkboxes
    expand_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='tree-node']/ol/li/span/button")))
    expand_button.click()
    if expand_button:
        print("Expand button clicked successfully.")
    else:
        print("Failed to click the expand button.")

    # Select the 'Home' checkbox
    home_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"label[for='tree-node-home'] span.rct-checkbox")))
    home_checkbox.click()

    # Validate that the 'Home' checkbox is selected
    result = wait.until(EC.presence_of_element_located((By.ID, "result")))
    if "home" in result.text.lower():
        print("Home checkbox is selected successfully.")
    else:
        print("Failed to select the Home checkbox.")

try:
    check_home_checkbox()
except Exception as e:
    print("Test Failed:", e)    
finally:
    time.sleep(3)
    driver.quit()
