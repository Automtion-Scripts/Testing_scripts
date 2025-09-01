import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)    
action = webdriver.ActionChains(driver)

def double_click():
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HTML10"]/div[1]/button')))
    action.double_click(button).perform()
    print("Button double clicked successfully.")

# def right_click():
#     button = wait.until(EC.element_to_be_clickable((By.ID, 'field2')))
#     action.context_click(button).perform()
#     print("Button right clicked successfully.")

try:
    double_click()
    # right_click()
except Exception as e:      
    print("Test Failed:", e)
finally:  
    time.sleep(2)
    driver.quit()