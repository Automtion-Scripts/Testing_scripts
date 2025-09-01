import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/entry_ad")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 15)

try:
    #wait for the modal to appear
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"modal")))
    print("Modal is visible.")
    # Click the close button
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#modal > div.modal > div.modal-footer > p")))
    close_button.click()
    print("Modal closed successfully.")
except Exception as e:
    print("Test Failed:", e)    
finally:
    time.sleep(3)
    driver.quit()

