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
wait = WebDriverWait(driver, 30)


# # Locate element to hover
menu_element = driver.find_element(By.CLASS_NAME, "dropbtn")

# Create ActionChains object
actions = ActionChains(driver)

# Perform hover
actions.move_to_element(menu_element).perform()
print("Mouse hovered on 'Point me'")


time.sleep(3)
driver.quit()


