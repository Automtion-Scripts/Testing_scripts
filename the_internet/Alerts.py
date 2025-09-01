from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click button to trigger alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Switch to alert
alert = driver.switch_to.alert

print("Alert text:", alert.text)   # Read alert message
alert.accept()                    # Click OK
time.sleep(2)

driver.quit()
