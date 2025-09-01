import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 15)

def select_option_by_value(value):
    dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdown"))).click()

    option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dropdown']/option[3]"))).click()
    print(" option selected successfully.")

try:
    select_option_by_value("3")
except Exception as e:
    print("Test Failed:", e)    
finally:
    time.sleep(3)
    driver.quit()




