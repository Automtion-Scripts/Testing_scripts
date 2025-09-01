import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

def dynamic_button():
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HTML5"]/div[1]/button')))
    button.click()
    print("Button clicked successfully.")
    button.click()
    print("Button clicked successfully again.") 

try:
    dynamic_button()
except Exception as e:
    print("Test Failed:", e)    

finally:  
    time.sleep(2)
    driver.quit()