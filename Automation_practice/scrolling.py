import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)  # Correct usage

def scrolling():
    # Wait until element is visible
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    
    # Scroll to the element
    actions.move_to_element(element).perform()
    if element.is_displayed():
        print("Scrolled to element successfully.")  
    else:
        print("Failed to scroll to element.")
try:    
    scrolling()
except Exception as e:
    print("Test Failed:", e)
finally:  
    time.sleep(5)
    driver.quit()
