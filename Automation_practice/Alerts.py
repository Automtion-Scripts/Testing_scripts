import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 30)

def handle_alerts():
        # # Simple Alert
        # simple_alert_button = wait.until(EC.element_to_be_clickable((By.ID, 'alertBtn')))
        # simple_alert_button.click()
        # alert = driver.switch_to.alert
        # print("Simple Alert Text:", alert.text)
        # alert.accept()
       

        # Confirmation Alert
        # confirm_alert_button = wait.until(EC.element_to_be_clickable((By.ID, 'confirmBtn')))
        # confirm_alert_button.click()
        # alert = driver.switch_to.alert
        # print("Confirmation Alert Text:", alert.text)
        # alert.accept()
       

        # Prompt Alert
        prompt_alert_button = wait.until(EC.element_to_be_clickable((By.ID, 'promptBtn')))
        prompt_alert_button.click()
        alert = driver.switch_to.alert
        print("Prompt Alert Text:", alert.text)
        alert.send_keys("Muskaan Sahu")
        alert.accept()
        

try:
    handle_alerts()
    # print("Simple Alert accepted.")
    # print("Confirmation Alert dismissed.")
    # print("Prompt Alert handled.")
    print("Prompt Alert accepted with input.")

except Exception as e:
    print("Error handling alerts:", e)

finally:
    time.sleep(5)
    driver.quit()