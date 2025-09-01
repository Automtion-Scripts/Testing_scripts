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

def drag_and_drop():
    source = wait.until(EC.element_to_be_clickable((By.ID, 'draggable')))
    target = wait.until(EC.element_to_be_clickable((By.ID, 'droppable')))
    action.drag_and_drop(source, target).perform()
    print("Drag and drop action performed successfully.")

try:
    drag_and_drop()
except Exception as e:  
    print("Test Failed:", e)
finally:  
    time.sleep(5)
    driver.quit()